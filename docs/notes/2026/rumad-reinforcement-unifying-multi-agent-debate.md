---
title: "RUMAD: Reinforcement-Unifying Multi-Agent Debate"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["marl_coordination", "generative_agents", "agent_engineering"]
dblp_key: ""
doi: "10.65109/CBJO8409"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CBJO8409.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04c"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["multi-agent-debate", "ppo-topology-control", "token-efficiency", "zero-shot-transfer", "quantized-llms"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# RUMAD: Reinforcement-Unifying Multi-Agent Debate

## 一句话总结

RUMAD 以 PPO 控制多 LLM 辩论的有向通信图：控制器不读取原始推理文本，只看相似度、答案一致性、进度和 token 成本等高层动态，并通过边权、可见性和 agent activation 在准确率、共识与开销间权衡。

## 方法与证据

- 每轮采样的 edge-weight matrix 决定邻居信息进入 prompt 的程度及 agent 是否更新；budget loss 将可见边数的先验 $B$ 作为训练期稀疏正则，而不是推理期硬限制（§3）。
- reward 分层结合逐轮与 episode 级 solution quality/progress、cohesion 和效率；在 MMLU dev 上训练 PPO controller，六个量化 agents 由 LLaMA-3.1-8B、ChatGLM-4-9B、DeepSeek-Math-7B 各两名组成（§3–4）。
- 表 3 中 $B=12$ 的 RUMAD 在 MMLU/GPQA/GSM8K 为 68.3/31.9/86.4% 和 11.4/19.5/10.5k tokens；移除 activation 时 token 成本升至 51.9/67.5/45.0k。论文称相对 fully connected MAD 在 MMLU、GSM8K 节省逾 80%，并零样本迁移到后两者（§4）。

## 适用边界与复现

- “content-agnostic” 仍使用文本 embedding 相似度及答案/进度信号，不等同于隐私保护或中立性证明；结果依赖 0-shot、4-bit、单张 RTX 3090 的特定 agent pool、prompt 与预算。
- 复现需开放 PPO observation/reward 系数、图采样/threshold、activation 规则、LLM versions/quantization/prompts、benchmark splits、token accounting、所有 seeds 与基线配置。还应评估错误共识、对抗 agent、长程工具任务及控制器本身的训练成本。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CBJO8409.pdf) 人工核对控制机制、六 agent 设置、表 3 和 zero-shot 描述；未把 benchmark efficiency 解释为一般辩论真实性或安全性保证。
