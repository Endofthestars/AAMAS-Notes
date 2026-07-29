---
title: "On the Trade-Off Between Transparency and Security in Adversarial Machine Learning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "game_theory_mechanism", "norms_trust_governance"]
dblp_key: ""
doi: "10.65109/HCNI3628"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HCNI3628.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "image_classification_benchmark_scope", "transfer_attack_assumptions", "defense_status_disclosure_only", "security_through_obscurity_insufficient"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# On the Trade-Off Between Transparency and Security in Adversarial Machine Learning

## 一句话总结

本文考察 transferable adversarial examples 中“是否披露 target model 受防御保护”这一最小透明信息的策略影响：攻击者若用与 target 同样防御状态的 surrogate，攻击通常更成功；因而隐藏 defense status 在该 benchmark 里可降低攻击者收益。作者用 9 种 attacks、181 个 CIFAR‑10/ImageNet models 的实证矩阵构造 Nash、Stackelberg 和 Attack‑&‑Surrogate games；结论是特定攻击/模型分布下的 disclosure trade-off，不是以 obscurity 取代可靠鲁棒训练、公开审计或用户透明度的安全建议。

## 方法与证据

- 设 attacker 选择 undefended/defended surrogate distribution \(S\)，defender 选择 undefended/defended target distribution \(T\)；defender payoff 是攻击下 expected accuracy，attacker payoff 是 \(1-u_d\) 的 accuracy degradation（§3）。这是 zero-sum distribution-level abstraction，未表达攻击成本、查询限制、adaptive defender/patching、检测/恢复、model ownership、用户伤害、不同 threat actors或 disclosure 的法律/问责价值。
- 实证评估 Admix、VNIFGSM、LGV、SSAH、BIA、OPS、PGN、CDTP、AutoAttack 共 9 attacks，在 CIFAR‑10/ImageNet、92 undefended + 89 defended models上进行（§2）。CIFAR‑10用 entire test set，ImageNet用 5,000-image RobustBench subset，metric 是全 test-set accuracy degradation；不能概括到文本/LLM、语音、tabular、physical attacks、poisoning/backdoor、prompt injection、privacy or availability threats。
- Table 1 报平均攻击后 accuracy：CIFAR‑10 的 U surrogate→U target 77.4（+71.4 degradation），D→D 20.4（+8.1）；ImageNet U→U 57.4（+33.3），D→D 32.3（+4.0）。文中称用 defended rather than undefended surrogate 攻 defended target 在 degradation increase 上最高 3.2×，而用 defended surrogate 攻 undefended target 低 4.7×（§2）。这些是跨 attacks/models平均值；defense implementations、clean accuracy、epsilon/norm、attack hyperparameters、per-model variance/CI与真实风险均未在 3 页文稿充分列出。
- Surrogate-matching game 的 Stackelberg（attacker预知 defender choice）相对 Nash 优势在 CIFAR‑10 9 attacks 中 5 个非零、平均 0.46% degradation；ImageNet 6 个、平均 0.33%（§3）。Attack-&-Surrogate game 再允许 attacker 选攻击，ImageNet expected payoff difference 0.18%，CIFAR‑10用 VNI‑FGSM 可达最大；这些小幅 game-payoff差并不能衡量现实透明机制的整体成本/收益。
- 限制 attacker 必须用 undefended surrogate 的 Attack game 相比 A&S，平均 degradation 增加为 CIFAR‑10 3.73×、ImageNet 2.15×（§3）。这支持在 transferable-attack benchmarking 加入 defended surrogates，且作者建议 defense diversification；没有证明“隐藏防御状态”对已知模型、white/black-box attacker、security testing或长期防御最优，也不应阻止必要的 vulnerability disclosure。

## 适用边界与复现

- 适合 adversarial-ML evaluation 和安全架构的 threat-model分析，提醒研究者不能只用 undefended surrogate 来估计 transferable attack potency；不适合作为公共服务系统减少解释、停止独立 audit 或以“安全”为名隐藏影响用户的 model behavior 的依据。
- 复现需锁定 181 models/weights/defense variants及来源、CIFAR/ImageNet preprocessing/subsets、九种 attack implementations/epsilon/norm/iterations/seed、clean/attacked accuracy、surrogate-target pairing、aggregation、payoff matrix与 Nash/Stackelberg/A&S solver。分 attack、dataset、architecture和defense报告置信区间，而不只给总体 mean。
- 应扩展到 adaptive/black-/white-box and query-limited attackers、new/unknown defenses、robustness under distribution shift、certified robustness、detection/recovery、ensemble/randomized defenses、physical inputs和 non-vision modalities。更重要的是比较多层防御、secure development、red-team、responsible disclosure、public documentation和用户/监管所需透明度的联合效果。
- 生产决策应区分对攻击者的敏感 operational details 与对用户/审计者必要的解释、数据/用途说明、性能和风险披露。可采用分层披露、受控安全评估、coordinated vulnerability disclosure和独立审计；不应把 secrecy 当作唯一防线，或以此规避公平、可质询和合规义务。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 adversarial ML、安全与 game-theoretic transparency analysis extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/HCNI3628.pdf) 核验 9 attacks/181 models、CIFAR‑10/ImageNet setup、表 1、三种 games、0.46%/0.33% 与 3.73×/2.15× 结果；没有将 benchmark 中的 status-obscurity benefit 写成反透明原则、通用防御或真实系统安全保证。
