# quanttide-laboratory-of-course-development

课程开发实验室。模拟用户访问 provider/studio 的入口。

## 目录结构

```
bin/                          ← 编译产物（gitignored）
├── qtcloud-course-provider     provider 二进制
└── studio/                     studio bundle（Flutter）

src/
├── provider_sim.py           ← 模拟用户访问 provider API（CRUD 全流程）
├── studio_sim.py             ← 模拟用户使用 studio（运行测试 + 验证产物）
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
python examples/default/src/provider_sim.py

# 模拟用户使用 studio（运行测试 + 验证产物）
python examples/default/src/studio_sim.py
```
