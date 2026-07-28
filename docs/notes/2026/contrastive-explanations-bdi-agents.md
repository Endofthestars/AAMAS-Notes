---
title: "Contrastive Explanations of BDI Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics:
  - "safety_verification"
  - "agent_engineering"
dblp_key: ""
doi: "10.65109/VRTD1803"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/VRTD1803.pdf"
code_url: "https://doi.org/10.5281/zenodo.18603362"
note_status: "reviewed"
review_route: "spark_draft_escalated_full_spark_qa"
risk_level: "medium"
escalation_model: "gpt-5.6-sol"
escalation_reason: "full_verification"
escalation_verdict: "pass"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.6 Sol)"
reviewed_at: "2026-07-28"
---

# Contrastive Explanations of BDI Agents

## 一句话总结

论文为 BDI goal-plan tree 定义“为什么做 \(X\) 而不是 \(F\)”的对比解释生成方法；
对比解释通常更短，但人类实验显示其偏好、理解和信任收益高度依赖具体场景，解释并非
越多越好。

## 研究问题与设定

作者扩展既有 BDI 行为解释机制，研究两个问题：

1. 如何从 goal-plan tree 和执行 trace 生成相对于显式或隐式 foil 的对比解释；
2. 相比完整解释或不给解释，对比解释是否更短、更受偏好，并提高理解、正确性信心与信任。

计算实验使用合成 goal-plan tree。人因实验包含煎饼机器人和搜救无人机两类系统、
每类三个场景，并把参与者分配到完整解释、对比解释和无解释条件。

## 方法

- 在 action、goal 与 AND/顺序/选择节点构成的 goal-plan tree 上定义完整解释 \(E_X\)。
- 对显式 foil \(F\)，从 \(E_X\) 中过滤与 \(F\) 共享、因而不能解释差异的祖先节点，
  得到 \(E_{X/F}\)。
- 对隐式 foil，先计算动作 \(X\) 的有效 foil 集合，再合并相应的对比解释。
- 生成 1,000 棵合成树比较解释长度；随后以九个假设 H1–H9 进行问卷研究，并采用
  Mann–Whitney、Kruskal–Wallis、Dunn/Holm 和 Spearman 相关等检验。

## 实验与证据

| 结论 | 证据位置 | 核验状态 |
|---|---|---|
| 对比解释随完整解释增长而保持更短 | Figure 2、§4.3，pp.26–27 | 已核对计算实验与图 |
| 收到 161 份回答；注意力检查后 131 份，再排除 27 份矛盾回答，最终分析 104 份 | §5.3.1，p.27 | 已核对筛选流程 |
| H1 仅部分支持；不同场景分别偏好完整或对比解释 | Table 1、§5.3.2，pp.27–28 | 已核对方向 |
| H2/H3 未获支持，感知质量和细节适当性无显著优势 | Table 1、§5.3.2，p.28 | 已核对 |
| H4 支持：对比解释组系统信任更高，两个系统的 \(p=0.008575\) 与 \(p=0.04205\) | §5.3.3，p.28 | 已核对数值 |
| H5 只在场景 2 显著（\(p=0.04079\)）；H6 只在场景 1、2 显著（\(p=0.005351,0.04028\)） | §5.3.3，pp.28–29 | 已核对数值与范围 |
| H7 未支持；H8 不支持总体优势，部分场景无解释组反而更正面 | §5.3.4，p.29 | 已核对 |
| 一般技术信任与两系统信任相关：\(\rho=0.52,0.38\) | §5.3.5，p.29 | 已核对相关系数 |

## 主要贡献

1. 把 BDI 行为解释扩展为支持显式和隐式 foil 的对比解释。
2. 给出可执行的 tree/trace 生成与解释过滤规则。
3. 同时提供计算长度评估与人类受试评估。
4. 以负结果说明更短或更完整的解释都不能自动转化为理解和信任。

## 局限与威胁

论文讨论及未来工作表明：

- 人因结果明显依赖场景，需要更多任务和更具代表性的参与者；
- 解释可能重复用户已知信息，或采用用户并不认可的 foil，从而降低信任；
- 当前方法针对 BDI tree；扩展到非 BDI agent 需要 policy graph 等替代表达。

我们的额外判断：

- 从 161 份回答筛到 104 份可能引入选择偏差；
- 多场景、多指标检验提高偶然显著风险，尽管部分比较使用了 Holm 校正；
- 主要结果来自自报量表，未直接测量真实高风险决策行为；
- 正文引用 Zenodo 补充材料，但本轮只核验正文，未独立复算问卷原始数据。

## 与 AAMAS 研究方向的关系

论文连接 `agent_engineering` 与可解释性安全：它不仅定义解释算法，还检查解释接口对
信任与判断的真实影响。其结果提醒 AAMAS 智能体系统不能把“提供解释”直接等同于
“提高可信度”。

## 复现信息

- 官方 PDF SHA-256：`79e3819fc4ba07098985a5158b16138284dd6fe23e6e07abf9e14c805d6190b6`
- DOI：<https://doi.org/10.65109/VRTD1803>
- 补充材料：<https://doi.org/10.5281/zenodo.18603362>
- 计算实验：1,000 棵合成树；正文给出生成参数与解释算法
- 人因数据/问卷：正文指向补充材料 [48]，本轮未独立下载核验
- 当前核验级别：`SOURCE_METHOD_RESULTS_LIMITATIONS_VERIFIED`

## 核验说明

Spark 负责首次结构化阅读；复核阶段逐项检查了 H1–H9、样本筛选、显著性数值和作者
结论。`reviewed` 表示正文中的方法、主要结果、比较和局限已核对，不表示完成独立统计
复算，也不表示经过人类领域专家签字。
