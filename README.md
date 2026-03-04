# 🤖 Language Clone (数字人分身/语言风格克隆)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Model](https://img.shields.io/badge/Model-Qwen2.5--7B-orange)

## 📖 项目简介

**WeClone** 是一个基于大语言模型（LLM）与文本转语音（TTS）技术的综合性数字分身克隆项目。本项目旨在通过个人的历史聊天记录或特定角色的台词数据，微调出高度还原目标人物语言风格和音色的专属 AI。

本项目是一个涵盖数据清洗、模型微调、在线推理与系统评测的全链路工程。目前，项目内已包含针对经典影视角色**李云龙**的成功微调案例。



## ✨ 核心特性

- **💬 多源数据解析**：内置 `wechat_parser` 与 `telegram_parser`，支持一键将微信、Telegram 等聊天导出记录转换为标准训练集。
- **🛡️ 隐私保护 (PII)**：集成了严格的个人敏感信息脱敏模块（`pii_detector`），确保训练数据安全合规。
- **🧠 高效微调训练**：基于 `Unsloth` 和 `LoRA` 技术，支持对 Qwen2.5 等主流开源大模型进行快速、低显存消耗的指令微调（SFT / DPO 等）。
- **🎙️ 声音克隆 (TTS)**：集成 `SparkTTS` 与 `Llasa` 模型，不仅能模仿说话方式，还能高度还原目标人物的声音特质。
- **📊 评估与部署**：提供完善的评测脚本与 Web UI 界面（Web Demo），支持本地或服务器的一键 API 部署。

## 📂 项目结构

```text
WeClone/
├── dataset/                  # 训练与测试数据集存放目录
├── examples/                 # 配置文件模板 (JSONC)
├── weclone/                  # 核心源码目录
│   ├── core/                 # 推理引擎与 PII 隐私保护模块
│   ├── data/                 # 数据清洗、对话解析与 QA 生成
│   ├── eval/                 # 模型评测与 Web Demo 界面
│   ├── prompts/              # 提示词工程模板
│   ├── server/               # API 服务化部署
│   ├── train/                # 针对不同模式的模型训练脚本
│   └── utils/                # 日志、重试机制等通用工具类
├── weclone-audio/            # 语音克隆模块 (SparkTTS / Llasa)
├── liyunlong_lora_output/    # (被 Git 忽略) 本地模型微调权重输出
└── launcher.py               # 项目快捷启动入口
```

## 🚀 快速开始
1. 环境准备
建议使用 Conda 创建独立的 Python 虚拟环境：

```
conda create -n weclone python=3.10
conda activate weclone
pip install -r pyproject.toml # 或按照你的依赖管理方式安装
```
2. 数据处理
将导出的聊天记录放入对应目录，执行数据清洗与转换：

```
python launcher.py data_process --config examples/mllm.template.jsonc
```
3. 模型微调
基于清洗好的数据集启动 LoRA 微调：

```
python launcher.py train --model qwen2.5-7b --dataset data/real.json
```
4. 启动 Web 交互界面
训练完成后，启动图形化界面与你的“数字分身”对话：

```
python -m weclone.eval.web_demo
```
## ⚠️ 声明与免责条款
本项目主要用于学术研究（毕业设计）与技术交流，请勿将生成的内容用于任何非法、侵权或欺诈用途。

涉及真实用户数据时，请务必先运行项目中的 PII 脱敏模块。
