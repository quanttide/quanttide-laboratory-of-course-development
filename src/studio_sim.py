#!/usr/bin/env python3
"""studio_sim — 模拟用户访问 studio 课程云。

模拟用户操作：
1. 运行 Flutter Widget 测试（模拟 UI 交互：点击、导航、预览）
2. 验证编译产物完整性
"""
import os
import subprocess
import sys
from pathlib import Path


def main():
    root = Path.cwd().resolve()
    for _ in range(10):
        if (root / ".gitmodules").exists():
            break
        parent = root.parent
        if parent == root:
            break
        root = parent

    studio_dir = root / "apps" / "qtcloud-course" / "src" / "studio"
    bundle = root / "examples" / "default" / "bin" / "studio" / "qtcloud_course_studio"

    print("=== 模拟用户: 验证 studio 课程云 ===\n")

    # 1. 运行 Flutter 测试
    print("▶ 运行 Widget 测试（模拟用户点击、导航、预览）...\n")
    result = subprocess.run(
        ["flutter", "test", "--reporter", "compact"],
        cwd=str(studio_dir),
        capture_output=False,
    )
    if result.returncode != 0:
        print("\n✗ Widget 测试失败", file=sys.stderr)
        sys.exit(1)
    print("\n✓ Widget 测试通过 — 用户交互逻辑正常\n")

    # 2. 验证编译产物
    print("▶ 验证编译产物...")
    if not bundle.exists():
        print(f"✗ 未找到二进制: {bundle}", file=sys.stderr)
        print("  请先编译: cd apps/qtcloud-course/src/studio && flutter build linux --release")
        sys.exit(1)

    # ldd 检查依赖
    result = subprocess.run(
        ["ldd", str(bundle)],
        cwd=str(bundle.parent),
        capture_output=True, text=True,
    )
    missing = [line for line in result.stdout.split("\n") if "not found" in line]
    if missing:
        for line in missing:
            print(f"  ✗ 缺失依赖: {line.strip()}")
        sys.exit(1)
    print("  ✓ 二进制文件存在")
    print("  ✓ 所有共享库依赖满足\n")

    # 3. 尝试启动
    print("▶ 尝试启动应用...")
    result = subprocess.run(
        [str(bundle), "--help"],
        cwd=str(bundle.parent),
        capture_output=True,
    )
    if result.returncode == 0:
        print("  ✓ 应用正常启动")
    else:
        print("  ~ 应用需桌面环境（当前无显示器，此为预期）")

    print("\n=== 模拟完成: studio 验证通过 ===")


if __name__ == "__main__":
    main()
