# 量潮课堂 · 创新系统原型 v0.1 MVP 交接说明

> 交接对象：技术团队 / 后续接手者
> 交接日期：2026-08-15
> 范围：生产实习板块 MVP 闭环（纯前端原型，服务端待技术团队实现）

---

## 0. 一句话

**学员进入「生产实习」→ 看 5 个模块 → 上报进度 → 提交立项（不做审批）→ 后台能看学员 / 进度 / 立项**。当前为纯前端 + localStorage 实现的闭环原型，数据只存在当前浏览器，服务端接口留待技术团队按本说明落地。

## 1. 交付物与位置

| 内容 | 位置 |
|---|---|
| 主原型（唯一需改的文件） | `innovation-prototype/innovation-prototype-latest.html`（约 2400 行，2 个 `<script>` 块） |
| 线上预览 | `https://quanttide.github.io/quanttide-laboratory-of-course-development/innovation-prototype/innovation-prototype-latest.html` |
| 旧版参考（勿改） | `prototype.html`、`prototype-v0.12.html`、`screens/`、`models/course.md`、`创新原型UI设计系统.md` |

## 2. MVP 范围（v0.1）

- 只做一门课：**生产实习**（课程列表步骤 1–4 已锁定为「暂未开放」，仅第 5 步可进入）。
- 生产实习含 5 个模块：m1 认识量潮 → m2 量潮课堂为什么存在 → m3 工作方法论 → m4 量潮正在探索什么 → m5 Sell Your Demo（含立项表单）。
- **班级概念本版不做**（单门课、单学员视角）。
- **本版不提供视频资源**（所有课时均为「阅读 X min」）。
- 提交立项后**不做审批**，状态恒为「已提交」。
- 立项 = 生产实习的核心动作，必须存在。

## 3. 当前实现

### 3.1 学习端（`#view-front`）
- 进入生产实习：`enterCourse('prod')` → 展示 5 模块、顶部进度条、底部 stepbar（认识量潮/理解业务/学会做事/发现机会/Sell Your Demo）。
- 模块内容在页面内展开（`toggleLesson(id)`），无需跳页。
- 切到任一模块 `m1`–`m5` 即触发：
  1. `saveProgress('prod', id)` 记录本地进度（`qt-progress-prod`，结构 `{max, last}`）；
  2. `reportProgress()` **上报进度到后台学员数据**（见 3.3 学员表）。
- m5 内嵌「机会验证」立项表单（5 问 + 方向类型 + 组队），按钮 `submitProposal()`。姓名按组队方式拆分填写：
  - 组队方式选「**个人独立**」→ 只显示「你的姓名」输入框（`pf-ownname`）；
  - 选「已找好搭档 / 希望在组队广场招募」→ 切换为「队长姓名」（`pf-leader`）+「队员姓名」（`pf-member`，多个用顿号分隔），由 `togglePfNameArea()` 控制显示切换。

### 3.2 后台（`#view-back`，切顶栏「创新中台 / 数据看板」）
- **学员管理**：学员 / 当前课程 / 进度(X/5 模块) / 最近活跃 / 立项(✓ 项目名 或 —) / 状态。学员由「上报进度」与「提交立项」自动建档。
- **立项管理**：项目名称 / 学员 / 方向 / 组队 / 核心假设 / 提交时间 / 状态（已提交）/ 操作（删除）。组队提交时「学员」列显示**队长姓名**，队员姓名存在 `teamMember` 字段，后台列表暂不单独展示。
  - 删除 = **软删除**，记录移入历史（`qt-proposals-history`，含删除时间）。
  - 顶部「📜 历史记录」开关展开历史表。
- 其余后台区块（课程管理 / 阶段报告模板 / 双创项目管理）为静态展示，不参与闭环。

### 3.3 数据存储（localStorage，纯本地）

| Key | 内容 | 结构 |
|---|---|---|
| `qt-progress-prod` | 生产实习进度 | `{"max": 1, "last": "m1"}` |
| `qt-students` | 学员档案（进度自动上报+立项自动建档） | `[{name, course:'生产实习', progressMax, progressTotal:5, activeAt, status:'在读'\|'已完成'}]` |
| `qt-proposals` | 立项申请 | `[{id, studentName, projectName, opportunity, fit, hypothesis, demo, directionType, teamMode, teamLeader, teamMember, status:'已提交', submittedAt}]` |
| `qt-proposals-history` | 已删除立项（软删除留痕） | `[{projectName, studentName, submittedAt, directionType, deletedAt}]` |
| `qt-learner` | 当前学员身份（默认「演示学员」，提交立项时改用表单所填姓名；组队时取**队长姓名**） | 字符串 |

- 种子数据：`SEED_STUDENTS` / `SEED_PROPOSALS` 均为空，首次打开是干净空状态。
- 示例数据键均为 `qt-*` 前缀；清空可在控制台 `localStorage.clear()`。

## 4. 关键函数（第二个 `<script>` 块，约 2220 行起）

| 函数 | 作用 |
|---|---|
| `submitProposal()` | 按组队方式取姓名（个人=`pf-ownname`，组队=`pf-leader`）→ 校验姓名/项目名 → 生成记录（含 `teamLeader`/`teamMember`）写入 `qt-proposals` → 同步学员身份 → 建档/更新学员 → 上报进度 → 进度 100% |
| `togglePfNameArea()` | 监听组队方式下拉，切换「个人姓名」与「队长+队员」两个输入区块 |
| `reportProgress()` | 按当前学员把 `qt-progress-prod` 进度 upsert 到 `qt-students` |
| `mergeStudent(rec)` | 按立项姓名（组队时=队长姓名）建档/更新学员（进度取真实上报值） |
| `learnerName()` / `setLearnerName(n)` | 读写当前学员身份，改名时迁移既有学员记录 |
| `deleteProposal(id)` | 软删除：移入历史 + 学员表联动刷新 |
| `getHistory()` / `toggleHistory()` | 历史记录读写 / 展开收起 |
| `loadBackendData()` | 渲染后台学员表 + 立项表 + 历史表（进后台时调用） |
| `saveProgress()` / `getProgress()` | 学习进度读写（第一个 script 块） |

## 5. 闭环流程

```
学员 → 课程列表(仅生产实习可进) → 模块 m1..m5
  ├─ 切模块 → saveProgress + reportProgress → 后台学员表进度实时可见
  └─ m5 提交立项 → qt-proposals + 学员建档 + 进度100%
后台 → 学员管理(学员/进度/立项) + 立项管理(列表/删除/历史)
```

## 6. 技术团队落地清单（服务端）

> 页面结构与数据模型可直接沿用，把 localStorage 读写换成真实 API 即可。

1. **课程与进度**
   - 生产实习 5 模块结构可由前端静态配置迁移到服务端课程表；其余 4 门课按「暂未开放」返回。
   - 进度上报接口：`POST /api/courses/prod/progress`（body：`{moduleId}`），返回 `{max, last}`，对应现 `qt-progress-prod`。
2. **立项（核心）**
   - `POST /api/proposals`：创建立项，字段见 3.3 表；**无审批流**，`status='已提交'`。
   - `GET /api/proposals`：后台列表。
   - `DELETE /api/proposals/:id`：软删除（is_deleted + deleted_at），对应现「删除→历史」。
   - `GET /api/proposals/history`：历史记录。
3. **学员档案**
   - 进度上报与提交立项时自动 upsert 学员（按 `studentName`/`userId`），字段见 3.3。组队时以 `studentName`（队长）建档，`teamMember` 存队员姓名，不单独建档。
4. **身份**
   - 原型用姓名做身份；服务端建议换 `userId`，`qt-learner` 对应登录态。
5. **班级**
   - 本版不做，服务端无需班级表；表结构预留 `class_id` 可空即可。

## 7. 已知限制与取舍

- 数据仅存当前浏览器（多浏览器/换机不互通）——按「原型阶段 localStorage 作数据层」的确认执行，服务端是交付时技术团队的正式实现。
- 单学员视角，无登录/多账号/班级；学员由「上报进度」与「提交立项」自动建档，非预置名单。
- 后台「课程管理 / 阶段报告模板 / 双创项目管理」为静态展示，未接数据。
- `#form-page` 为「立项申请表」独立问卷预览页（静态展示），未参与闭环，可保留或删除。

## 8. 验收步骤

1. 打开原型（本地 file:// 或线上地址）→ 课程列表仅生产实习可进。
2. 依次点击 m1–m5 → 顶部进度条推进 → 切到后台「学员管理」出现「演示学员」且进度与实点同步。
3. 回到 m5 提交立项（**个人**：选「个人独立」填自己的姓名；**组队**：选「已找好搭档」填队长+队员姓名）→ 后台「立项管理」出现记录（状态：已提交，组队时「学员」列=队长）→「学员管理」该学员出现 ✓ 项目名。
4. 组队/个人切换验证：下拉组队方式时姓名输入区随之切换（`togglePfNameArea`）。
5. 立项管理点「删除」→ 记录从当前列表消失 → 点「📜 历史记录」可见该条（含删除时间）。
6. 刷新页面数据不丢（localStorage 持久化）。
