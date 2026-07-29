---
title: "On Multiagent Online Problems with Predictions"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "marl_coordination", "safety_verification"]
dblp_key: ""
doi: "10.65109/WZRJ7594"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WZRJ7594.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "decision_theoretic_not_game_theoretic", "aggregate_others_predictor", "perfect_prediction_assumption", "random_bid_experiment", "competitive_ratio_not_welfare", "adaptive_predictions_open"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# On Multiagent Online Problems with Predictions

## 一句话总结

该文提出 multiagent online algorithms 的两预测器框架：每个 agent 分别预测自己的未来活跃期和其他人总 pledge；以多人 ski-rental 为例给出不同 prediction-quality 组合下的最优 competitive ratios，并用可调 trust 的 meta-algorithm 避免盲信预测的灾难性误差，但分析是单 agent 的 decision-theoretic competitive analysis，不建模他人会如何理性响应、共谋或操纵预测，因此不是多主体均衡、市场机制或群体福利保证。

## 方法与证据

- 每 agent 有 self-predictor（自身未来 activity）和 others-predictor（其他 agents 的 behavior）；后者在 ski-rental 实例中只预测其他人的总 pledge（§1--§2）。作者明确称其为 decision-theoretic 而非 game-theoretic：agent 不计算其他人理性 best response，只将 others-predictor 视作可能可信的黑箱；均衡版本留给 companion paper（§1）。
- Multiagent ski rental 中 \(n\) 个 agents 初始活跃、可永久失活；每日租资源成本 1，或各自 pledge 共同买价格 \(B>1\) 的 group license，pledges 总和至少 \(B\) 才获得此后免费使用，overpledge 时仍支付 pledged sums（Definition 1，§2）。每 agent 最小化自己的 competitive ratio，抽象掉支付能力、协商/转移、预算、公平、身份/违约、许可证规则及共同购买失败的现实后果。
- 无/最差 self/others predictions 下，最优策略第 1 日租、第 2 日 pledge \(B\)，ratio 为 \(B+1\)；即便 self-predictor 完美，只要 others-predictor 最差，也不能优于 \(B+1\)（Table 1、§2）。若 others predictor 完美但 self predictor 最差，最优 ratio 随其他 players’ actions 而变；两者 perfect 时 ratio 为 1。这里的“optimal”是各指定 prediction regime 的单-agent worst-case ratio，而不是总成本最小、所有人同时采用时的稳定性。
- 作者证明盲目跟随预测不 robust：即使 others predictor 完美，只要 self prediction 有误，competitive ratio 可以任意差（§2）。meta-algorithm 以 \(\lambda,\mu\in[0,1]\) 调 self/others predictor trust，在 Table 1 的四个极限情形同时达到相应 optimal ratios，并给 analytical bounds（Theorem 6 在 full version [29]）。没有给该 3 页文本中算法伪码、proof、完整 error-dependent trade-off 或预测校准方案。
- 实验不假定 rational agents，而是以 random total bids of others 产生 agent 需补的“price”（§3）。设 \(B=100\)，自身活跃期 \(T\sim[1,4B]\)，预测 \(\hat T=T+\epsilon\)（zero-mean normal noise），price 在 \([B-\lfloor zB\rfloor,B]\) 随机波动；每 \(z\) 1000 samples，报告 \(z=0,0.5,1\)（Figure 1、§3）。这只是随机 aggregate-input 下的 average ratio，不能验证 adversarial/strategic peers、相关 prediction errors、重复互动或集体 purchase formation。
- 论文认为图中表现与单 agent ski-rental with predictions 结果“qualitatively similar/acceptable”（§3）。但基线 worst-case ratio 是 101，而图是 average ratio；两者不能混作 robustness 或实际成本优势。作者还把 adaptive predictions、equilibria/Kantian equilibria、不同 decision theories和 Minority-game interaction 列为开放问题（§4）。
- 文档为 Extended Abstract，核心 theorem 细节、全表公式、meta algorithm/实验实现都指向 arXiv full version [29]；没有真实协作数据、多人 simultaneous simulation、API/ML predictor、隐私/安全、通信成本或群体 welfare/PoA 评估。

## 适用边界与复现

- 适用于研究在可明确定义的 online cost problem 中，如何将个人未来与他人 aggregate behavior 的不可靠 advice 分开，并分析 consistency--robustness 权衡；不适合直接用来决定共享订阅、集体采购、资源互助、云配额、保险或任何真实参与者的财务承诺。
- 复现需公开 full-version definitions/proofs、all predictor regimes、\(B,n,T\)/activity/pledge distributions、exact meta algorithm和 \(\lambda,\mu\)、prediction noise/correlation、random-bid sampler、1000 samples/seeds、worst-case/average ratio calculation与 per-agent costs。必须区分 offline optimum、individual competitive comparator与所有 agents 同时用算法后的 social cost。
- 应扩展到 agent policies 的 strategic response、shared/learned/adaptive predictors、prediction manipulation/poisoning、correlated/biased errors、identity/Sybil、coalition/side payment、heterogeneous budgets/values、asynchronous/departing agents、overpledge settlement和 communication/privacy costs。须同时测 equilibrium、welfare、distributional harms和 adversarial worst case，而非仅 random total bid。
- 部署时须将 prediction provenance/confidence、fallback、spending caps、opt-out、transparent group-license terms和 human approval 分离处理。较低 average competitive ratio 不能证明对预测错误、他人策略改变、收费争议或弱势参与者安全；没有 game-theoretic interaction 模型时尤其不能假设集体结果稳定。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的带预测在线算法、多人协作与竞争分析论文，且为 Extended Abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WZRJ7594.pdf) 核验 two-predictor、多人 ski rental、Table 1 四种 prediction regime、盲信不稳健、trust meta-algorithm、random-bid/1000-sample 实验与 decision-theoretic 限定；没有将单 agent competitive-ratio 理论夸写成多主体均衡、集体福利、真实预测可靠性或安全购买协议。
