---
title: "The Multi-Agent Off-Switch Game"
conference: "AAMAS"
year: 2026
track: "research"
topics:
  - "safety_verification"
  - "game_theory_mechanism"
dblp_key: ""
doi: "10.65109/HQQZ1937"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/HQQZ1937.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_draft_escalated_full_spark_qa"
risk_level: "high"
escalation_model: "gpt-5.6-sol"
escalation_reason: "full_verification"
escalation_verdict: "pass"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "Codex (GPT-5.6 Sol)"
reviewed_at: "2026-07-28"
---

# The Multi-Agent Off-Switch Game

## 一句话总结

论文把单智能体 off-switch game 扩展到多智能体共同收益博弈：可加联合效用会保留个体可纠正性，但非可加交互能够让各自愿意接受人类干预的智能体出现群体不可纠正均衡。

## 研究问题与设定

单智能体可选 `act`、`wait` 或 `off`；选择 `wait` 后，人类以温度参数
\(\beta\) 的 softmax 策略在执行与关闭之间决策。智能体对行动效用持有概率信念。
多智能体版本令 \(n\) 个智能体同时选择策略，以组合函数 \(f\) 表示多项行动共同发生
时的共享效用。

论文的群体可纠正性要求：

1. 全体选择 `wait` 是纯纳什均衡；
2. 在每个纯纳什均衡中，每个智能体都弱偏好 `wait`，而非直接行动或关闭。

个体可纠正性则在“其他智能体均关闭”的诱导单智能体游戏中判断。

## 方法

- 先分析高斯信念 \(B=\mathcal N(\mu,\sigma^2)\) 下的单智能体可纠正区间。
- 对两智能体写出完整期望收益矩阵，分别研究可加与非可加组合函数。
- 可加情形利用 soft-average 的平移/分解性质证明等待偏好在对方任一策略下保持。
- 非可加情形把一个智能体的条件可纠正性化为其行动的边际贡献
  \(z=f(u_1,u_2)-u_2\) 是否满足单智能体可纠正条件，并用构造与均衡图展示失效。

## 实验与证据

本论文是理论工作，没有数据集实验；证据由定理、收益矩阵和构造示例组成。

| 结论 | 证据位置 | 核验状态 |
|---|---|---|
| 高斯信念下，当且仅当 \(|\mu|\leq \sigma^2/(2\beta)\) 时智能体可纠正 | Theorem 1，论文 p.6 | 已核对公式与边界 |
| 群体可纠正性同时约束全等待均衡及所有纯均衡 | Definition 2，p.6 | 已核对定义 |
| 可加效用保持个体可纠正性；严格个体可纠正时全等待是唯一纯均衡 | Theorem 2，pp.9–10 | 已核对定理条件与结论 |
| 可加情形中，个体可纠正是群体可纠正的充要条件 | Corollary 2，p.10 | 已核对 |
| 条件可纠正性取决于行动相对其他行动的边际贡献 | Proposition 1，p.10 | 已核对 |
| 非可加函数可产生额外的不可纠正均衡区域 | Figure 2、Theorem 3，p.11 | 已核对存在性结论；未外推为所有非可加函数 |

## 主要贡献

1. 给出 multi-agent off-switch game 与群体可纠正性的正式定义。
2. 证明可加共同效用下可纠正性的组合性质，并说明该结论可扩展到 \(n\) 个智能体。
3. 用边际贡献原则解释非可加交互为何会改变等待激励。
4. 把 AI 可关闭性从单体属性提升为需要分析均衡与交互外部性的系统属性。

## 局限与威胁

论文明确限定或留作未来工作的部分：

- 详细的非可加分析采用两智能体、同时行动和不可通信的静态博弈；
- 只有一个人类 principal，未处理多 principal 的利益与协调；
- 决策时信念固定，没有建模观察、沟通或在线更新；
- 更多非可加组合函数的图只声明将在扩展版给出，当前论文未提供完整附录。

我们的额外判断：

- 纯纳什均衡不能描述混合策略、学习动态或均衡选择过程；
- softmax 人类模型无法覆盖系统性偏差、操纵或不同监督者；
- 没有代码和数值复算材料，理论复核依赖手工重建公式与矩阵。

## 与 AAMAS 研究方向的关系

它把对齐与可关闭性问题写成多智能体机制和均衡问题，直接连接
`safety_verification` 与 `game_theory_mechanism`。对 PaperCompass 的价值在于：
判断多智能体安全机制时不能只验证单个智能体，还要检查联合收益、外部性和全部均衡。

## 复现信息

- 官方 PDF SHA-256：`a371fdb08521ae906cd96af8898753b1c00d1b3ce7e61314c8e2804f3b2a929c`
- DOI：<https://doi.org/10.65109/HQQZ1937>
- 代码：论文未报告
- 数据：不适用；属于理论分析
- 可复核对象：Theorem 1–3、Proposition 1、Table 1–2、Figure 1–2
- 当前核验级别：`SOURCE_METHOD_RESULTS_LIMITATIONS_VERIFIED`

## 核验说明

Spark 负责首次结构化阅读；复核阶段重新检查了官方 PDF 的定义、定理条件、图表和
Discussion，并删除了草稿中把存在性结果泛化到所有非可加函数的风险表述。尚未完成
独立形式化证明或数值脚本复算。
