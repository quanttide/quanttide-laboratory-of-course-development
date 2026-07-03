use std::fs;
use std::path::PathBuf;

use anyhow::Result;
use chrono::Local;
use clap::Parser;
use quanttide_agent::{llm::CompleteOptions, Message, Settings, LLM};

#[derive(Parser)]
#[command(name = "lab", about = "实验：用 LLM 生成课程蓝图")]
struct Args {
    /// 主题，例如 git、docker
    topic: String,

    /// prompt 模板文件路径（默认与二进制同目录下的 prompt.md）
    #[arg(short, long, default_value = "prompt.md")]
    prompt: PathBuf,
}

fn main() -> Result<()> {
    let args = Args::parse();

    let settings = Settings::from_env();
    let prompt_file = &args.prompt;

    if !prompt_file.exists() {
        anyhow::bail!("找不到 prompt 文件：{}", prompt_file.display());
    }

    // 准备输出目录
    let timestamp = Local::now().format("%Y%m%d-%H%M");
    let output_dir = PathBuf::from("results").join(format!("{}-{}", timestamp, args.topic));
    fs::create_dir_all(&output_dir)?;

    // 读取 prompt 并替换占位符
    let prompt_text = fs::read_to_string(prompt_file)?.replace("{topic}", &args.topic);
    fs::write(output_dir.join("prompt.md"), &prompt_text)?;
    println!("Prompt 已准备：{}", output_dir.join("prompt.md").display());

    // 调用 LLM
    println!("正在调用 DeepSeek（主题：{}）...", args.topic);
    let llm = LLM::new(
        &settings.llm_model,
        &settings.llm_base_url,
        &settings.llm_api_key,
    );
    let messages = vec![Message::new("user", &prompt_text)];
    let options = CompleteOptions::default();
    let resp = llm.complete(&messages, options)?;

    fs::write(output_dir.join("response.md"), &resp.content)?;
    println!(
        "LLM 回复已保存：{}",
        output_dir.join("response.md").display()
    );

    // 创建评分表
    let score = format!(
        "# 评分：实验 - {}\n\
         \n\
         **LLM**：{}\n\
         **日期**：{}\n\
         **评分人**：（待填写）\n\
         \n\
         | 维度 | 分数（1-5） | 评语 |\n\
         |------|------------|------|\n\
         | 溯源深度 | /5 | |\n\
         | 概念对比 | /5 | |\n\
         | 逻辑链条 | /5 | |\n\
         | 教学可操作性 | /5 | |\n\
         | 风格契合度 | /5 | |\n\
         \n\
         **总分**：/25\n\
         \n\
         **总体评价**：\n",
        args.topic,
        resp.model,
        Local::now().format("%Y-%m-%d")
    );
    fs::write(output_dir.join("score.md"), &score)?;
    println!("评分表已创建：{}", output_dir.join("score.md").display());

    println!("完成。请填写评分表后提交。");
    Ok(())
}
