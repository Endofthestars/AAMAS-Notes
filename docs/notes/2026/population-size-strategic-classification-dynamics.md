---
title: "Population Size Effects on Strategic Classification Dynamics"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "human_agent_interaction", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/CKRS7125"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKRS7125.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["stylized_payoff_model", "binary_user_types", "small_mutation_limit", "population_parameter_sensitivity", "fairness_metric_scope", "high_stakes_deployment_gap"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Population Size Effects on Strategic Classification Dynamics

## 一句话总结

本文用有限群体 evolutionary game 与稀有 mutation 极限的 Markov chain，分析用户和机构在 strategic classification 中的共同适应。模型显示：当中等阈值机构的分类器可被伪造时，长期常见状态可让好用户承担适应成本、坏用户伪造；缩小机构群体在所给参数下会使不利用户状态更常出现，但总体影响并非单调，且理想化的 manipulation-proof classifier 也不能自动消除这种风险。这是参数化机制模型的长期分布分析，不是对真实信贷/招聘系统公平性、准确性或因果效果的保证。

## 方法与证据

- 作者设机构群体、Good 用户群体和 Bad 用户群体三类有限 population，机构策略为 Medium/High threshold；Good 用户可 Not adapt/Adapt，Bad 用户可 Fake/Improve（§2）。它把 true 与 observable feature、接受收益、伪造/改善成本压缩为二元类型、二元策略和固定 payoff；不直接估计真实特征分布、模型误差、申诉、法律约束或群体保护属性。
- baseline 中 Medium 对 Fake 的 Bad user 给 false positive；robust scenario 仅改变该格，使 Medium 识别 Fake 为 true negative（Eq. 5–8）。所谓 manipulation-proof 是这一个结果矩阵中的理想设定，不等于已实现并审计过的防操纵 ML，亦不代表无法发生其他攻击、误报、歧视或分布漂移。
- 行为更新为同类个体 pairwise imitation：较高 payoff 的策略以 logistic 概率更易被模仿，selection strength 为 \(\beta\)；以小概率 \(\mu\) mutation 使链 ergodic（Eq. 12, §2.4）。在 small-mutation limit，作者把完整 \((N_I+1)(N_G+1)(N_B+1)\) 状态空间近似为八个 homogeneous states，以 fixation probability 构成 reduced Markov chain，再计算 stationary distribution（Eq. 13–17）。因此结果依赖 rare mutation、well-mixed interaction、长期平稳、策略固定和近似是否成立。
- 在 imperfect classifier 下，HAF（High、Good Adapt、Bad Fake）对整个参数空间有强鲁棒性：好用户为接受而付出成本，坏用户会被拒；当 Good 用户比例满足给定阈值时，MNF 也可能稳健（§3, Fig. 2）。这描述该 payoff 结构下的演化方向，不能推出实际个人一定会撒谎、机构一定会提高门槛，或任意分类器的均衡行为。
- 对 \(N_I=N_G=N_B=100\)、论文所用 \(\rho=15,\lambda=50,b=50,c_F=1,c_I=5,\beta=0.02,N=300,p_G=0.5\)，imperfect case 的 HAF 是唯一 prevalent state；在 robust case，MNI（Medium、Good Not adapt、Bad Improve）为唯一 prevalent state（Fig. 3A）。这些是特定参数/初始模型的 stationary probabilities，不是普适的 accuracy 或 welfare 排名。
- 将总人数保持为 300、机构降至 10 时，作者报告 imperfect 情形变化不大，但 robust 情形中 HAF 约有 14% 的长期占比；性能未明显变而 social cost 上升（Fig. 3B）。机制是小机构群更容易 fixation，同时该群产生的 mutation 更少；两种效应相互竞争（§3）。
- 扫描机构人数时，imperfect setting 的 HAF prevalence 在约 \(N_I\approx30\) 达到峰值，因此人口规模效应非单调；robust setting 中理想 MNI 随 \(N_I\) 降低的下降约在 \(N_I\approx20\) 后出现（Fig. 5）。图中的“约”来自一组固定参数与 reduced-chain computation，不能当成跨行业的机构数阈值。
- 作者以 true-positive 与 true-negative rates 之和定义 accuracy，以 Good users Adapt 的平均比例表征 social cost，并考察 social-cost/accuracy ratio（Fig. 3, 6）。这不是通常完整的公平性审计：未报告不同受保护群体的错误率、individual fairness、可解释性、拒绝伤害、债务/就业后果或分布外稳健性。

## 适用边界与复现

- 适用于提出和比较 strategic-classification 的机制假设：明确谁能观察/伪造什么、阈值和收益成本、用户组成、mutation/learning rule 与时间尺度，再把有限群体随机性纳入长期分析。它更适合压力测试“机构数量不重要”这类假设，而非直接为部署选阈值。
- 高风险场景中不应据此认定缩减机构数量、采用某类阈值或声称“防操纵”就会提高公平性。部署前还需以真实数据做漂移与行为验证、分组与交叉分组公平审计、反事实/因果评估、隐私与安全审查、申诉和人工复核、持续监测，并遵循适用的信贷/就业等法律责任。
- 可复现路径是实现 Eq. 5–12 的 payoff 与 imitation process，按 Eq. 14–17 求各 mutant fixation probability 和八态 transition matrix，解 \(v=v\Lambda\)，复画 Fig. 2–6，并对 \(N_I,N_G,N_B,\rho,\lambda,b,c_F,c_I,\beta,\mu\) 做敏感性分析；应同时模拟非稀有 mutation 的完整链，检验 eight-state approximation。
- 后续可加入连续特征和策略、异质/网络互动、非固定人口、有限观察与学习、多个机构类型、经验校准 payoff、群体公平指标、动态再训练及干预/申诉机制。论文也明确把连续策略、靠近 decision boundary 的用户和不同 selection intensities 列为扩展方向（§4）。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 关于 strategic classification、evolutionary multiagent dynamics 与社会技术系统的研究。笔记根据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/CKRS7125.pdf) 核验了二元机构/用户策略、payoff 修改、imitation-plus-mutation Markov model、small-mutation eight-state reduction、Fig. 3–6 的参数化观察及结论中的局限；没有把模型的 stationary-state 结果写成真实高风险分类系统的公平、性能或防操纵认证。
