---
title: "BeWater: Effective Protesters Navigate Watersheds in Street Networks"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["marl_coordination", "applications", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/EIDE2300"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EIDE2300.pdf"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["osm_data_and_city_scope", "offline_tactic_search_vs_local_information", "synthetic_walker_model", "real_world_safety_not_evaluated"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# BeWater: Effective Protesters Navigate Watersheds in Street Networks

## 一句话总结

BeWater 是一个在加权街道图上让独立 walker 沿局部最大可观测量前进、在 maxima 处停止的分布式聚集协议；其终止与 watershed forest 有形式证明，且在 Hong Kong、Paris、Seattle 的 OSM 图上，离线选出的多 observable tactic 能减少终点群组数、增大汇集规模，但这不是对真人抗议、通信受限行为或安全性的实证。

## 方法与证据

- 城市以 OSMnx 默认参数提取的无向街道图表示，仅保留最大连通分量并去除 degree-1/self-loop；链接离散化为约 10m slices。Hong Kong island、Paris、Seattle 分别有 1,878/7,289/12,485 nodes（§2–3）。
- walker 在 crossing 处跟随唯一最大权重链接，在 street node 沿来向前进；遇到多个 maxima 停止，对特定 descending U-turn 也停止。可观测量包括街长、名称长度、车道数、POI 数/密度、限速、area 及建筑编号方向（§3、§5）。
- Theorem 1 证明每个 walker 有限步停止；由此定义 sink 与 watershed。Theorem 2 将各 walker 的运动关系构成无环 watershed forest，支撑从所有起点直接计算最终群组（§5–6）。
- 单 observable 在三城多产生小 watershed。作者再用长度为 `k` 的 observable sequences（tactics）将前一 observable 的 sinks 作为下一阶段起点，离线遍历到 `k=7`；对 Paris 11th 所有 7-tactics 的组合数为 391,909，文中称数分钟完成，最佳 tactic 的群组数下降并比单一 observable 更聚集（§9–10）。

## 局限与复现

- 本文实验仅是确定性图 walker，未收集/模拟人群从众、恐惧、可达性、体力、障碍、实时封路、警力、群体识别、通信或拥挤/安全后果；“effective protesters”仅意味着在该模型中较大最终 watershed，不代表任何现实抗议成效或风险降低。
- 虽然单步选择是局部且 memoryless，最佳 observable 顺序是针对完整 OSM 城市图离线穷举得到的，且每城最优次序不同。若参与者事前不共享同一 tactic、城市数据过期或现场不可观察 lanes/POI/建筑编号，该部署假设不成立。
- OSM tags 缺失时作者对 lanes 作默认假设，街道抽取/清理/离散化、10m step、权重 ties、单向道路被忽略的无向图处理都会改变 watershed。文中只覆盖三个城市及有限 observables，不说明跨时段或地图版本稳定性。
- 复现应固定 OSM snapshot/OSMnx version、边清理与离散化、每条 tag 的缺失值规则、所有 tactic sequences 和 tie behavior，报告规模分布而不仅最优 tactic；任何人本/公共空间应用还需独立的安全、法律、伦理和现场可行性评估。

## 与 AAMAS 的关系与核验说明

该文研究利用街道图局部可观测量进行无通信多主体汇集的图协议。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EIDE2300.pdf) 核对协议、Theorem 1–2、OSM 图和多 observable 搜索范围，未把抽象 walker 的聚集结果外推为现实群体行动建议。
