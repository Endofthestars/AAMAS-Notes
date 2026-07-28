---
title: "Greedy Routing Reachability Games"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/JJND5892"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JJND5892.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["complete_position_knowledge_assumption", "strict_metric_routing_scope", "unit_edge_cost_assumption", "approximate_equilibrium_not_exact", "dynamic_network_unmodeled", "robustness_stretch_not_guaranteed"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Greedy Routing Reachability Games

## 一句话总结

本文研究位置固定、每个 agent 以最少自购边换取对所有节点 greedy-reachability 的网络形成博弈。有向边时每个 Nash equilibrium 同时是 social optimum（PoA=1）；无向二维欧氏空间中精确均衡的 PoA 介于 1.75 和 1.8，但 best-response dynamics 会循环。作者可多项式构造边数近最优的 2-NE（二维还可 +2-NE），这并不证明任意无向实例有精确均衡，也不提供现实网络的可靠性、时延或抗故障保证。

## 方法与证据

- agents 是 metric space 中已知位置的点；策略为购买 incident edge。greedy path 要求每一跳到目标的 metric distance 严格下降；若一个 agent 不能 greedy-reach 所有其他点则承担无穷 penalty，否则 cost 为其购买边数（§1.1）。因此模型优化 unit link count 与全对可达性，不计距离/能耗/带宽/时延、拥塞、支付转移、异质偏好、链路失败或部分位置知识。
- 论文区分有向与无向 ownership。每个 NE 必须是 navigable，因为 agent 总能以直接边规避无穷 penalty；同时定义乘法 \(\beta\)-NE 与加法 \(+\gamma\)-NE（§1.1）。这些稳定性是一次性单 agent deviation 定义，不能等同多方重谈、coalition-proof、重复博弈稳定或真实自治系统的收敛。
- 对有向边，Theorem 1 给出“每个 NE 是 SO、每个 SO 是 NE”，Corollary 1 因而 PoA=1；不存在 best-response cycle（Lemma 5）。在欧氏任意正维可多项式算 SO/NE 并判定 profile 是否为 NE（Cor. 2–3），但单个 agent 的 best response 仍是 NP-hard（Theorem 2）。
- 欧氏几何中 greedy routing degree 可多项式计算；二维至多为 6，高维由 kissing number \(K(D)\) 界定（Lemma 3–4）。这是固定、精确欧氏几何与严格距离比较的结构性质；坐标噪声、ties、非欧氏测距或协议所需的路由状态会破坏其直接适用。
- 无向二维精确 NE 的 PoA 上界为 1.8（Theorem 3），构造下界 1.75（Lemma 7）；高维上界为 \(2-1/K(D)\)，一般 metric 小于 2（Cor. 4）。这些是最坏情况下“购边数量/社会最优购边数量”的理论比，不报告实际 traffic performance 或平均实例质量。
- 无向 best responses 可形成 cycle（Theorem 4），故不能把朴素去中心化更新当作收敛算法。作者证明任意 general-metric SO 可赋 ownership 成 2-NE（Theorem 7），二维 SO 可成 +2-NE（Theorem 8），并在欧氏空间多项式构造相应近似网络（Theorem 10）。摘要中“almost stable”应准确读作这些近似定义，而非 exact NE existence。
- 构造的二维网络边数至多是 optimal 的 1.8 倍，优于文中所述 Delaunay triangulation 的 factor 3（§1.3, §4.3）。这是在该模型下的边数近似比较；Delaunay 还可能有不同的实现便利、局部维护、几何质量、stretch 与故障容忍性质，不能由单一 factor 直接否定。
- 作者把加入 stretch 或 robustness 作为未来工作，并称无向 exact equilibria 是否存在仍是 open/challenging（§5）。因此没有仿真/部署证据显示随机投放传感器、IoT 或灾后通信会自然形成这些网络。

## 适用边界与复现

- 适用于研究 greedy routing 所需的最小结构与单边拥有者激励，尤其是位置稳定、可精确比较距离、目标仅为全对 reachability 的抽象网络。工程设计应另外验证地址分配、邻居发现、路由 loop/tie handling、控制面开销、负载、移动性与故障。
- 用于应急、物联网或关键通信前，必须补充冗余路径、连接/延迟/stretch 下界、容量与能耗约束、恶意节点与 Sybil 防护、隐私保护定位、断链检测、分区恢复和受限更新协议。可达性不等于在压力下可用，更不等于安全通信。
- 复现需实现严格 greedy rule、无穷不可达 penalty、directed/undirected ownership、NNG 与 social optimum；生成二维与高维 point sets，验证 Theorem 1–10 的小实例构造、PoA 1.75/1.8 家族、best-response cycle，以及近似 ownership assignment。报告实例规模、position precision、tie policy、计算时间和所有失败/循环轨迹。
- 后续应研究 uncertain/dynamic coordinates、limited local information、asynchronous updates、weighted edges、heterogeneous objectives、coalitions、finite penalties、edge failures、robust/stretch constraints和经验拓扑；还应明确在这些扩展下 exact equilibrium 是否存在与计算复杂度。

## 与 AAMAS 的关系与核验说明

这是将 greedy-routing 几何结构与 network-creation game 结合的 AAMAS 理论工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JJND5892.pdf) 核对模型、严格递减路径、directed PoA=1、best-response NP-hardness、二维 PoA 1.75–1.8、cycle、2-NE/+2-NE、Delaunay factor 3 比较与作者开放问题；没有把近似均衡或静态 metric 结论写成无向精确收敛、现实网络可用性或鲁棒/低延迟保证。
