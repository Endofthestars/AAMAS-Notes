---
title: "Toward Recognizing Social Media Recommenders Under Absent Recommendations: A Graph Neural Network-Based Approach"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "safety_verification", "agent_engineering"]
dblp_key: ""
doi: "10.65109/YMXQ7472"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YMXQ7472.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03y"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "recommender-auditing", "synthetic-proxy-data", "identifiability", "social-impact"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Toward Recognizing Social Media Recommenders Under Absent Recommendations: A Graph Neural Network-Based Approach

## 一句话总结

SM-ARR-G 把“无推荐日志时识别平台推荐器”表述为候选 infosphere 的模型选择：分别在每个假设推荐器下训练 GNN 行为预测器，选择 held-out 负对数似然最低者作为最可能的生成机制。

## 方法与证据

- 任务输入只有观测到的用户交互；对候选推荐器 $R$ 模拟 exposure/infosphere，并以 $R^*=\arg\min_R L(\hat\theta_R;D_{test},R)$ 选择解释。完整边缘对行为的概率需对隐式推荐边缘与 $R$ 边缘化，实际以 hindsight predictive model 近似（§2）。
- 先学习尽量不依赖隐藏推荐器的 recommender-neutral user model（RNU），再在已知候选推荐器下合成交互；在每个候选下从头训练两层 HGT 做 link prediction，采用五折交叉验证、BCE、Adam 和 OneCycleLR（§2–3）。
- 使用 DBLP Citation Network V14 作为社交网络代理（逾 5M papers、36M citations）。报告的 LightGCN 生成真值实验中，LightGCN 候选的 NLL 为 $0.0900\pm0.0579$、准确率为 $0.9836\pm0.0113$，优于所列其它 infosphere（表 1）。

## 适用边界与复现

- 关键证据来自合成数据和学术共著/引用网络代理，且 ground-truth simulation 仅限下一年仍活跃作者；这尚不能证明能在真实、动态、带广告和策略干预的社交媒体上辨认闭源排序器，也存在多机制不可辨识风险。
- 复现须固定时间切分、RNU/hindsight 构造、六种 infosphere 的参数、活跃作者筛选、负采样和每折随机种子；外部审计还需预注册候选族、稳健性/混合推荐器检验、隐私合规与不确定性阈值，避免把低 loss 直接认作因果归因。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/YMXQ7472.pdf) 人工核对似然选择准则、HGT 设置、DBLP 代理和表 1；该文是 extended abstract，文中也将真实世界扩展列为未来方向。
