#!/usr/bin/env bash
# 启动 provider 服务 — 模拟用户访问
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/bin/qtcloud-course-provider"
DATA_DIR="$ROOT/../../data"

if [ ! -x "$BIN" ]; then
  echo "错误: 未找到 provider 二进制文件，请先编译"
  echo "  cd apps/qtcloud-course/src/provider && go build -o $BIN ./cmd/server"
  exit 1
fi

export LISTEN_ADDR="${LISTEN_ADDR:-:8080}"
export VIDEO_DIR="${VIDEO_DIR:-$DATA_DIR/video}"

echo "==> 启动 provider 服务"
echo "    地址:  http://localhost${LISTEN_ADDR}"
echo "    视频:   $VIDEO_DIR"
echo ""
echo "    测试:   curl http://localhost${LISTEN_ADDR}/healthz"
echo "    课堂:   open $ROOT/../classroom.html"
echo ""

exec "$BIN"
