#!/usr/bin/env python3
"""provider_sim — 模拟用户访问 provider API 服务。

启动 provider 后模拟完整 CRUD 工作流：
创建 Program → Course → Phase → Lesson → Scene → 查询 → 更新 → 删除
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def find_root() -> Path:
    """从当前目录向上找到项目根（包含 .gitmodules 的目录）。"""
    p = Path.cwd().resolve()
    for _ in range(10):
        if (p / ".gitmodules").exists():
            return p
        parent = p.parent
        if parent == p:
            break
        p = parent
    return p


def request(method: str, url: str, body: dict | None = None) -> dict | None:
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            text = resp.read().decode()
            return json.loads(text) if text else None
    except urllib.error.HTTPError as e:
        sys.exit(f"✗ {method} {url} 返回 {e.code}: {e.read().decode()}")


def main():
    root = find_root()
    server_bin = root / "examples" / "default" / "bin" / "qtcloud-course-provider"

    if not server_bin.exists():
        print("错误: 未找到 provider 二进制。请先编译:", file=sys.stderr)
        print(f"  cd apps/qtcloud-course && go build -o {server_bin} ./src/provider/cmd/server", file=sys.stderr)
        sys.exit(1)

    # 启动 provider
    proc = subprocess.Popen(
        [str(server_bin)],
        env={**os.environ, "LISTEN_ADDR": ":18080"},
    )
    try:
        base = "http://localhost:18080"

        # 等待服务就绪
        for _ in range(20):
            try:
                request("GET", f"{base}/healthz")
                break
            except Exception:
                time.sleep(0.2)

        print("=== 模拟用户: 访问 provider API ===")

        # 1-5. 创建资源
        prog_id = request("POST", f"{base}/programs", {
            "id": "test-prog-1", "name": "测试专业", "description": "模拟测试", "status": "draft",
        })["id"]
        print(f"✓ 创建 Program: {prog_id}")

        course_id = request("POST", f"{base}/courses", {
            "id": "test-course-1", "name": "测试课程", "description": "模拟课程", "status": "draft",
        })["id"]
        print(f"✓ 创建 Course: {course_id}")

        phase_id = request("POST", f"{base}/phases", {
            "id": "test-phase-1", "name": "基础阶段", "sortOrder": 1, "courseId": course_id,
        })["id"]
        print(f"✓ 创建 Phase: {phase_id}")

        lesson_id = request("POST", f"{base}/lessons", {
            "id": "test-lesson-1", "title": "概述", "duration": 30, "status": "draft",
        })["id"]
        print(f"✓ 创建 Lesson: {lesson_id}")

        scene_id = request("POST", f"{base}/scenes", {
            "id": "test-scene-1", "name": "intro", "title": "入门", "lessonId": lesson_id,
            "steps": [{"order": 1, "content": "第一步"}, {"order": 2, "content": "第二步"}],
            "verifyTip": "验证提示",
        })["id"]
        print(f"✓ 创建 Scene: {scene_id}")

        # 6-9. 查询、更新、查询、健康检查
        request("GET", f"{base}/programs")
        request("GET", f"{base}/scenes?lessonId={lesson_id}")
        print("✓ 查询列表")

        request("PUT", f"{base}/programs/{prog_id}", {"name": "更新后的专业"})
        request("PUT", f"{base}/scenes/{scene_id}", {"title": "更新后的场景"})
        print("✓ 更新资源")

        request("GET", f"{base}/programs/{prog_id}")
        request("GET", f"{base}/scenes/{scene_id}")
        print("✓ 按 ID 查询")

        request("GET", f"{base}/healthz")
        print("✓ 健康检查")

        # 10. 清理删除
        request("DELETE", f"{base}/scenes/{scene_id}")
        request("DELETE", f"{base}/lessons/{lesson_id}")
        request("DELETE", f"{base}/phases/{phase_id}")
        request("DELETE", f"{base}/courses/{course_id}")
        request("DELETE", f"{base}/programs/{prog_id}")
        print("✓ 清理删除")

        print("\n=== 模拟完成: 所有 API 操作通过 ===")
    finally:
        proc.terminate()
        proc.wait()


if __name__ == "__main__":
    main()
