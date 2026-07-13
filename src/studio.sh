#!/usr/bin/env bash
# 启动 studio 课程云 — 模拟用户访问
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUNDLE="$ROOT/bin/studio"
BIN="$BUNDLE/qtcloud_course_studio"

if [ ! -x "$BIN" ]; then
  echo "错误: 未找到 studio 二进制，请先编译"
  echo "  cd apps/qtcloud-course/src/studio && flutter build linux --release"
  echo "  cp -r apps/qtcloud-course/src/studio/build/linux/x64/release/bundle $BUNDLE"
  exit 1
fi

echo "==> 启动 studio 课程云"
echo "    地址:  本地桌面应用"
echo "    数据:  内嵌 assets（本地 JSON）"
echo ""

cd "$BUNDLE" && exec ./qtcloud_course_studio
