# AGENTS.md — 给 AI Agent 的实验室指南

---

## 🧪 产品实验室

> 定位：产品实验沙盒。画原型、写小网站、试任何东西。零工程规范，自由折腾。
> GitHub Pages 已开启，推上去就能在线看效果。

### 核心规矩

1. **一个实验一个目录** — 自包含，删目录 = 删实验（如 `innovation-prototype/`）
2. **每个实验至少一个 README.md** — 说清三件事：这是什么 / 怎么访问 / 当前状态
3. **原型即部署** — HTML 放目录里，GitHub Pages 路径即 URL，无需额外配置
4. **状态要标记** — 用 `[进行中]` `[已完成]` `[废弃]` 标签，别堆死代码
5. **INDEX.md 是唯一总索引** — 根目录一个文件记录所有实验，不搞复杂目录
6. **别过度工程化** — 不建深层嵌套目录、不写没人看的文档、原型先跑起来再说
7. **💰 省 token** — 小亦每月 100 预算，文档写简洁，实验代码优先复用

### 预算红线

- 月预算：**100 元**（Claude Code token 消耗）
- 原则：先想清楚再动手，能复用不复写，文档够用就行不写论文

---

## 📦 历史档案：provider/studio 模拟（果哥遗留）

以下是原仓库的 provider/studio 二进制模拟说明，保留作为参考。

### 项目概况

本仓库是 quanttide-course 课程领域实验示例，位于 `examples/default/`。两个核心组件以编译产物的形式存在于 `bin/` 中。

### 关键路径

| 路径 | 说明 |
|------|------|
| `bin/qtcloud-course-provider` | Go HTTP API 服务，端口由 `LISTEN_ADDR` 环境变量控制 |
| `bin/studio/` | Flutter 桌面应用 bundle |
| `src/provider_sim.py` | 模拟用户访问 provider API 的完整 CRUD 流程 |
| `src/studio_sim.py` | 模拟用户启动 studio 并验证运行正常 |
| `docs/` | 从二进制分析提取的功能文档 |

### 开发注意事项

1. **docs/ 中的文档从编译产物中逆向提取**，只能反映已有的功能，不能反映源码中尚未编译的新功能。
2. `docs/provider.md` 包含完整的 REST API 端点列表和领域模型。新增 API 端点后需要同步更新文档。
3. `docs/studio.md` 基于 Flutter asset 中的示例数据推断功能。新增页面或数据后需要同步更新文档。
4. provider 使用内存存储（`internal/store` 包），重启后数据丢失。
5. `src/provider_sim.py` 模拟了完整的 CRUD 生命周期，新增实体或端点时应更新模拟脚本作为集成测试。
6. `src/studio_sim.py` 仅检测应用是否能正常启动 3 秒，未覆盖 UI 交互测试。
