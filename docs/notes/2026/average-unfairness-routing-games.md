---
title: "Average Unfairness in Routing Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "applications"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HAKF7947.pdf"
preprint_url: "https://arxiv.org/abs/2601.16187"
note_status: "reviewed"
review_route: "manual_formal_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_formal_scope_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["nonatomic_fractional_flow_scope", "fairness_definition_scope", "cso_strictness_conditions", "static_traffic_model"]
escalation_model: "none"
escalation_reason: "manual_primary_source_check"
escalation_verdict: "manual_theorem_scope_review"
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source theorem check)"
reviewed_at: "2026-07-29"
---

# Average Unfairness in Routing Games

## 一句话总结

论文为静态非原子路由流定义 average unfairness：每个 commodity 的平均旅行延迟与其已使用路径中最短延迟之比；它在一般条件下不超过 loaded unfairness，并在同一容忍度下使 constrained system optimum（CSO）的总延迟不高于 loaded 约束，平行链路网络中除已达 system optimum 外严格更低。

## 方法与证据

- 模型是有限有向网络、多 source–destination commodities、连续非递减的边延迟函数与固定正需求的可分割 path flow。总成本为所有 path latency 的 flow-weighted 和；这不是离散驾驶者、动态需求、随机出行时间或带容量排队的交通模型（§2.1）。
- loaded unfairness 比较同一 commodity 所有正流路径的最大/最小延迟；UE unfairness 比较当前正流路径延迟和 Nash flow 延迟。新定义的 average unfairness 为该 commodity 总 latency 除以需求与其正流路径最小 latency 的乘积，再取 commodities 最大值；若全为零延迟，约定 $0/0=1$（Definitions 2–4）。
- 对可微、standard（$x\ell(x)$ convex）且包含所有常数函数的 latency class，Theorem 1 给出 $U^L(\mathcal L)=U^{UE}(\mathcal L)=U^A(\mathcal L)=\gamma(\mathcal L)$，其中 $\gamma(\ell)=\sup_{x>0}\hat\ell(x)/\ell(x)$。例如非负系数、次数至多 $n$ 的多项式类，Corollary 1 为 $n+1$；这是跨实例与 optimal flows 的最坏上确界，不是每个具体实例都会达到该值。
- 对任意实例/可行 flow，Proposition 1：要么 $U^L>U^A>1$，要么两者均为 1；因此 average 不超过 loaded，二者相等只在完全公平时。UE 与二者一般没有全序关系；single-commodity optimal flow 下 Proposition 2 才给出 loaded 大于 UE，或二者均为 1（§3.2）。
- CSO 在 $U(f)\le 1+\beta$ 下最小化总延迟。由上述包含关系，Corollary 3 保证 $C^A\le C^L$。Proposition 4 的严格性还需要 $\beta>0$、standard 假设，并且存在 loaded-CSO 解对每个 commodity 都使用一个全局最短 latency path；平行链路网络中该条件保证成立（Corollary 4）。一般网络不保证严格改进，论文给出 Braess 反例（§4.1）。
- 数值部分以 $\alpha=0.01$ 步进的插值凸程序近似 Pareto frontier，在 Anaheim、Sioux Falls、Massachusetts、Friedrichshain 四个 benchmark 上使用 BPR 函数。图中 average 约束除 Friedrichshain 的一个数据点外均有更低成本；这是近似算法下的四个静态网络观测，不替代一般严格性定理（§4.2）。

## 局限与复现

- “公平”仅是同一 OD commodity 已使用路径的时间比值：它不含跨 OD 群体、收入、可达性、残障、路线风险、排放、可靠性或个体离散体验；对 commodity 聚合采用 max（论文说明改为平均时其结果仍成立），仍需由具体政策决定是否合理。
- 理论界和 CSO 结论依赖分数、静态、非原子 flow 与延迟函数假设。原子拥堵博弈、实时重路由、需求弹性、随机事故、容量约束或离散信号控制不能直接套用；作者也把 atomic games 列为未来工作。
- $C^A\le C^L$ 不意味着每个实例严格更优；严格结果有明确的 path-support 条件。实际求解时还须处理可能多个 edge-flow 相同但 path assignment 不同、因而 unfairness 不同的情形。
- 实验扫描固定步长 $\alpha$ 而非精确求解所有非凸 CSO，并仅用了 BPR 参数和四个公共网络；“real-world network benefit”应读作模型实验，不是实地驾驶时间或接受度证据。
- 复现应固定网络/OD、BPR 参数、path enumeration 与 flow decomposition，报告每个 $\alpha$ 的 $C(f)/C(f^\star)$、$U^A$、$U^L$ 与误差；对理论部分单独验证 Pigou/Braess 例、steepness 前提和平行链路的最短已用路径条件。

## 与 AAMAS 的关系与核验说明

该文把效率—公平权衡形式化为多 agent 路由分配中的 flow 约束，并给出度量间的精确关系。笔记依据作者公开的 [arXiv PDF](https://arxiv.org/pdf/2601.16187) 核对模型、定义、Theorem 1、Propositions 1–4、平行网络推论和数值协议；不将路由延迟比外推为广义社会公平或现实交通政策成效。
