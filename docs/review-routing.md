# 模型审核路由

本仓库默认采用 **Spark 双通道、Terra 风险升级**。目标是让 80%–90% 的模型工作量
由 `GPT-5.3-Codex-Spark` 完成，并把 `GPT-5.6 Terra` 的使用限制在需要更强判断的
关卡。`GPT-5.6 Sol` 不再自动调用，只在用户明确要求时使用。比例是长期路由目标，
不得以降低证据标准为代价。

## 每篇论文的默认流程

1. **Spark S1：结构化草稿**
   - 读取原论文；
   - 提取研究问题、方法、主要结果、比较、局限和复现信息；
   - 每个数值结论必须定位到节、表、图或论文页码。
2. **Spark S2：独立反向 QA**
   - 使用新的临时会话；
   - 不读取 S1 的推理过程，只读取原论文和待核验笔记；
   - 专门检查事实、数值、页码、因果表述、过度泛化和核验范围。
3. **一致性关卡**
   - S1 与 S2 结论一致、证据完整且没有升级条件时，可直接进入 `reviewed`；
   - 任一 Spark 返回 `uncertain`、证据缺失或核心结论冲突时，不得自动放行。
4. **Terra 风险升级**
   - 只处理触发条件对应的争议片段，不默认重新通读整篇；
   - Terra 无法裁决时，状态保持 `note_draft` 或 `hold_for_human`。

## Terra 触发条件

- S1 与 S2 对核心方法、结果方向或局限的判断冲突；
- 关键数值、阈值、样本量或效果量没有精确正文证据；
- 核心主张涉及形式化证明、安全边界、因果推断、伦理或高风险部署；
- 正文、图表、附录或不同权威来源互相冲突；
- 滚动质量抽样：每累计 10 篇由 Spark 双通道放行的笔记，抽取 1 篇交给 Terra。

除非用户明确提高预算，Terra 的长期工作量目标为 10%–20%。如果风险触发会让某批
超过该范围，优先把未裁决项目置为 `hold_for_human`，而不是静默增加 Terra 用量。

## 不使用 Terra 的任务

- 候选论文初筛；
- 元数据规范化、主题分类和重复检测；
- 正文分段、表格抽取和引用定位；
- 笔记初稿、格式修复和 front matter 补全；
- 第一轮事实 QA；
- 已通过验证规则的机械更新。

## `reviewed` 最低门槛

- 原始来源可访问，并记录官方 URL；
- Spark S1 与 S2 均完成；
- 方法以及主要结果已经定位到正文证据；
- 实证论文核对主要比较与局限；理论论文核对定义、定理条件、构造与边界；
- 记录 `review_route`、`risk_level`、`escalation_model`、`escalation_reason`、
  生成模型、审核模型和日期；
- 未完成的复现、附录、代码版本或原始数据检查必须明确列出；
- 仓库验证器和测试通过。

`reviewed` 代表声明范围内的来源证据已核验，不代表人类专家签字或独立实验复现。

## 失败与升级

| 情况 | 处理 |
|---|---|
| Spark 输出格式失败或超时 | 用新 Spark 会话重试一次 |
| 第二次仍失败 | 保持 `note_draft`；仅在风险预算内升级 Terra |
| S1/S2 核心结论冲突 | Terra 定点裁决，或 `hold_for_human` |
| Terra 与来源仍冲突 | `hold_for_human`，不得标记 `reviewed` |
| 抽样发现实质错误 | 回退受影响批次，修订提示词并重新执行 S2 |

## 推荐 front matter

```yaml
note_status: "note_draft"
review_route: "spark_dual_pass"
review_batch: ""
spark_draft_verdict: ""
spark_qa_verdict: ""
spark_consistency: ""
risk_level: "low"
risk_tags: []
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: ""
reviewed_at: ""
```

已有笔记保留其真实历史路由。若历史上使用过 Sol，其 `escalation_model` 必须继续
记录为 `gpt-5.6-sol`，不得追溯改写为 Terra。
