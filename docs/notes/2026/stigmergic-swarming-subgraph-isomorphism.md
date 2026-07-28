---
title: "Stigmergic Swarming Agents for Fast Subgraph Isomorphism"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "agent_engineering", "applications"]
dblp_key: ""
doi: "10.65109/DEZC1973"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DEZC1973.pdf"
preprint_url: "https://arxiv.org/abs/2601.02449"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["heuristic_claim_scope", "synthetic_evaluation_scope", "complexity_conditions"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Stigmergic Swarming Agents for Fast Subgraph Isomorphism

## 一句话总结

论文提出 ASSIST：让大量轻量代理通过共享信息素场协同，从带标签的查询图与数据图中逐步强化可匹配边，作为最大部分子图同构的随机启发式方法。

## 方法与证据

- 目标是带标签（允许标签重复）的最大部分子图同构；作者明确将 ASSIST 定位为启发式，而非精确求解器（摘要、§1–2）。
- 初始化的 *peering* 按节点标签和 detail 找跨图候选点对，并将数据图置于树索引中；论文给出的该步骤复杂度是 $O(q\cdot\log d)$（§4.1、§4.3）。
- 每个代理完成“查询点→数据 peer→数据邻居→查询 peer→起点”的四步回路；成功回路给路径上的节点和边加信息素，所有信息素每个 tick 衰减。重复回路将局部匹配合成为更大子图（Algorithms 1–2、§4.4、Figure 3）。
- 实现使用 Repast；当前版本是单线程，论文把多线程/GPGPU 重实现列为未来工作（§4.2、§6.1）。
- §5 在 NetworkX 生成的 Barabási–Albert 图上实验，报告至少五个随机种子下的中位数与四分位范围。对 100 节点查询，匹配阶段在 $d>3000$ 时基本平坦；作者报告在其设定中 peering 与 $q\log d$ 呈线性关系，匹配时间随查询规模和已发现公共子图规模上升（§5.1–5.4，Figures 7–11）。

## 局限与复现

- “匹配对数据规模恒定”的表述是论文在已 peering、带明确标签/detail 的合成 BA 图上的实验性结果；不构成任意图、任意标签歧义或任意实现的最坏情况保证。
- 评估主要固定每个自变量场景的一组三元图（kernel、query、data），仅改变随机种子；作者也明确建议扩展到多组随机图和 Erdős–Rényi、Watts–Strogatz 等模型（§5.1、§6.2–6.3）。
- 近似标签、时间顺序边与缺失节点/边在 §6.4 是拟议扩展，而非正文主实验已充分验证的能力。
- 复现应保留 Algorithms 1–2、§4 的标签/detail、信息素与终止条件，及 §5 的 BA 生成参数（`m=2`）、种子数、计时硬件和 Figures 7–11；论文未在正文提供可核验的代码仓库链接。

## 与 AAMAS 的关系与核验说明

这是一种以间接环境信号协调独立代理的计算型多智能体系统：重点不在通信协议，而在信息素强化如何使局部回路收敛为候选公共子图。本文笔记使用与官方题名、作者和 DOI 一致的[作者公开预印本](https://arxiv.org/abs/2601.02449)作主文本核验；官方 PDF 在本轮传输中损坏，未以损坏文件作证据。
