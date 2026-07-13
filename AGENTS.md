# AGENTS.md — 给 AI Agent 的开发指南

## 项目概况

本仓库是 quanttide-course 课程领域实验示例，位于 `examples/default/`。两个核心组件以编译产物的形式存在于 `bin/` 中。

## 关键路径

| 路径 | 说明 |
|------|------|
| `bin/qtcloud-course-provider` | Go HTTP API 服务，端口由 `LISTEN_ADDR` 环境变量控制 |
| `bin/studio/` | Flutter 桌面应用 bundle |
| `src/provider_sim.py` | 模拟用户访问 provider API 的完整 CRUD 流程 |
| `src/studio_sim.py` | 模拟用户启动 studio 并验证运行正常 |
| `docs/` | 从二进制分析提取的功能文档 |

## 开发注意事项

1. **docs/ 中的文档从编译产物中逆向提取**，只能反映已有的功能，不能反映源码中尚未编译的新功能。
2. `docs/provider.md` 包含完整的 REST API 端点列表和领域模型。新增 API 端点后需要同步更新文档。
3. `docs/studio.md` 基于 Flutter asset 中的示例数据推断功能。新增页面或数据后需要同步更新文档。
4. provider 使用内存存储（`internal/store` 包），重启后数据丢失。
5. `src/provider_sim.py` 模拟了完整的 CRUD 生命周期，新增实体或端点时应更新模拟脚本作为集成测试。
6. `src/studio_sim.py` 仅检测应用是否能正常启动 3 秒，未覆盖 UI 交互测试。
