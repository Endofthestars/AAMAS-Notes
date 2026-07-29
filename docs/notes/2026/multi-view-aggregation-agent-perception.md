---
title: "More Views, More Problems? A Critical Analysis of Multi-View Aggregation for Agent Perception"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "human_agent_interaction", "agent_engineering"]
dblp_key: ""
doi: "10.65109/CERC5181"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CERC5181.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03l"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "small-embodied-dataset", "domain-shift", "caption-metric-sensitivity", "llm-hallucination"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# More Views, More Problems? A Critical Analysis of Multi-View Aggregation for Agent Perception

## 一句话总结

这项具身感知研究比较单一俯视图、可事后选出的最佳视图、逐视图平均、以及 LLM 汇总多视图 caption。多视图并非天然更好：最佳视图会稳定提升，但把嘈杂 caption 直接汇总在 3D 域偏移下会产生幻觉，甚至低于固定俯视图。

## 方法与证据

- Franka Emika Research 3 搭配 eye-in-hand RealSense D435i：每个物体有固定 top view，及沿半球轨迹采集的 $M$ 个视图并用 SAM2 分割；数据分为真实工具与其 3D-printed replicas，用于 domain shift 检验（§2）。
- 感知 VLM 为 $M_{VLM}$，聚合 LLM 为 $M_{LLM}$。比较四种策略：top-view；对所有主动视图跨指标排序得到的 oracle-like consensus caption；各单视图得分平均；以及由 LLM 从所有 per-view captions 合成描述（§2.1）。
- 使用 lexical、scene-graph、embedding 等 caption metrics；选出 Qwen 2.5 VL 和 GPT-4.1 作后续实验，后者也作聚合器（§2.2）。作者报告 real objects 上 Qwen 的 consensus 至多在 70% 样本严格优于 top-view；naive average 往往更差。合成通常胜过简单平均但不及 consensus，3D 数据上可能把 wing nut 幻觉为三叶黑色螺旋桨（§3）。

## 适用边界与复现

- consensus 是使用 ground-truth metrics 后选出的上界，不是在线 agent 可直接执行的 view-selection policy。caption 指标与 reference phrasing 敏感；作者也观察到 BLEU/ROUGE 可惩罚合理同义表达，而 SPICE/BERTScore 更稳健。
- 摘要未说明数据规模、具体视角数、标注协议、模型版本/提示词、聚合 token 预算与统计不确定性。部署前应在任务相关物体、传感器噪声、遮挡与抓取闭环中验证，且为多视图冲突设置 grounded verification 或拒答机制。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/CERC5181.pdf) 人工核对四种策略、机器人采集设置和摘要中报告的失败案例；不将 caption 指标改进写成操作成功率保证。
