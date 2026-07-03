# quanttide-laboratory-of-course-development

课程开发实验室——用 LLM 生成课程蓝图，人类打分。

## 用法

```bash
cargo run <topic>
```

例如：

```bash
cargo run docker
```

流程：
1. 读取 `prompt.md`，替换 `{topic}` 占位符
2. 调用 DeepSeek（通过 `quanttide-agent` Rust 库）
3. 输出保存到 `results/<timestamp>-<topic>/response.md`
4. 创建评分表 `score.md`，由人类讲师打分

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `LLM_API_KEY` | DeepSeek API 密钥 | 必填 |
| `LLM_MODEL` | 模型名 | `deepseek-v4-flash` |
| `LLM_BASE_URL` | API 地址 | `https://api.deepseek.com` |
