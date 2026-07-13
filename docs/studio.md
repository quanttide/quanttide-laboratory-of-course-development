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

## 示例数据

- 3 个专业：大数据微专业、AI应用开发、UI/UX设计
- 4 个班级：浙理班级（active, 45人）、杭电班级（preparing, 32人）、线上周末班（active, 78人）、暑期集训营（preparing, 24人）
- 1 个课时示例：「开发环境搭建」，含 3 个场景（Zed 安装、DeepSeek 密钥、Zed Agent 配置）
