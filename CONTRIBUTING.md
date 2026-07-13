# Contributing — 实验规范

## 目录约定

```
lab/                       # 实验现场
├── bin/                   # 编译产物（gitignore）
├── videos/                # 视频数据（gitignore）
├── deploy.sh              # 跟踪：一键部署脚本
├── seed-demo.sh           # 跟踪：数据填充脚本
└── video-test.html        # 跟踪：播放测试页
```

## 规则

1. **所有操作在 `lab/` 内完成** — 不涉及系统目录（如 `~/course-lab/`），不污染仓库其他位置
2. **脚本和配置文件可跟踪** — `.sh`、`.html` 等代码文件正常进版本控制
3. **构建产物和视频数据必须过滤** — 二进制放在 `lab/bin/`，视频放在 `lab/videos/`，已加入 `.gitignore`
4. **视频自包含** — 实验所需的视频通过 `ffmpeg` 自动生成，不依赖外部视频文件

## 快速开始

```bash
bash lab/deploy.sh         # 构建、部署、启动服务
bash lab/seed-demo.sh      # 创建演示数据
```

详情见 [`ROADMAP.md`](ROADMAP.md)。
