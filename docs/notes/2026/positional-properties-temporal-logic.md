---
title: "Positional Properties in Temporal Logic"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["argumentation_reasoning", "game_theory_mechanism", "safety_verification"]
dblp_key: ""
doi: "10.65109/ULIK5622"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ULIK5622.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05j"
spark_draft_verdict: "source_grounded_draft_with_theory_direction_error"
spark_qa_verdict: "needs_revision_corrected_for_star_free_direction_page_map_and_scope"
spark_consistency: "pass"
risk_level: "medium"
risk_tags: ["doctoral_research_program", "theorem_without_proof_in_short_paper", "omega_star_free_direction", "state_edge_label_scope", "incomplete_prefix_independent_characterisation", "citation_vs_contribution_boundary", "sl_sg_state_local_dependency", "no_model_checker_or_benchmark"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_theorem_direction_page_mapping_resource_semantics_and_contribution_boundary_check"
escalation_verdict: "pass_after_star_free_direction_page_scope_and_future_work_corrections"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted logic-boundary check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Positional Properties in Temporal Logic

## 一句话总结

这篇 Doctoral Consortium 文稿研究何时可把 ATL* 与 Strategy Logic 中依赖历史或完整策略的语义限制为 positional 或 state-local semantics，而不改变相关片段的含义；它报告所有 positional \(\omega\)-regular languages 都是 \(\omega\)-star-free、state/edge-labelled 模型间的一步观测记忆关系，以及 \(SL\text{-}[SG]\) 的逐状态依赖结果，但完整刻画、近似算法、扩大逻辑片段和工具实现仍未完成。

## 问题与术语边界

文稿讨论 non-terminating multi-agent systems 的 temporal-logic semantics。ATL* 与 Strategy Logic 的公式通过 agents 或 coalitions 是否存在可强制某个 temporal goal 的策略来解释；限制策略可用的 memory 或 dependence，可能缩小策略空间并改善推理性质，但也可能改变语义（p. 4050）。

这里几类概念不能互换：

- **memoryful strategy** 可依赖已经历的状态历史；
- **positional strategy** 只按当前 state 指定 action；
- **finite-memory strategy** 允许有限内部记忆，不等同于 positional；
- **bipositional** 与 **half-positional** 是关于双方或其中一方能否用 positional winning strategy 的目标语言分类。

论文把一组 infinite words 称为 positional，当它作为任意 graph game 的 winning condition 时，只要 player 1 有 memoryful winning strategy，就也有 positional winning strategy（p. 4050）。

## State-labelled 与 edge-labelled 不是同一语义

许多 infinite-game 结果把 observations 放在 edges 上，而 temporal logic 通常把 observations 放在 states 上。同一 property 的 positionality 会受该表示差异影响（pp. 4050–4051）。

作者报告：在 state-labelled models 上 positional 的 properties，转到 edge-labelled models 后，为获得 optimal play 至多需要记住 previous observation（p. 4051）。这不是说两类模型具有相同 positional semantics，也不是说任意 state-labelled positional property 在 edge-labelled model 中仍然 memoryless。

## Positional language 的报告结果

### \(\omega\)-star-free 的方向

Theorem 2.1 明确写为（p. 4051）：

> All \(\omega\)-regular positional languages are \(\omega\)-star-free.

因此方向是

\[
\text{positional } \omega\text{-regular}
\subseteq
\omega\text{-star-free}.
\]

文稿同时指出 LTL path formulae 只表达 \((\omega\)-)star-free languages，而这种表达力**足以**覆盖所有 positional \(\omega\)-regular languages。该结论不能反写成 LTL/star-free 不足以覆盖这些 positional languages。

作者还报告：

- 将 positional languages 与研究 star-free languages 的 algebraic techniques 对齐，可为某些 game subclasses 得到 necessary and sufficient conditions；
- 给定识别 language 的 Wilke algebra，这些条件较易检查；
- CTL 加入 \(\exists(GF\varphi_1 \land FG\varphi_2)\) 的 fragment 被更强的、加入 \(\exists G(\varphi_1 U \varphi_2)\) 的 CTL fragment 包含，二者所用 path formulae 都是 positional；
- 存在 prefix-independent path formulae 不能编码成 Rabin condition（p. 4051）。

三页稿没有给 Theorem 2.1、Wilke-algebra conditions 或这些 fragment claims 的证明细节。

## 引用背景不能并入本文新贡献

以下主要以 known result 和引用文献出现（pp. 4050–4051）：

- parity games positionally determined；
- positional-for-both-players、single-player positional 与 half-positional languages 的既有 characterisations；
- \(\omega\)-regular languages 恰是 infinite graphs 中可用 finite memory optimally play 的 objectives；
- prefix-independent bipositional languages 可表达为 finite-colour parity winning conditions；
- half-positional Muller conditions 可表达为 Rabin conditions；
- ATL 只允许 \(X\varphi\)、\(\varphi_1 U\varphi_2\)、\(\varphi_1 R\varphi_2\) 等受限 path formulae，并具有 positional semantics；
- ATL+ 虽可包含 non-positional path formulae，但引用工作 [13] 给出 ATL+ 与 ATL 的表达力等价。

最后一项只支持 ATL+/ATL 的具体等价关系：不能泛化为任意 ATL* 或 Strategy Logic formula 都能换成 positional equivalent。

## Strategy Logic 的依赖范围

在一般 Strategy Logic 中，existentially quantified strategy 可能依赖其 scope 内的 universal strategies，包括对未来或 counterfactual plays 的选择。既有 behavioural semantics 限制这种依赖：在 history \(\pi\) 上，\(\sigma(\pi)\) 只看相关策略沿当前 path 已选择的 moves。文稿引述已有结果称，只允许 disjunctive 或只允许 conjunctive path-formula combinations 时可保持 behavioural dependence，而一般 Boolean combinations 会破坏它（p. 4051）。

作者针对 \(SL\text{-}[SG]\) fragment 报告更强的 state-local finding：

- 该 fragment 允许 alternating quantifier blocks 后接单一 temporal operator；
- strategies 可 pointwise on states 定义；
- 只允许 positional strategies 时语义仍等价；
- strategy 在 state \(q\) 的 action 只依赖其他 in-scope strategies 在同一 \(q\) 的 actions；
- 因而每个 state 可视为一个 discrete game，并可借助 effectivity functions 把 concurrent game models 转到 neighbourhood models（p. 4051）。

这是该 fragment 的局部依赖结论，不等同于 full Strategy Logic 具有 positional semantics，也不意味着 unrestricted visibility、完整历史依赖或所有 model-theoretic 问题已解决。

## 未完成工作

作者明确说，目前尚无 \(\omega\)-regular、prefix-independent positional languages 的完整 characterisation。Positionality 是 non-local property，且不对普通 LTL operators 良好组合：两个 positional properties 的 disjunction 可能不是 positional（p. 4051）。

Future Work 包括：

- 寻找更自然的 prefix-independent positional LTL fragment；
- 用 \(\psi_1 \rightarrow \phi \rightarrow \psi_2\) 形式的 simpler positional formulae 为复杂公式给 upper/lower approximations；
- 通过 syntactic transformations 转到已知 positional 的 ATL* fragment；
- 寻找更大的 Strategy Logic fragments，使其具有 state-based 或 behavioural dependence；
- 在 effectivity models 上复用 completeness 等 model-theoretic constructions。

这些是研究方向，不是已经实现的 model checker、approximation algorithm、complexity improvement 或 completeness result。

## 证据与复现边界

该三页文稿没有提供 theorem proofs、完整 formal syntax/semantics、algorithm、pseudocode、implementation、runtime、memory use、dataset、benchmark、quantitative evaluation 或 code。它支持的是精确的定理/发现陈述、与既有文献的关系以及博士研究计划，不能据此声称已交付 tractable verification tool。

## 页码与核验说明

PDF 逐页核对：p. 4050 为摘要、Introduction 和 Positional Properties 开端；p. 4051 为 state/edge-labelled finding、Theorem 2.1、algebraic/fragment results、Strategy Dependency 与 Future Work；p. 4052 仅为 References。

笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/ULIK5622.pdf) 核对定理方向、资源语义、引用/贡献边界与研究阶段；`reviewed` 不表示未展示的证明、完整 characterisation、复杂度算法或工具已经完成。
