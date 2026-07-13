# quanttide-laboratory-of-course-development

课程开发实验室。本地启动 provider 和 studio 的入口。

## 启动

```bash
# 启动 provider API 服务（:8080）
./src/provider.sh

# 启动 studio 桌面应用
./src/studio.sh
```

## 前置条件

- provider: 需要先编译 Go 二进制 `go build -o bin/qtcloud-course-provider ./apps/qtcloud-course/src/provider/cmd/server`
- studio: 需要先编译 Flutter 二进制 `flutter build linux --release` 并复制 bundle 到 `bin/studio/`
