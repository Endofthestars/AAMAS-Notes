---
title: "Structured Agent Distillation for Large Language Model Agents"
conference: "AAMAS"
year: 2026
track: "aaai"
topics: ["agent_engineering", "generative_agents", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/OLHJ8062"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OLHJ8062.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-04b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["agent-distillation", "reasoning-action-spans", "react-agents", "benchmark-evaluation", "teacher-trace-dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Structured Agent Distillation for Large Language Model Agents

## 一句话总结

Structured Agent Distillation 将 ReAct 轨迹切为 reasoning 与 action spans，并施加分段对齐损失，使小模型保留教师的推理结构和执行行为，而不是把 agent trajectory 当成扁平 token 序列蒸馏。

## 方法与证据

- 论文认为 token-level KD 无法表达 reasoning--action 的语义角色和跨 span 依赖；方法对 teacher trajectory 的 `[REASON]`/`[ACT]` 段分别监督，并以 span-level alignment 对齐 CoT 与动作（§1–3）。
- 在 ALFWorld、WebShop、HotPotQA-ReAct 上，使用 success、reasoning length、CoT match 与 episode latency；数据分别为 5,400/1,200/1,475、8,000/2,000/2,000、84,000/3,447/3,000 的 train/val/test，结果平均五次运行（§4）。
- GPT-2 1.5B teacher、120M student 时，表 3 的方法在三个任务成功率为 43.7/41.2/52.8，token KD 为 39.4/36.7/48.3；方法也缩短 reasoning length 与 latency。OPT/LLaMA/Orca2 teacher 的扩展表中呈同方向改进（§4–6）。

## 适用边界与复现

- CoT match 衡量与教师痕迹的一致，不直接证明推理真实、稳健或安全；收益依赖有质量且可获得的 ReAct teacher trajectories，且论文承诺 acceptance 后发布代码。
- 复现需公开 span parser、教师/学生 checkpoint 与 prompts、各 loss 权重、rollout/tool 环境、token/latency 计量、所有 splits/seeds；部署还应测量工具失败、分布漂移、成本及不忠实 reasoning 的风险。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/OLHJ8062.pdf) 人工核对分段思路、实验设置、表 3 与 ablation；未把 benchmark CoT 对齐解释成现实任务的可验证推理保证。
