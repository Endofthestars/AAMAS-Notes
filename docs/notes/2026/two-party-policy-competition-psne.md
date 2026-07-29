---
title: "Computing Pure-Strategy Nash Equilibria in a Two-Party Policy Competition: Existence and Algorithmic Approaches"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "safety_verification"]
dblp_key: ""
doi: "10.65109/RUHW5194"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RUHW5194.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "two_party_assumption", "fixed_supporter_partition", "inner_product_utility", "affine_isotone_win_probability", "gradient_no_convergence_guarantee", "not_real_election_prediction"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Computing Pure-Strategy Nash Equilibria in a Two-Party Policy Competition: Existence and Algorithmic Approaches

## 一句话总结

该文在两个党各选单位球内 policy vector、选民已分属一方且以内积评价政策、胜选概率为总效用差的 affine isotone 函数的模型下，证明一维有 closed-form PSNE、任意维也存在 PSNE，并给出 polynomial-time 的 grid \(\epsilon\)-PSNE 算法；这是一项对高度结构化两方连续博弈的存在/计算结果，不是对现实选举均衡、选民行为或政治建议的预测。

## 方法与证据

- 两党 \(A,B\) 各选 \(z_X\in S=\{z\in[-1,1]^k:\|z\|\le1\}\)；选民预先分为 supporters \(V_A,V_B\)，每人偏好向量 \(q_v\in S\)，党 \(X\) 对其 supporters 的政策效用为 \(z^\top Q_X\)（§2）。模型允许政策“benefit supporters of either party”的内积方向性，但不包含未决定选民、投票率、身份/党派转换、策略沟通、候选人质量、议题约束或异质/非线性偏好。
- 胜选概率固定为 \(p_A(z)=1/2+(z_A-z_B)^\top Q/8\)，\(p_B=1-p_A\)，party payoff 是其 supporters 的 expected utility（§2）。存在性/算法依赖这一 affine isotone rule、归一化 \(\|Q_A\|,\|Q_B\|\le1\) 和 compact domain；改为 plurality thresholds、噪声/操纵投票、非线性 win function、动态民调或多方竞争不能直接沿用结果。
- \(k=1\) 时 Theorem 1 给出 PSNE existence 和 closed-form characterisation（细节在 extended version）。\(k\ge1\) 时，由 payoff 只依赖 policies 在 \(span\{Q_A,Q_B\}\) 上的投影，转为二维 polar angles；Lemma 1 说明 best response/PSNE 都有 maximal strength \(r_A=r_B=1\)，Theorem 2 以 angular best responses 和 fixed-point arguments 证明每个维度均存在 PSNE（§3）。这不是一般 continuous game 都有纯均衡的结论。
- pseudo-gradient 在该 game 一般不 monotone，也无 \(\lambda\)-cocoercivity；因此标准 gradient convergence guarantees 不适用（§4）。作者仍报告 decaying-step projected gradient ascent 在随机 preference/initial-policy 实例中通常数千 iterations 内到 approximate PSNE，extragradient 未见一致改善；实验细节仅在完整版本，本文未给实例分布、seed、成功率/阈值或最坏例。
- 离散化算法 GBA-PSNE 在 reduced angular domain 建 uniform grid，因 pseudo-gradient Lipschitz \(L=O(\|Q_A\|+\|Q_B\|)\)，spacing \(h=\Theta(\epsilon/L)\) 能近似 unilateral deviations；Theorem 3 声明时间对 input size 与 \(1/\epsilon\) 多项式，并借一维 grid best-response unimodality 给出 \(O(nk+\epsilon^{-1}\log\epsilon^{-1})\) 实现（§5）。它保证该模型的 \(\epsilon\)-PSNE，未承诺在高维现实特征、多党或不完全信息中仍 practical/快速。
- 文档为 Extended Abstract，理论 proof、closed form、gradient counterexample 数值、算法伪码与实验完整性均指向 external extended version；没有现实选举数据、校准、反事实验证、人类受试、选民公平/代表性分析或政策伤害评估（§3--§6）。作者未来方向是 alternate isotone win functions、multi-party、partial-information learning/strategy（§6）。

## 适用边界与复现

- 可用于理论机制设计/计算社会选择研究中，分析给定两方内积效用和连续 policy action 下的均衡结构，或在受控模拟中求近似 PSNE；不应作为选举预测器、竞选策略优化器、公共政策推荐器或对真实党派/选民的行为解释。
- 复现需要提供完整版本的 proofs、\(Q_A,Q_B\)/voter generator、supporter partition、normalization、win/payoff equations、angular reduction、closed-form cases、GBA grid/\(\epsilon\)/Lipschitz constants、projected-gradient step schedule、all seeds/initializations、termination/\(\epsilon\)-PSNE checker和 runtime。应验证 theorem preconditions与数值 stability，而不只展示典型收敛轨迹。
- 应测试多党、浮动/策略性选民、投票/参与噪声、non-affine or discontinuous win rules、nonlinear/multi-issue/constraint preferences、policy feasibility/implementation costs、partial information、coalitions/misinformation、dynamic feedback和 robustness to estimation errors。需报告不存在/多均衡、cycle、boundary policies和分配/福利结果。
- 任何面向真实政治的使用必须有严格法律/伦理审查、隐私和反操纵保障、独立多学科验证与公众参与；纯策略均衡只是模型内不偏离条件，不能证明民主正当性、代表性、公平、可执行性或社会福利。不可把算法输出用于微定向说服、压制投票或自动公共资源决策。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的博弈论、政策竞争与均衡计算论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RUHW5194.pdf) 核验双党/内积/affine-isotone 模型、Theorems 1--3、二维角度归约、非单调 pseudo-gradient、经验 gradient 描述及 grid \(\epsilon\)-PSNE；没有将模型内 PSNE existence、典型随机数值收敛或 polynomial grid search 夸写为现实选举均衡、政治预测或规范性政策结论。
