---
title: "Game-Theoretic and Algorithmic Analyses of Multi-Agent Routing under Crossing Costs"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "game_theory_mechanism", "marl_coordination"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KETH5148.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02n"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "asynchronous_timing_not_modeled", "crossing_cost_proxy", "complexity_result_scope", "no_empirical_robot_evaluation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Game-Theoretic and Algorithmic Analyses of Multi-Agent Routing under Crossing Costs

## 一句话总结

该文提出 Crossing Cost Multi-Agent Routing（CC-MAR）：在混合图中让各智能体自主选路，并以同一无向边上反向通行人数的乘积衡量潜在迎面冲突，而非强制同步避碰。模型总有纯 Nash 均衡、最优解也是均衡（PoS=1），但一般均衡求解为 PLS-complete、零 crossing-cost 判定为 NP-complete；论文给出若干参数化算法。它适合分析异步路线的冲突风险代理指标，不能替代带时间、动力学和安全距离约束的 MAPF/机器人验证。

## 方法与证据

- 输入是带无向边 \(E\) 和有向弧 \(A\) 的加权混合图，以及 \(k\) 对起点--终点。每个智能体选择一条路径；对无向边 \(\{u,v\}\)，总成本累计 \(w_{uv}x_{uv}x_{vu}\)，即两方向使用数的乘积。相同方向共用边不产生该项成本（§2）。
- 作者将此非标准成本写成拥塞博弈。纯策略 Nash 均衡总存在；任何全局最小成本策略组都是 Nash 均衡，故 Price of Stability 为 1，而构造实例显示 Price of Anarchy 无界（§3、表 1）。
- best-response dynamics 在至多 \(w_{max}k^2m\) 步收敛，其中 \(w_{max}\) 是最大权重、\(m=|E|\)。当边权受输入规模多项式界定时可多项式时间求均衡；一般权重下求均衡为 PLS-complete（§3）。这些是离散路径选择的渐近复杂度结论，不给出具体路网规模下的运行时。
- 对优化问题，零 crossing-cost 是否存在推广 Steiner Orientation，因而为 NP-complete。文章还概述：按终端对数 \(k\) 有 XP 算法；按边数 \(|E|\)、按 \(|A|+k\)、按 \(|A|+\mathrm{diam}(G)\) 均有 FPT 算法；无权情形下还有以 vertex cover 与终端结构为参数的 FPT 结果（§3、表 2）。
- 该 AAMAS 版本为 3 页扩展摘要，完整证明与细节指向作者引用的 arXiv 完整版；本文笔记只据摘要中明确陈述的模型、界与复杂度分类，不补写未展示的算法细节。

## 适用边界与复现

- CC-MAR 的“冲突”是未定时路线的迎面相遇风险代理；它没有表示到达时间、等待、顶点碰撞、速度/动力学、通信、任务优先级或实际碰撞概率。零成本也不等价于真实执行安全。
- 适用于窄通道双向流、通信受限车队或多机器人路线的离线风险分析，可与时间扩展 MAPF、容量约束和重规划结合；若直接下发路线，仍需独立的时序安全层。
- PoA 无界意味着单纯自利选路可非常低效；部署时不应仅依赖均衡存在性，应明确全局目标、激励/协调规则和最坏情形保护。
- 复现理论结论应实现混合图、反向流计数和路径成本，以小实例枚举验证势函数/最优解即均衡，再按 \(k,|E|,|A|,\mathrm{diam}(G),vc\) 分层生成实例，分别记录最优成本、均衡成本、best-response 步数和求解资源。还应与时间化 MAPF 在同一场景比较真实冲突、延迟和吞吐；摘要没有提供这类实证评测。

## 与 AAMAS 的关系与核验说明

该文位于多智能体路径规划、协调和算法博弈交叉处。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KETH5148.pdf) 人工核对 CC-MAR 的反向边成本、均衡/PoS/PoA 结论、收敛界及表 2 的参数化分类。PDF 页脚显示的 DOI `10.65109/ICRJ7770` 已被官方目录另一篇不同论文使用；为避免传播这一冲突标识，元数据 DOI 暂留空。
