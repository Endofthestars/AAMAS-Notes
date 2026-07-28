---
title: "Automatically Benchmarking LLM Code Agents through Agent-driven Annotation and Evaluation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "applications", "safety_verification"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HJFB4234.pdf"
preprint_url: "https://arxiv.org/abs/2510.24358"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["benchmark_construction_bias", "judge_human_alignment_scope", "fixed_interface_evaluation", "proprietary_model_reproducibility"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Automatically Benchmarking LLM Code Agents through Agent-driven Annotation and Evaluation

## 一句话总结

该文提出 PRDBench：用 agent 生成 PRD、代码 scaffold 与可执行的评测准则、再经人工检查/迭代修正后移除 scaffold 的项目级 Python benchmark；并训练专用评测 agent PRDJudge，以执行测试和审查产物来对代码代理打分。

## 方法与证据

- PRDBench 最终含 50 个 Python 项目任务、20 个应用域、1,258 个 metrics。seed tasks 来自内部 AI 产品开发请求、GitHub CS 课程项目和 CS 论文复现任务；入选要求可完全用 Python 实现且关联数据公开（§3.1、§3.3）。这不是从真实生产 issue 随机抽样的全量软件工程分布。
- 生产链路为：(1) 代码 agent 生成结构化 PRD，GPT-4.1 生成 Arrange–Act–Assert 的 metric outline；(2) 代码 agent 生成 scaffold、接口与具体 criteria scheme；(3) 人工只检查接口/预期输出是否与 PRD 相符；(4) 将反馈交给 agent 迭代修复，保留至少经过 5 轮人机 refinement 的任务；(5) 删除 scaffold，仅保留 PRD、criteria、测试工件、数据和参考解（§3.2）。因此“低人工成本”指不逐项手写 metric/代码，并不代表没有人工质量控制。
- 三类评测是 408 项 unit test、732 项 shell interaction、118 项 file comparison；每个任务的 PRD 平均 105.22 行，scaffold 行数均值 2,583.8（中位 1,279，范围 188–9,185）（§3.3、Figures 3–4）。
- PRDJudge 有文件读写、命令执行、图像处理和专用 judge 等工具；对 criteria 中的测试执行、日志/文件差异做解释并给分。其训练候选由 Qwen3-Coder-480B-A3B 对 11 个 code-agent 的输出生成 2,147 条 evaluation trajectories，先保留与人工分数完全一致的 1,742 条，再过滤无效/冗长 tool use，得到 911 条 LoRA 训练轨迹；base model 为 Qwen3-Coder-30B-A3B（§4.1–4.2）。
- 人工标注采用两轮：两名 annotator 一致即采用，不一致由第三人裁决。评测的 Human Alignment Rate（HAR）是 judge 分数与这份人工 ground truth 的 exact match，不是软件正确性、漏洞检出率或用户满意度（§4.2、§5.3）。
- 在报告的 fixed-interface 测试中，PRDJudge 的 in-domain/out-of-domain HAR 分别为 91.75%/92.69%，对比 Qwen3-Coder-480B 为 90.32%/87.91%、GPT-5.2 为 89.76%/87.09%；该对比也报告平均 token 与时间，专用 judge 在这组设置下更短、更快（§5.3、Table 3）。
- 对 code agents，表中 GPT-5.2 从 DEV 62.49% 到 DEBUG 69.00%，Claude-4.5 从 69.19% 到 56.40%；作者强调迭代 debugging 并不保证提升。free-development 模式需要 judge 动态改写测试接口，作者明确认为该过程会引入评价噪声，fixed inference 才是当前较可靠的设置（§5.4、Table 4、Figure 7）。

## 局限与复现

- benchmark 的 PRD、scaffold、criteria 及“至少五轮”筛选均由同类 agent 加人工共同塑形，可能偏向其生成的接口和可判定任务；50 个 Python 项目不足以代表多语言、遗留系统、私有依赖、代码审查协作或生产运维。
- PRDJudge 的 HAR 仅相对于该数据集的人工标准与固定接口设置。训练轨迹先按与人工分数完全一致过滤，虽能减少错误监督，也使结果不能自动外推到新接口、不同 rubric、对抗性提交、长期 agent trajectory 或真实安全审计。
- 评测 agent 本身依赖执行环境、依赖安装、测试工件和部分外部模型/工具；论文的可复现结论应分别核验数据、judge 权重、运行沙箱、依赖版本、模型访问和成本，而不是只复跑最终 pass rate。
- 复现应固定任务与数据版本、PRD/criteria 的 revision history、每个任务的人工检查记录、scaffold removal 过程、各类 metrics、code-agent 提示词和工具权限、DEV/DEBUG 预算、judge 运行环境及三次以上 judge 重复运行；还应补充跨语言、真实 issue、对抗性测试和人类开发者效用验证。

## 与 AAMAS 的关系与核验说明

该文将代码代理作为自主系统，研究其任务构造、工具化评测与人机对齐，属于 agent engineering、应用与验证基础设施。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2510.24358) 核对 benchmark 构造、PRDJudge 训练筛选、HAR 定义、表格结果和 free-development 限制。
