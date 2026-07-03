#!/usr/bin/env python3
"""实验：用 LLM 生成课程蓝图，人类打分。

用法：
    ./run.py <topic> [prompt_file]

默认 prompt 文件为 prompt.md（与本脚本同目录）。
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from quanttide_agent import LLM


def main():
    parser = argparse.ArgumentParser(description="用 LLM 生成课程蓝图")
    parser.add_argument("topic", help="主题，例如 git")
    parser.add_argument(
        "prompt_file",
        nargs="?",
        default=Path(__file__).parent / "prompt.md",
        help="prompt 模板文件（默认同目录下的 prompt.md）",
    )
    args = parser.parse_args()

    topic = args.topic
    prompt_file = Path(args.prompt_file)

    if not prompt_file.exists():
        print(f"错误：找不到 prompt 文件 {prompt_file}", file=sys.stderr)
        sys.exit(1)

    # 准备输出目录
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    output_dir = Path("results") / f"{timestamp}-{topic}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 读取 prompt 并替换占位符
    prompt_text = prompt_file.read_text(encoding="utf-8")
    prompt_text = prompt_text.replace("{topic}", topic)
    (output_dir / "prompt.md").write_text(prompt_text, encoding="utf-8")
    print(f"Prompt 已准备：{output_dir / 'prompt.md'}")

    # 调用 LLM
    print(f"正在调用 DeepSeek（主题：{topic}）...")
    llm = LLM()
    resp = llm.complete(prompt_text)
    (output_dir / "response.md").write_text(resp.content, encoding="utf-8")
    print(f"LLM 回复已保存：{output_dir / 'response.md'}")

    # 创建评分表
    score = output_dir / "score.md"
    score.write_text(
        f"# 评分：实验 - {topic}\n"
        f"\n"
        f"**LLM**：{resp.model}\n"
        f"**日期**：{datetime.now().strftime('%Y-%m-%d')}\n"
        f"**评分人**：（待填写）\n"
        f"\n"
        f"| 维度 | 分数（1-5） | 评语 |\n"
        f"|------|------------|------|\n"
        f"| 溯源深度 | /5 | |\n"
        f"| 概念对比 | /5 | |\n"
        f"| 逻辑链条 | /5 | |\n"
        f"| 教学可操作性 | /5 | |\n"
        f"| 风格契合度 | /5 | |\n"
        f"\n"
        f"**总分**：/25\n"
        f"\n"
        f"**总体评价**：\n",
        encoding="utf-8",
    )
    print(f"评分表已创建：{score}")
    print("完成。请填写评分表后提交。")


if __name__ == "__main__":
    main()
