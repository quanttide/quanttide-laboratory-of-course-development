#!/usr/bin/env bash
# 实验：用 LLM 生成课程蓝图，人类打分
# 用法：./run.sh <topic> [prompt_file]
set -euo pipefail

TOPIC="${1:?请指定主题，例如：git}"
PROMPT_FILE="${2:-prompt.md}"
OUTPUT_DIR="results/$(date +%Y%m%d-%H%M)-${TOPIC}"

mkdir -p "$OUTPUT_DIR"

if [ ! -f "$PROMPT_FILE" ]; then
  echo "错误：找不到 prompt 文件 $PROMPT_FILE"
  echo "请先创建 prompt.md，或在运行时指定 prompt 文件路径"
  exit 1
fi

echo "=== 实验：LLM 生成课程蓝图 ==="
echo "主题：$TOPIC"
echo "Prompt 文件：$PROMPT_FILE"
echo "输出目录：$OUTPUT_DIR"
echo ""

# 读取 prompt 并替换 {topic} 占位符
sed "s/{topic}/$TOPIC/g" "$PROMPT_FILE" > "$OUTPUT_DIR/prompt.md"

echo "Prompt 已准备：$OUTPUT_DIR/prompt.md"
echo ""
echo "下一步："
echo "  1. 将 $OUTPUT_DIR/prompt.md 发给 LLM"
echo "  2. LLM 输出保存到 $OUTPUT_DIR/response.md"
echo "  3. 按评分表打分，结果保存到 $OUTPUT_DIR/score.md"
echo ""
echo "评分表模板见 experiments/llm-blueprint/README.md"
