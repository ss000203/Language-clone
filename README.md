# 🤖 WeClone (数字人分身/语言风格克隆)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Model](https://img.shields.io/badge/Model-Qwen2.5--7B-orange)

## 📖 项目简介

**WeClone** 是一个基于大语言模型（LLM）与文本转语音（TTS）技术的综合性数字分身克隆项目。本项目旨在通过个人的历史聊天记录或特定角色的台词数据，微调出高度还原目标人物语言风格和音色的专属 AI。

本项目不仅是一个涵盖数据清洗、模型微调、在线推理与系统评测的全链路工程，同时也作为高校毕业设计项目进行持续维护与优化。目前，项目内已包含针对经典影视角色**李云龙**的成功微调案例。



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
