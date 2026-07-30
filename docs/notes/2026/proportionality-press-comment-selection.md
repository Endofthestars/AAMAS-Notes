---
title: "Proportionality Press: Illustrating Proportionality through Comment Selection"
conference: "AAMAS"
year: 2026
track: "demo"
topics: ["game_theory_mechanism", "resource_allocation", "norms_trust_governance", "human_agent_interaction", "safety_verification", "applications"]
dblp_key: ""
doi: "10.65109/XVUL7166"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XVUL7166.pdf"
demo_url: "https://youtu.be/G6JhDP97TCo"
app_url: "https://simon-rey.github.io/ProportionalityPress/"
code_url: "https://github.com/Simon-Rey/ProportionalityPress"
data_url: "https://github.com/compdemocracy/openData"
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05s"
spark_draft_verdict: "source_grounded_with_required_high_risk_taxonomy_spelling_and_scope_corrections"
spark_qa_verdict: "needs_revision_corrected_for_risk_level_topics_spelling_and_deployment_fairness_boundaries"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["political_comment_visibility", "minority_inclusion_popularity_tradeoff", "subjective_relevance", "no_fairness_ground_truth", "no_user_study", "no_polarization_outcome", "no_deployment_evaluation", "ballot_incompleteness_unhandled", "data_consent_privacy_and_provenance_unreported", "strategic_manipulation_unstudied", "transparency_and_appeal_governance_unreported"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_public_discourse_visibility_representation_fairness_provenance_manipulation_and_deployment_boundary_check"
escalation_verdict: "needs_revision_corrected_for_static_demo_fairness_evidence_public_discourse_and_governance_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted public-discourse and fairness-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Proportionality Press: Illustrating Proportionality through Comment Selection

## 一句话总结

Proportionality Press 把真实 pol.is 讨论转换为多赢家投票示例，用静态网站并列展示 popularity、representation 与 inclusion 导向规则选出的评论；它是教学与外展演示，不是已部署的评论排序干预，也没有验证形式化公平性、代表性真值、用户理解或去极化效果。

## 系统定位与边界

网站模仿新闻站点，把真实讨论数据组织成 article、comments 与 thumb votes，并让访客比较不同 voting rules 的选择结果（p. 4104）。

作者把主要用途定位为：

- outreach activities；
- teaching computational social choice；
- 让非技术用户直观看到规则之间的取舍。

页面由 Python 脚本生成，是静态展示站；论文没有报告其接入真实平台、改变线上评论可见性或执行生产排序。因此，这项工作不能被描述为 deployed moderation、真实用户 intervention、deployment A/B test 或已验证的 governance mechanism。

## 从在线讨论到多赢家投票

映射关系为（p. 4104）：

- 一次 pol.is poll 对应一篇 article；
- comments 对应 alternatives；
- thumbs-up / thumbs-down 对应用户 preferences；
- 每种规则从 comments 中选择固定大小 \(k\) 的 subset。

网站呈现的是不同 committee-selection objectives 的结果。它展示 popularity、proportionality 与 inclusion 如何互动，但没有给出一个外部 fairness ground truth，因而不能把任一规则称为现实意义上的“公平答案”。

## ABC、TBC 与七类规则

Approval-based committee voting（ABC）只使用 thumbs-up；trichotomous-based committee voting（TBC）同时使用 thumbs-up 与 thumbs-down。论文主要讨论 ABC，并说明 TBC 使用 PAV、MES 与 Phragmén 的推广版本（pp. 4104–4105）。

ABC setting 提供七种标准规则（pp. 4104–4105）：三种 default rule families 是 AV、MES、CC；四种 additional rules 是 SAV、Sequential PAV 与两个未命名的 Phragmén variants。

- Approval Voting（AV），页面标签为 Popularity-Based Selection；
- Method of Equal Shares（MES），页面标签为 Representation-Based Selection，并提供：
    - MES with approval-voting completion；
    - MES with increment completion，网站默认使用该 completion；
- Chamberlin–Courant（CC），页面标签为 Inclusion-Based Selection；
- Satisfaction Approval Voting（SAV）；
- Sequential Proportional Approval Voting（Sequential PAV）；
- Phragmén rule variant 之一，三页稿未给出具体名称；
- Phragmén rule variant 之二，三页稿未给出具体名称。

MES 的两个 completion 是同一 rule family 的实现选择，不另计为 additional rules；两个 Phragmén variants 各计一项，因此总数仍与论文所述 seven standard rules 一致。本笔记不补写三页稿未披露的 Phragmén 名称。

## Popularity 与 inclusion 指标

Popularity score 定义为（p. 4104）：

- ABC：入选 comments 的 approval scores 之和；
- TBC：入选 comments 的 approvals 减 disapprovals，即 net support。

Inclusion score（文中也称 CC score）统计获得正 satisfaction 的 voters：

- ABC：至少批准一条入选 comment；
- TBC：对入选 comments 的 approvals 数严格多于 disapprovals 数。

这些是论文选择的操作化指标。较高 inclusion 不自动等同于群体公平、观点质量、事实正确性、长期满意度或降低极化。

## Operation Marching Orders 示例

作者用 `Operation Marching Orders` 数据集、\(k=5\) 比较规则（p. 4105）：

- AV 选出的五条热门 comments 都围绕 policy issues；
- MES 用一条关于 Trump 人格与 impeachment 的 comment 替换 AV 中最不热门的 policy message；
- 替换进来的 comment 获得的 approvals 约少 10%；
- inclusion 从 AV 的 66% 上升到 MES 的 71%；
- CC 达到 79% inclusion。

作者同时形容 CC 结果看起来更随机、明显不那么热门。这里的“随机”或“less relevant”只是作者的定性观察，不是论文定义的 relevance metric 或经过人类评测的质量结论。

在 20 个 datasets、\(k=5\) 的汇总中，AV 与 MES 在 10/20 个 datasets 产生相同结果；CC 每次都与 AV/MES 不同，并常被作者判断为选择了较不相关的 comments（p. 4105）。该汇总没有报告不确定性、显著性检验或对 \(k\)、ballot missingness 与规则参数的 sensitivity analysis。

## 实现与复用

实现流程包括（p. 4105）：

1. 从公开的 [pol.is openData](https://github.com/compdemocracy/openData) 取得数据；
2. 清洗并转换为 PrefLib 格式；
3. 通过 `abcvoting` 计算 ABC 规则，通过 `trivoting` 计算 TBC 规则；
4. 使用 `jinja` 与 Python scripts 生成静态页面。

作者称实现模块化，可替换数据与规则。公开资源包括 [网站](https://simon-rey.github.io/ProportionalityPress/)、[代码](https://github.com/Simon-Rey/ProportionalityPress) 和 [演示视频](https://youtu.be/G6JhDP97TCo)。

## 本稿没有验证什么

三页 demo 没有报告：

- 用户理解、可用性或认知负担研究；
- 公平性或代表性的外部 ground truth；
- 对 echo chamber 或 polarization outcome 的因果影响；
- 真实平台部署或线上 A/B test；
- 对 \(k\)、缺失投票、噪声或规则选择的 uncertainty / sensitivity analysis；
- 对 strategic voting、brigading 或 coordinated manipulation 的鲁棒性。

Ballot incompleteness 的主动处理被列为 Future Work，不是当前版本已实现能力（p. 4105）。

## 高风险公共讨论与治理边界

若把同类规则用于真实公共讨论，committee selection 会直接决定哪些政治表达被看见。更高 inclusion 可能让更多 voters 至少看到一条支持的 comment，却也可能牺牲 aggregate popularity；这是一项显式取舍，不是少数声音一定得到实质公平待遇的证明。

三页稿没有说明：

- pol.is 数据的 consent、privacy、再发布与 provenance 治理；
- 如何处理虚假、骚扰、有害或低质量但能优化目标函数的 comments；
- 战略操纵、刷票、身份重复与协同放大的检测；
- 规则、目标、参数和选择结果如何向受影响用户解释；
- comment 被遗漏或降权后的申诉、复议和审计机制；
- 谁有权决定 \(k\)、规则与 inclusion/popularity 的权重。

因此本笔记将其标为高风险：这是对潜在真实部署后果与治理缺口的披露，不表示当前静态教学站已经实施这些高风险决策。

## Future Work 与页码核验

作者计划加入更多 datasets，并实现能主动考虑 incomplete ballots 的规则（p. 4105）。

PDF 逐页核对：p. 4104 为 identity、Abstract、Introduction、在线讨论映射、规则与指标起点；p. 4105 为规则续述、Operation Marching Orders、20-dataset 观察、实现、Conclusion 与 Future Work；p. 4106 为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/XVUL7166.pdf) 核验；`reviewed` 不表示公平性、代表性、评论质量、用户理解、去极化或部署效果已被验证。
