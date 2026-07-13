# qtcloud_course_studio

Flutter 桌面应用（Linux），课程云客户端。

## 文件信息

- version: 0.0.2
- package: com.quanttide.qtcloud_course_studio
- 类型: ELF 64-bit pie executable, Linux

## 目录结构

```
bin/studio/
├── qtcloud_course_studio    # 主二进制
├── data/
│   ├── flutter_assets/      # Flutter 资源包
│   │   ├── assets/
│   │   │   ├── programs.json    # 专业/课程/阶段/课时 示例数据
│   │   │   ├── classes.json     # 班级示例数据
│   │   │   └── lesson1.json     # 课时详情（含场景/步骤/视频/选项跳转）
│   │   ├── fonts/
│   │   ├── packages/
│   │   ├── shaders/
│   │   ├── AssetManifest.bin
│   │   ├── FontManifest.json
│   │   └── version.json
│   └── icudtl.dat           # ICU 国际化数据
└── lib/
    ├── libapp.so             # Dart/Flutter 业务代码
    ├── libflutter_linux_gtk.so  # Flutter 引擎
    └── native_assets.json
```

## 功能

基于内置示例数据推断的功能：

- **专业浏览** — 查看专业（Program）列表，展开查看其下的课程（Course）、阶段（Phase）、课时（Lesson）
- **班级管理** — 查看班级列表，展示名称/关联专业或课程/状态/时间/人数/进度
- **课时播放** — 按步骤引导的教学场景（Scene），支持：
  - 分步文字指引
  - 关联视频（videoUrl）
  - 场景间跳转选择（Choice → targetSceneId）
  - 验证提示（verifyTip）

## 交互验证（GUI 自动化测试方法）

此 build 的交互能力有限（仅底部 3 个 tab 可点击），但为后续自动化测试提供了可复用的方法。

### 工具链

| 工具 | 用途 |
|------|------|
| `xvfb-run` / `Xvfb` | 虚拟显示器，无头环境运行 GUI 应用 |
| `wmctrl` | 查询窗口列表、几何位置、激活窗口 |
| `xdotool` | 鼠标点击、键盘输入、窗口聚焦 |
| `import` (ImageMagick) | 截取窗口或全屏截图 |
| `tesseract` (chi_sim) | OCR 提取界面文字，定位 UI 元素 |
| `convert` (ImageMagick) | 像素颜色探测，辅助定位导航区域 |

### 操作流程

```
启动应用 → 截图 → OCR → 解析文字位置 → xdotool 点击 → 再截图 → OCR 对比变化
```

### 关键步骤

1. **启动**：`Xvfb :99` 创建虚拟桌面，`DISPLAY=:99 ./bin/studio/qtcloud_course_studio` 启动
2. **截图**：`import -window $WID /tmp/shot.png` 截取指定窗口
3. **OCR 定位**：`tesseract shot.png stdout -l chi_sim --psm 6 tsv` 输出 TSV 格式含 bounding box
4. **颜色探测**：`convert shot.png -crop 1x1+X+Y -format "%[hex:p{0,0}]" info:` 获取像素颜色，辅助定位导航栏等区域
5. **点击**：`xdotool mousemove --window $WID $X $Y click 1` 在窗口相对坐标点击
6. **验证**：再次截图 + OCR，对比前后文字判断页面是否切换

### 精确定位点击的方法

#### 推荐方案：OpenCV 模板匹配（通用 + 抗 UI 变动）

预先截取目标 UI 元素的截图保存为模板，用 OpenCV 在窗口截图中匹配定位。

```bash
# click_at_template — 给截图模板，返回中心坐标并点击
click_at_template() {
  local template=$1 window=$2

  python3 -c "
import cv2, numpy as np, sys, json

shot = cv2.imread('/tmp/shot.png')
template = cv2.imread('$template')
h, w = template.shape[:2]
res = cv2.matchTemplate(shot, template, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(res)

if max_val < 0.7:
    print(f'置信度过低: {max_val:.2f}', file=sys.stderr)
    sys.exit(2)

cx, cy = max_loc[0] + w//2, max_loc[1] + h//2
print(f'{cx} {cy}')
" 2>/dev/null || return 1

  read cx cy
  xdotool mousemove --window "$window" "$cx" "$cy" click 1
}
```

使用示例：

```bash
# 1. 截图保存为模板（只需做一次）
import -window $WID /tmp/shot.png
# 用图片编辑工具从截图中裁剪 tab 按钮区域，保存为 tab_kaifa.png

# 2. 自动化流程
import -window $WID /tmp/shot.png
click_at_template "assets/tab_kaifa.png" $WID
sleep 1

# 3. 验证
import -window $WID /tmp/shot2.png
tesseract /tmp/shot2.png stdout -l chi_sim 2>/dev/null | grep "研发" \
  && echo "✅ 导航成功" || echo "❌ 导航失败"
```

#### 备选：OCR bounding box（无模板时快速定位）

```bash
import -window $WID /tmp/shot.png
tesseract /tmp/shot.png /tmp/shot -l chi_sim --psm 6 tsv
awk -F'\t' '$1==5 && $11!="-1" {printf "%s  center=(%d,%d)\n", $12, $7+$9/2, $8+$10/2}' /tmp/shot.tsv

xdotool mousemove --window $WID 384 675 click 1
```

#### 像素颜色探测（无 OCR 无模板时应急用）

```bash
for y in $(seq 700 10 819); do
  c=$(convert /tmp/shot.png -crop 1x1+666+$y -format "%[hex:p{0,0}]" info:)
  echo "y=$y color=#$c"
done
NAV_Y=<探测到的 Y 中心>
xdotool mousemove --window $WID $((W/2)) $NAV_Y click 1
```

#### 验证点击（三种定位方式通用）

```bash
import -window $WID /tmp/before.png
tesseract /tmp/before.png /tmp/before -l chi_sim --psm 6

xdotool mousemove --window $WID $X $Y click 1
sleep 1

import -window $WID /tmp/after.png
tesseract /tmp/after.png /tmp/after -l chi_sim --psm 6

diff /tmp/before.txt /tmp/after.txt && echo "页面未变化" || echo "✅ 页面已切换"
```

#### 三种定位方式对比

| 方式 | 速度 | 抗 UI 变动 | 维护成本 |
|------|------|-----------|---------|
| OCR bounding box | 慢 | 文字不变即可 | 中 |
| 像素颜色探测 | 快 | ❌ 颜色一变就崩 | 高 |
| **OpenCV 模板匹配** | **快** | **相似度容忍微调** | **低** |

### 已知限制

- `xdotool` 使用**窗口相对坐标**（`--window` 参数），需精确计算 UI 元素位置
- 窗口管理器装饰（标题栏、边框）会影响坐标计算，需通过 `wmctrl -lG` 获取准确几何
- tesseract 中文字 OCR 在复杂背景或小字号时准确率下降
- Flutter 应用可能不响应模拟的鼠标/键盘事件（取决于 build 类型）

- 3 个专业：大数据微专业、AI应用开发、UI/UX设计
- 4 个班级：浙理班级（active, 45人）、杭电班级（preparing, 32人）、线上周末班（active, 78人）、暑期集训营（preparing, 24人）
- 1 个课时示例：「开发环境搭建」，含 3 个场景（Zed 安装、DeepSeek 密钥、Zed Agent 配置）
