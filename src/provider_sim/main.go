// provider_sim — 模拟用户访问 provider API 服务
//
// 启动 provider 后模拟完整 CRUD 工作流：
// 创建 Program → Course → Phase → Lesson → Scene → 查询 → 更新 → 删除
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

var base string

func findRoot() string {
	dir, _ := os.Getwd()
	for i := 0; i < 10; i++ {
		if _, err := os.Stat(filepath.Join(dir, ".gitmodules")); err == nil {
			return dir
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			break
		}
		dir = parent
	}
	return dir
}

func main() {
	root := findRoot()
	bin := filepath.Join(root, "examples", "default", "bin", "qtcloud-course-provider")

	if _, err := os.Stat(bin); os.IsNotExist(err) {
		fmt.Fprintln(os.Stderr, "错误: 未找到 provider 二进制。请先编译:")
		fmt.Fprintf(os.Stderr, "  cd apps/qtcloud-course && go build -o %s ./src/provider/cmd/server\n", bin)
		os.Exit(1)
	}

	// 启动 provider 子进程
	cmd := exec.Command(bin)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Env = append(os.Environ(), "LISTEN_ADDR=:18080")
	if err := cmd.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "启动 provider 失败: %v\n", err)
		os.Exit(1)
	}
	defer cmd.Process.Kill()

	base = "http://localhost:18080"
	client := &http.Client{Timeout: 5 * time.Second}

	// 等待服务就绪
	for i := 0; i < 20; i++ {
		resp, err := client.Get(base + "/healthz")
		if err == nil && resp.StatusCode == 200 {
			resp.Body.Close()
			break
		}
		time.Sleep(200 * time.Millisecond)
	}

	fmt.Println("=== 模拟用户: 访问 provider API ===")

	// 1. 创建 Program
	programID := mustPost(client, "/programs", map[string]any{
		"id": "test-prog-1", "name": "测试专业", "description": "模拟测试", "status": "draft",
	})
	fmt.Printf("✓ 创建 Program: %s\n", programID)

	// 2. 创建 Course
	courseID := mustPost(client, "/courses", map[string]any{
		"id": "test-course-1", "name": "测试课程", "description": "模拟课程", "status": "draft",
	})
	fmt.Printf("✓ 创建 Course: %s\n", courseID)

	// 3. 创建 Phase
	phaseID := mustPost(client, "/phases", map[string]any{
		"id": "test-phase-1", "name": "基础阶段", "sortOrder": 1, "courseId": courseID,
	})
	fmt.Printf("✓ 创建 Phase: %s\n", phaseID)

	// 4. 创建 Lesson
	lessonID := mustPost(client, "/lessons", map[string]any{
		"id": "test-lesson-1", "title": "概述", "duration": 30, "status": "draft",
	})
	fmt.Printf("✓ 创建 Lesson: %s\n", lessonID)

	// 5. 创建 Scene
	sceneID := mustPost(client, "/scenes", map[string]any{
		"id": "test-scene-1", "name": "intro", "title": "入门", "lessonId": lessonID,
		"steps": []map[string]any{
			{"order": 1, "content": "第一步"},
			{"order": 2, "content": "第二步"},
		},
		"verifyTip": "验证提示",
	})
	fmt.Printf("✓ 创建 Scene: %s\n", sceneID)

	// 6. 查询列表
	mustGet(client, "/programs")
	mustGet(client, fmt.Sprintf("/scenes?lessonId=%s", lessonID))
	fmt.Println("✓ 查询列表")

	// 7. 更新资源
	mustPut(client, fmt.Sprintf("/programs/%s", programID), map[string]any{"name": "更新后的专业"})
	mustPut(client, fmt.Sprintf("/scenes/%s", sceneID), map[string]any{"title": "更新后的场景"})
	fmt.Println("✓ 更新资源")

	// 8. 按 ID 查询
	mustGet(client, fmt.Sprintf("/programs/%s", programID))
	mustGet(client, fmt.Sprintf("/scenes/%s", sceneID))
	fmt.Println("✓ 按 ID 查询")

	// 9. 健康检查
	mustGet(client, "/healthz")
	fmt.Println("✓ 健康检查")

	// 10. 清理删除
	mustDelete(client, fmt.Sprintf("/scenes/%s", sceneID))
	mustDelete(client, fmt.Sprintf("/lessons/%s", lessonID))
	mustDelete(client, fmt.Sprintf("/phases/%s", phaseID))
	mustDelete(client, fmt.Sprintf("/courses/%s", courseID))
	mustDelete(client, fmt.Sprintf("/programs/%s", programID))
	fmt.Println("✓ 清理删除")

	fmt.Println("\n=== 模拟完成: 所有 API 操作通过 ===")
}

func mustPost(c *http.Client, path string, body any) string {
	b, _ := json.Marshal(body)
	resp, err := c.Post(base+path, "application/json", bytes.NewReader(b))
	if err != nil {
		fmt.Fprintf(os.Stderr, "POST %s 失败: %v\n", path, err)
		os.Exit(1)
	}
	defer resp.Body.Close()
	if resp.StatusCode >= 400 {
		b, _ := io.ReadAll(resp.Body)
		fmt.Fprintf(os.Stderr, "POST %s 返回 %d: %s\n", path, resp.StatusCode, string(b))
		os.Exit(1)
	}
	var result map[string]any
	json.NewDecoder(resp.Body).Decode(&result)
	id, _ := result["id"].(string)
	return id
}

func mustGet(c *http.Client, path string) {
	resp, err := c.Get(base + path)
	if err != nil {
		fmt.Fprintf(os.Stderr, "GET %s 失败: %v\n", path, err)
		os.Exit(1)
	}
	defer resp.Body.Close()
	if resp.StatusCode >= 400 {
		b, _ := io.ReadAll(resp.Body)
		fmt.Fprintf(os.Stderr, "GET %s 返回 %d: %s\n", path, resp.StatusCode, string(b))
		os.Exit(1)
	}
}

func mustPut(c *http.Client, path string, body any) {
	b, _ := json.Marshal(body)
	req, _ := http.NewRequest("PUT", base+path, bytes.NewReader(b))
	req.Header.Set("Content-Type", "application/json")
	resp, err := c.Do(req)
	if err != nil {
		fmt.Fprintf(os.Stderr, "PUT %s 失败: %v\n", path, err)
		os.Exit(1)
	}
	defer resp.Body.Close()
	if resp.StatusCode >= 400 {
		b, _ := io.ReadAll(resp.Body)
		fmt.Fprintf(os.Stderr, "PUT %s 返回 %d: %s\n", path, resp.StatusCode, string(b))
		os.Exit(1)
	}
}

func mustDelete(c *http.Client, path string) {
	req, _ := http.NewRequest("DELETE", base+path, nil)
	resp, err := c.Do(req)
	if err != nil {
		fmt.Fprintf(os.Stderr, "DELETE %s 失败: %v\n", path, err)
		os.Exit(1)
	}
	resp.Body.Close()
	if resp.StatusCode >= 400 {
		fmt.Fprintf(os.Stderr, "DELETE %s 返回 %d\n", path, resp.StatusCode)
		os.Exit(1)
	}
}
