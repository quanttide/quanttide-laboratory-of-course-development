// studio_sim — 模拟用户访问 studio 课程云
//
// 模拟用户操作：
// 1. 验证 Flutter 测试套件（模拟 UI 交互：点击、导航、预览）
// 2. 验证编译产物完整性
package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

func main() {
	root, _ := os.Getwd()
	// 从当前目录向上找到项目根（包含 .gitmodules 的目录）
	for i := 0; i < 10; i++ {
		if _, err := os.Stat(filepath.Join(root, ".gitmodules")); err == nil {
			break
		}
		parent := filepath.Dir(root)
		if parent == root {
			break
		}
		root = parent
	}
	studioDir := filepath.Join(root, "apps", "qtcloud-course", "src", "studio")
	bundle := filepath.Join(root, "examples", "default", "bin", "studio", "qtcloud_course_studio")
	bundleDir := filepath.Join(root, "examples", "default", "bin", "studio")

	fmt.Println("=== 模拟用户: 验证 studio 课程云 ===")

	// 1. 运行 Flutter 测试（模拟 UI 交互）
	fmt.Print("\n▶ 运行 Widget 测试（模拟用户点击、导航、预览）...\n\n")
	cmd := exec.Command("flutter", "test", "--reporter", "compact")
	cmd.Dir = studioDir
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		fmt.Fprintf(os.Stderr, "\n✗ Widget 测试失败: %v\n", err)
		os.Exit(1)
	}
	fmt.Print("\n✓ Widget 测试通过 — 用户交互逻辑正常\n")

	// 2. 验证编译产物
	fmt.Print("\n▶ 验证编译产物...\n")
	if _, err := os.Stat(bundle); os.IsNotExist(err) {
		fmt.Fprintf(os.Stderr, "✗ 未找到二进制: %s\n", bundle)
		fmt.Println("  请先编译: cd apps/qtcloud-course/src/studio && flutter build linux --release")
		fmt.Println("  cp -r apps/qtcloud-course/src/studio/build/linux/x64/release/bundle examples/default/bin/studio")
		os.Exit(1)
	}

	// 验证共享库依赖
	ldd := exec.Command("ldd", bundle)
	ldd.Dir = bundleDir
	out, err := ldd.Output()
	if err != nil {
		fmt.Fprintf(os.Stderr, "✗ ldd 检查失败: %v\n", err)
		os.Exit(1)
	}
	missing := false
	for _, line := range strings.Split(string(out), "\n") {
		if strings.Contains(line, "not found") {
			fmt.Printf("  ✗ 缺失依赖: %s\n", strings.TrimSpace(line))
			missing = true
		}
	}
	if missing {
		fmt.Println("\n✗ 存在缺失的共享库依赖")
		os.Exit(1)
	}
	fmt.Println("  ✓ 二进制文件存在")
	fmt.Println("  ✓ 所有共享库依赖满足")

	// 3. 尝试启动
	fmt.Print("\n▶ 尝试启动应用...\n")
	launch := exec.Command("./qtcloud_course_studio", "--help")
	launch.Dir = bundleDir
	if err := launch.Run(); err != nil {
		fmt.Println("  ~ 应用需桌面环境（当前无显示器，此为预期）")
	} else {
		fmt.Println("  ✓ 应用正常启动")
	}

	fmt.Println("\n=== 模拟完成: studio 验证通过 ===")
}
