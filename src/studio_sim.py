#!/usr/bin/env python3
"""studio_sim — 模拟用户启动 studio 课程云。

启动编译后的 studio 二进制，验证它能正常打开并保持运行。
"""
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


def find_root() -> Path:
    p = Path.cwd().resolve()
    for _ in range(10):
        if (p / ".gitmodules").exists():
            return p
        parent = p.parent
        if parent == p:
            break
        p = parent
    return p


def main():
    root = find_root()
    bundle = root / "examples" / "default" / "bin" / "studio"
    binary = bundle / "qtcloud_course_studio"

    print("=== 模拟用户: 启动 studio 课程云 ===\n")

    if not binary.exists():
        print(f"✗ 未找到二进制: {binary}", file=sys.stderr)
        print("  请先编译:", file=sys.stderr)
        print("  cd apps/qtcloud-course/src/studio && flutter build linux --release", file=sys.stderr)
        sys.exit(1)

    print(f"▶ 启动 {binary} ...")
    print(f"    目录: {bundle}\n")

    # 检测 xvfb-run（无头环境下的虚拟显示器）
    launch_cmd = [str(binary)]
    xvfb = subprocess.run(["which", "xvfb-run"], capture_output=True, text=True)
    if xvfb.returncode == 0:
        launch_cmd = ["xvfb-run", "-a"] + launch_cmd
        print("  ~ 使用 xvfb-run 虚拟显示器\n")

    proc = subprocess.Popen(
        launch_cmd,
        cwd=str(bundle),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # 等待 3 秒看是否稳定运行
    time.sleep(3)
    poll = proc.poll()

    if poll is None:
        # 仍在运行 → 成功
        print("  ✓ 应用启动成功，运行正常")
        proc.send_signal(signal.SIGTERM)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
        print("\n=== 模拟完成: studio 验证通过 ===")
    elif poll == 0:
        print("\n✓ 应用正常退出")
        print("=== 模拟完成 ===")
    else:
        # 异常退出，输出错误信息
        out, err = proc.communicate()
        if out:
            print(out.decode(), file=sys.stdout)
        if err:
            print(err.decode(), file=sys.stderr)
        print(f"\n✗ 应用启动后异常退出 (exit code {poll})", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
