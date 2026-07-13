# quanttide-laboratory-of-course-development

课程开发实验室。本地启动和模拟验证 provider/studio 的入口。

## 目录结构

```
bin/                          ← 编译产物（gitignored）
├── qtcloud-course-provider     provider 二进制
└── studio/                     studio bundle（Flutter）

src/
├── provider.sh                ← 启动 provider（仅启动，不模拟）
├── studio.sh                  ← 启动 studio（仅启动，不模拟）
├── provider_sim/main.go       ← 模拟用户访问 provider API（CRUD 全流程）
├── studio_sim/main.go         ← 模拟用户使用 studio（运行测试 + 验证产物）
└── go.mod
```

## 编译

```bash
# 编译 provider
cd apps/qtcloud-course/src/provider
go build -o ../../../examples/default/bin/qtcloud-course-provider ./cmd/server

# 编译 studio
cd apps/qtcloud-course/src/studio
flutter build linux --release
rm -rf ../../../examples/default/bin/studio
cp -r build/linux/x64/release/bundle ../../../examples/default/bin/studio
```

## 运行模拟

```bash
# 模拟用户访问 provider API
cd examples/default/src
go run ./provider_sim/

# 模拟用户使用 studio（运行测试 + 验证产物）
cd examples/default/src
go run ./studio_sim/
```

## 仅启动（不模拟操作）

```bash
./examples/default/src/provider.sh
./examples/default/src/studio.sh
```
