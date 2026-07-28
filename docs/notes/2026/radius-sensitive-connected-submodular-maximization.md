---
title: "A Radius-Sensitive Approximation Algorithm for Connected Submodular Maximization"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "planning_scheduling", "game_theory_mechanism"]
dblp_key: ""
doi: "10.65109/IPZQ7320"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IPZQ7320.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "low"
risk_tags: ["theoretical_approximation_scope", "strong_value_oracle", "bicriteria_size_violation", "optimal_radius_unknown", "no_empirical_evaluation", "epsilon_runtime_tradeoff"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# A Radius-Sensitive Approximation Algorithm for Connected Submodular Maximization

## 一句话总结

论文研究 CSM/DCSM/DRCSM：在图中选至多 \(k\) 条边的 connected tree/out-tree，以最大化 non-negative monotone submodular vertex objective。其 GreedyRadius 将任意 DRCSM bicriteria subroutine 的 \(k\)-依赖转换为 optimal tree radius \(r\)-依赖，配合 RecApprox-\(d\) 得到 CSM/DCSM 的 \(\Omega(\varepsilon^3/r^\varepsilon)\) 可行近似，及 DRCSM 的 \((\Omega(\delta\varepsilon^3/r^\varepsilon),1+\delta)\) bicriteria 近似。结论是 strong value-oracle 模型下的理论 guarantee；根问题允许尺寸超预算，且没有无线、机器人、疫情或基因网络的实证结果。

## 方法与证据

- CSM 输入 undirected \(G\)、non-negative monotone submodular \(f\)、整数 \(k\)，选 \(k\)-edge tree；DCSM 改为 directed out-tree，DRCSM 还固定 root。paper 以 edge count 表示 size，等价 vertex formulation 的对应为 \(k'=k+1\)（§1--2）。
- \(r\) 是最优 undirected tree 的 center-to-farthest-vertex radius；有向版本是 optimal out-tree 的 height。\(r\le\lceil k/2\rceil\)（undirected）和 \(r\le k\)（directed），但 \(r\)/center 属于 optimal solution 的未知参数，不是输入直接提供的运营量（§1--2）。
- Theorem 1.1：对每常数 \(\varepsilon\in(0,1]\)，(Directed) CSM 有 polynomial-time \(\Omega(\varepsilon^3/r^\varepsilon)\)-approximation。该表达是 value ratio lower bound，非“误差为 \(r^\varepsilon\)”；小 \(r\) 才带来更强保证（§1）。
- Theorem 1.2：DRCSM 对 \(\delta\in[1/k,1]\) 有 bicriteria \((\Omega(\delta\varepsilon^3/r^\varepsilon),1+\delta)\) approximation。第二坐标意味着输出可有最多 \((1+\delta)k\) edges；不是严格预算/容量可行（§1、§2）。
- GreedyRadius 以 root/radius guess 和 (\(\alpha(k),\beta(k)\)) DRCSM subroutine 反复加入有价值 out-subtrees；Theorem 3.1 将其转换为 \((\frac12\alpha(r),4\beta(r))\) bicriteria。随后 CSM/DCSM 可 partition/trim 回可行解，DRCSM 则通过 trimming 导出 \(1+\delta\) violation result（§3）。
- RecApprox-\(d\) 递归 greedy，Theorem 4.4 给 bicriteria \((1/(d+1),(d+1)2k^{1/d})\)（PDF 排版形式）并以 \(d=\lceil1/\varepsilon\rceil\) 产生总体 \(\varepsilon\) 依赖。\(\varepsilon\) 是 constant 才保持 polynomial runtime；更小 \(\varepsilon\) 改善 \(r\) 指数但提高递归/常数代价（§4、§5）。
- 算法通过 **strong value oracle** 查询 \(f\)，即允许对 feasible 和 infeasible sets 求值；复杂度只按 value-oracle queries 计，未计将实际 coverage/epidemic/genomics objective 构造成精确 oracle 的数据/计算成本（§2）。
- 对 CSM 的 hardness 讨论仅给出因 cardinality case 而无法优于 \(1-1/e\) 的 NP-hardness；作者说缺少更有信息量的 CSM hardness。论文未声称 approximation factor tight，未来工作是无 size violation 的更强 \(k/r\) 近似和 hardness（§1、§5）。
- 全文为算法/证明工作，没有 synthetic benchmark、真实网络、wireless/UAV/robot/epidemic/genomics 数据、runtime comparison 或 deployment study（§1、§5）。所列领域是 CSM modelling applications，不是已验证应用表现。

## 适用边界与复现

- 适用于能合理给出 graph connectivity 和可精确/可审计 value oracle 的 offline combinatorial design。真实节点/边可能有概率故障、动态容量、方向/时延、成本异质性、多个连通分量和不满足单调 submodularity 的相互作用，均会破坏定理输入条件。
- 预算严格时不可直接使用 DRCSM bicriteria result；必须选择可行 CSM/DCSM variant或先批准 \(1+\delta\) 资源超额并重新评估。\(\delta\) 小同时降低 value guarantee，工程上应报告该 trade-off。
- 不能将“radius-sensitive”解释为算法知道实际最优布局半径或在 small-world graph 自动高质量。实施需要说明 how guesses/enumeration are made、实际树半径/预算和 oracle errors；最优 radius 估计错误会影响可选方案/运行开销。
- 无线/无人机/卫生/癌症应用还需独立建模 stochastic propagation、coverage measurement、collision/flight constraints、隐私/公平、因果关系和人类/法规要求。submodular proxy value 最大化不保证这些领域的安全、治疗效果或公共卫生效益。
- 复现应固定 graph/direction/root、\(k,r\) definition、oracle implementation与所有 queried sets、\(\varepsilon,\delta,d\)、subroutine/partition/trimming/guess enumeration、runtime/oracle-query accounting和随机/并列处理；应补充 empirical scaling、exact small-instance optimum、budget violation和 objective sensitivity。

## 与 AAMAS 的关系与核验说明

这是 graph optimization 与 submodular maximization 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/IPZQ7320.pdf) 核对 CSM/DCSM/DRCSM 定义、radius、Theorems 1.1--1.2、GreedyRadius/RecApprox-\(d\)、strong value-oracle和 bicriteria条件/未来工作；没有把理论近似或应用动机误写成真实网络、机器人、卫生或基因数据的部署验证。
