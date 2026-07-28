---
title: "Feature-based Uncertainty Model for School Choice"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/KGWC6399"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KGWC6399.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["theoretical_model_scope", "preference_distribution_elicitation", "independence_assumption", "stability_probability_not_welfare", "computational_intractability", "no_empirical_deployment_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Feature-based Uncertainty Model for School Choice

## 一句话总结

论文为 school choice 引入 feature-based preference uncertainty：学生对每所学校在每项 feature 的效用明确，但 feature weights 是仅学生知道的随机变量；学校对学生有确定严格偏好。它以“随机权重实现后 matching weakly stable 的概率”(ProS) 为目标，并刻画该目标与不同强度学生侧 incentive compatibility 的理论冲突。HERF-proposing-order 的 generalized DA 可保证紧的 \((1/n)^n\) 最坏 ProS 近似，所有列出顺序规则都仅保证最弱 IC-C；这不是实证录取机制，也不能直接推出真实公平、福利或无操纵。

## 方法与证据

- instance 包含学生/学校、容量、学校对学生的 strict deterministic ranking、features、每位学生每 feature 对学校的 \([0,1]\) utility，以及该学生 simplex 上 feature-weight vector 的分布 \(\mu_s\)。不同学生的 \(\mu_s\) 被假设独立，pdf/cdf 可常数时间计算；所有学校彼此可接受（§3）。
- 给定 sampled weights，学生对学校按 feature utilities 的线性加权和排序；matching 的 ProS 是该 matching 在随机 student aggregated preferences 下 weakly stable 的概率。block 需要学生严格改善且学校有空位或更偏好该学生（§3，Defs. 3.1--3.2）。ProS 是稳定事件概率，不是学生 welfare、access equity、录取满意度、学校质量或群体公平指标。
- 学生可以 misreport utilities 与 weight distribution。IC-A 禁止任何有机会的改善，IC-R 禁止“新分配更好”的概率大于 \(1/2\)，IC-C 仅禁止 certainty improvement；强度为 IC-A \(\Rightarrow\) IC-R \(\Rightarrow\) IC-C（§3，Def. 3.3）。
- 即使仅两 features，求 ProS 最大 matching 也是 NP-hard（Theorem 4.3）。IC-A 只有总输出不变的机制才能满足；IC-R 与任意正的最坏 ProS approximation 不兼容，即使 \(|F|=2\)（Prop. 4.4、Theorem 4.5）。
- 更强的 trade-off：在 \(|F|=2\)，任何 IC-C 且 \(\alpha\)-optimal 的算法不能超过文中给出的指数上界；因此“抗策略操纵”与“高稳定概率”不可同时无代价取得（Theorem 4.6）。
- 论文比较 generalized student-proposing DA 的四种提议次序：LOCV、LOICV、HERF（higher expected ranking first）、HEUF（higher expected utility first）。LOCV/LOICV/HEUF 的 ProS worst-case ratio 为 0；HERF 保证 \((1/n)^n\)-optimal，且该界在两 feature 已紧（Table 1、Theorem 6.1--6.3）。该比率随学生数指数恶化，不能理解成强的实用近似保证。
- 四种规则都满足 IC-C；LOICV 在 \(|F|=2\) 时满足 IC-R。HEUF 只在两 feature 且首 feature weight 的 mean=median（概率两侧各 \(1/2\)）这一特定条件下满足 IC-R；\(|F|\ge3\) 时 IC-R 除非恒定输出一般不可得（Theorems 6.4、6.6--6.7，Cor. 7.6）。
- 对给定 matching，\(|F|=2\) 时可多项式计算 ProS；feature 更多时需算高维 half-space probability，通用积分体积为 #P-hard，连 LOCV/LOICV/HERF 的计算也可能不可行（Prop. 4.2、§7.2）。有限-support 离散分布或低维特定分布族才是作者讨论的较可计算情形。
- 论文为理论工作，没有真实 applicant/school 数据实验、福利/公平评测、behavioral misreport study 或上线部署评估（§1、§8）。

## 适用边界与复现

- 适用于确实可把择校偏好分解为可测 features、且愿意/能够 elicitate 每名学生的 feature utilities 与不确定 weight distribution 的机制分析。学生的 feature utility、分布、独立性、线性补偿和 deterministic school ranking 都是强建模假设；现实偏好可有非线性、相关、家庭/地域约束、信息不对称及随 policy/signaling 改变的内生不确定性。
- “报告分布”本身是战略对象。IC-C 只排除**确定**改善，不排除有正概率、甚至不超过 1/2 的获益操纵；所以不能对申请者宣称完全 strategy-proof。应说明采用哪一层 IC，并通过可验证的 preference elicitation、audit、appeal 与信息披露降低误报和分布估计误差。
- ProS 最大化不等于教育机会公平。部署还需独立检查群体机会/录取率/等待时间、student welfare、校方容量和资格约束、protected attributes 与反歧视规范、distributional robustness、privacy 和政策合法性。
- 由于 \((1/n)^n\) 会迅速变小，HERF 的理论非零比不能单独作为大市场设计理由。应在实际规模上比较稳定率、welfare、regret、操纵收益分布、计算时间和受扰动 distributions 下的敏感性，并与现行 DA/tie-breaking/lottery 机制共同评估。
- 复现需固定 utilities normalization、feature definitions、capacity/college rankings、\(\mu_s\) family/support/independence、tie/weak-block definition、各 proposing order、exact/approximate ProS calculation、\(n,m,|F|\)、solver/runtime 与随机种子；对多 feature/continuous distributions 报告积分/近似误差及无法计算的实例。

## 与 AAMAS 的关系与核验说明

这是 uncertain-preference matching 与 mechanism design 工作。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KGWC6399.pdf) 核对模型假设、ProS/IC 定义、NP-hardness与不可能性、Table 1、HERF 的紧 \((1/n)^n\) 界、两 feature 的特殊 IC-R 条件以及高维 #P-hard 计算限制；没有把稳定概率理论或 IC-C 误写为真实录取公平、福利最优或完全防操纵保证。
