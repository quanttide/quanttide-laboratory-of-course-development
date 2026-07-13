# ROADMAP — 部署与前端可用性实验

> 目标：将 Provider 部署为独立服务，在实验室内操作，验证浏览器可直接播放。

---

## 阶段一：构建与部署

### 1.1 构建二进制

```bash
cd apps/qtcloud-course/src/provider
go build -o qtcloud-course-provider ./cmd/server
```

### 1.2 部署到实验室目录

实验所有产出放在 `examples/default/lab/` 下，不污染仓库其他位置：

```bash
cd examples/default

mkdir -p lab/bin
mkdir -p lab/videos/quickstart

# 部署二进制
cp ../../src/provider/qtcloud-course-provider lab/bin/

# 清理构建产物
rm ../../src/provider/qtcloud-course-provider
```

### 1.3 生成测试视频

```bash
ffmpeg -f lavfi -i "testsrc=duration=10:size=640x360:rate=24" \
  -f lavfi -i "sine=frequency=440:duration=10" \
  -c:v libx264 -c:a aac \
  lab/videos/quickstart/intro.mp4 -y
```

> 也支持下载公共领域视频替代：`curl -L -o lab/videos/quickstart/intro.mp4 "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/720/Big_Buck_Bunny_720_10s_1MB.mp4"`

### 1.4 启动服务

```bash
LISTEN_ADDR=:8080 \
  VIDEO_DIR=$PWD/lab/videos \
  lab/bin/qtcloud-course-provider
```

验证：

```bash
curl -s http://localhost:8080/healthz
# → {"status":"ok"}
```

### 1.5 一键部署脚本

```bash
#!/usr/bin/env bash
# examples/default/lab/deploy.sh
set -euo pipefail
LAB_DIR="$(cd "$(dirname "$0")" && pwd)"
PROVIDER_DIR="$(cd "$LAB_DIR/../../../src/provider" && pwd)"

echo "==> 构建二进制"
cd "$PROVIDER_DIR"
go build -o qtcloud-course-provider ./cmd/server

echo "==> 部署到 lab"
mkdir -p "$LAB_DIR/bin" "$LAB_DIR/videos/quickstart"
mv qtcloud-course-provider "$LAB_DIR/bin/"

echo "==> 生成测试视频"
ffmpeg -f lavfi -i "testsrc=duration=10:size=640x360:rate=24" \
  -f lavfi -i "sine=frequency=440:duration=10" \
  -c:v libx264 -c:a aac \
  "$LAB_DIR/videos/quickstart/intro.mp4" -y

echo "==> 启动服务"
cd "$LAB_DIR"
LISTEN_ADDR=:8080 VIDEO_DIR="$LAB_DIR/videos" ./bin/qtcloud-course-provider
```

---

## 阶段二：准备课程数据

### 2.1 一键演示脚本

```bash
#!/usr/bin/env bash
# examples/default/lab/seed-demo.sh
set -euo pipefail
BASE="${1:-http://localhost:8080}"
VIDEO_SUBDIR="${2:-quickstart}"

echo "==> 创建课时"
LESSON=$(curl -sf -X POST "$BASE/lessons" \
  -H 'Content-Type: application/json' \
  -d '{"title":"快速上手","duration":10}')
LESSON_ID=$(echo "$LESSON" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
echo "   课时: $LESSON_ID"

echo "==> 创建场景"
curl -sf -X POST "$BASE/scenes" \
  -H 'Content-Type: application/json' \
  -d "{\"lessonId\":\"$LESSON_ID\",\"videoUrl\":\"$VIDEO_SUBDIR/intro.mp4\"}" > /dev/null

echo "==> 创建课程与阶段"
COURSE=$(curl -sf -X POST "$BASE/courses" \
  -H 'Content-Type: application/json' \
  -d '{"name":"演示课程"}')
COURSE_ID=$(echo "$COURSE" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")

PHASE=$(curl -sf -X POST "$BASE/phases" \
  -H 'Content-Type: application/json' \
  -d "{\"name\":\"演示阶段\",\"courseId\":\"$COURSE_ID\",\"sortOrder\":1}")
PHASE_ID=$(echo "$PHASE" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")

curl -sf -X PUT "$BASE/phases/$PHASE_ID" \
  -H 'Content-Type: application/json' \
  -d "{\"name\":\"演示阶段\",\"sortOrder\":1,\"lessonIds\":[\"$LESSON_ID\"]}" > /dev/null

echo ""
echo "演示数据已就绪"
echo "  课程: $BASE/courses/$COURSE_ID"
echo "  视频: $BASE/video/$VIDEO_SUBDIR/intro.mp4"
```

### 2.2 运行

服务器启动后，另开终端：

```bash
bash examples/default/lab/seed-demo.sh
```

---

## 阶段三：前端播放验证

### 3.1 浏览器直接打开

```bash
open http://localhost:8080/video/quickstart/intro.mp4
```

预期：浏览器直接播放，进度条可拖动。

### 3.2 测试页面

创建 `examples/default/lab/video-test.html`：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>视频播放测试</title>
</head>
<body>
  <video controls autoplay muted width="720">
    <source src="http://localhost:8080/video/quickstart/intro.mp4" type="video/mp4">
  </video>
</body>
</html>
```

### 3.3 流式传输验证

```bash
curl -sI http://localhost:8080/video/quickstart/intro.mp4 | grep -i accept-ranges
# → Accept-Ranges: bytes

curl -s -o /dev/null -w "%{http_code}" \
  -H "Range: bytes=0-1023" \
  http://localhost:8080/video/quickstart/intro.mp4
# → 206
```

---

## 阶段四：验证清单

| # | 检查项 | 验证方法 |
|---|--------|----------|
| 1 | 二进制可独立部署 | `go build` 后部署到 `lab/bin/` |
| 2 | 视频目录在 lab 内 | `VIDEO_DIR` 指向 `lab/videos/` |
| 3 | 服务端正常启动 | `curl /healthz` → 200 |
| 4 | 视频可访问 | `curl /video/quickstart/intro.mp4` → 200 |
| 5 | 视频在浏览器中可播放 | 直接打开视频 URL |
| 6 | HTML `<video>` 可播放 | 打开 video-test.html |
| 7 | 进度拖拽正常 | Range 请求 → 206 |
| 8 | API 数据正确 | `GET /courses/{id}` → name 匹配 |

---

## 目录结构

```
examples/default/
├── ROADMAP.md
├── .gitignore          # /lab/bin /lab/videos
└── lab/
    ├── bin/            ← gitignore 编译产物
    │   └── qtcloud-course-provider
    ├── videos/         ← gitignore 视频文件
    │   └── quickstart/
    │       └── intro.mp4
    ├── deploy.sh       ← 跟踪 代码脚本
    ├── seed-demo.sh    ← 跟踪
    └── video-test.html ← 跟踪
```

所有操作在 `examples/default/` 内完成，不涉及系统目录。脚本和 HTML 进版本控制，编译产物和视频数据被过滤。
