# qtcloud-course-provider

Go HTTP API server，提供课程领域资源的 CRUD 接口。

## 运行方式

```bash
export LISTEN_ADDR=:8080        # 监听地址（默认 :8080）
export VIDEO_DIR=./data/video   # 视频文件目录
./bin/qtcloud-course-provider
```

## 领域模型

| 实体 | 说明 | 关键字段 |
|------|------|----------|
| Program | 专业（培养方案） | id, name, description, status |
| Course | 课程 | id, name, description, status |
| Phase | 阶段（课程下的子阶段） | id, name, sortOrder, courseId |
| Lesson | 课时 | id, title, duration, status |
| Scene | 场景（课时内的教学步骤） | id, name, title, lessonId, steps[], choices[], verifyTip, videoUrl |
| Class | 班级（教学班） | id, name, refName, refType, refId, status, startDate, endDate, studentCount, progress |
| Choice | 场景跳转选项 | label, targetSceneId |

## API 端点

### 健康检查

```
GET /healthz
```

### Program

```
GET    /programs          # 列表
POST   /programs          # 创建
GET    /programs/{id}     # 查询
PUT    /programs/{id}     # 更新
DELETE /programs/{id}     # 删除
```

### Course

```
GET    /courses           # 列表
POST   /courses           # 创建
GET    /courses/{id}      # 查询
PUT    /courses/{id}      # 更新
DELETE /courses/{id}      # 删除
```

### Phase

```
GET    /phases            # 列表（支持 ?courseId= 过滤）
POST   /phases            # 创建
GET    /phases/{id}       # 查询
PUT    /phases/{id}       # 更新
DELETE /phases/{id}       # 删除
```

### Lesson

```
GET    /lessons           # 列表（支持 ?phaseId= 过滤）
POST   /lessons           # 创建
GET    /lessons/{id}      # 查询
PUT    /lessons/{id}      # 更新
DELETE /lessons/{id}      # 删除
```

### Scene

```
GET    /scenes            # 列表（支持 ?lessonId= 过滤）
POST   /scenes            # 创建
GET    /scenes/{id}       # 查询
PUT    /scenes/{id}       # 更新
DELETE /scenes/{id}       # 删除
```

### Class

```
GET    /classes           # 列表
POST   /classes           # 创建
GET    /classes/{id}      # 查询
PUT    /classes/{id}      # 更新
DELETE /classes/{id}      # 删除
```

### 视频

```
GET /video/{path}          # 静态视频文件服务
```

## 内部包

| 包 | 说明 |
|----|------|
| `cmd/server` | 入口，启动 HTTP 服务器 |
| `internal/domain` | 领域模型定义 |
| `internal/store` | 内存存储（map-based） |
| `internal/handler` | HTTP handler 及路由注册 |
