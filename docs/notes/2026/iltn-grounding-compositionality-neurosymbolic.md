---
title: "Grounding vs. Compositionality: On the Non-Complementarity of Reasoning in Neuro-Symbolic Systems"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/SDCB9121"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SDCB9121.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03z"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "neuro-symbolic-reasoning", "logic-tensor-networks", "synthetic-visual-puzzles", "compositional-shift"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Grounding vs. Compositionality: On the Non-Complementarity of Reasoning in Neuro-Symbolic Systems

## 一句话总结

该文主张符号 grounding 不会自动带来组合式推理；iLTN 在 Logic Tensor Network 上显式学习多步 belief refinement，并在实体、关系和规则三类组合分布偏移的合成视觉逻辑题中优于只做 grounding 的模型。

## 方法与证据

- 任务从图像感知对象世界状态，在一阶逻辑知识库约束下求一致赋值；测试分别引入新常量、未见关系/公理族和更长或不同的推理链（§2）。
- iLTN 反复进行约束驱动的可微满足度更新、鼓励离散清晰假设的可微 relaxation，并可按难度自适应展开更多步骤；推理轨迹是训练对象，而非单次逻辑 loss 的副产物（§3）。
- 比较 grounding-only、提供预 grounding 符号输入的 reasoning-only 与全 iLTN。作者报告所有三类 shift 中 grounding-only 明显退化，全 iLTN zero-shot robustness 更好；摘要未给出绝对数值或方差（§4–5）。

## 适用边界与复现

- 证据限于受控合成视觉逻辑 puzzles，不能直接证明其能处理开放世界语言、噪声知识库或多智能体协商；“显著改善”需要完整 benchmark 与统计结果佐证。
- 复现需公布图像/知识库生成器、三类 shift 的 train-test split、模糊逻辑语义、update/discretization/adaptive-unroll 参数、监督信号和每种 ablation 的 seeds/metrics。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/SDCB9121.pdf) 人工核对 taxonomy、iLTN 三步更新与对照设计；未把概念性 AAMAS implication 当作真实 multi-agent 性能证明。
