---
title: "TAXI2: Joint Pairing and Vehicle Assignment for Two-Passenger Shared Taxis"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["resource_allocation", "planning_scheduling", "agent_engineering"]
dblp_key: ""
doi: "10.65109/RVZN9394"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RVZN9394.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03q"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "snapshot-optimality", "free-flow-travel-time", "soft-deadline", "nyc-simulation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# TAXI2: Joint Pairing and Vehicle Assignment for Two-Passenger Shared Taxis

## 一句话总结

TAXI2 不先配客再派车，而是以一个 ILP 同时选择可行双乘客 pair 和车辆任务，目标在未服务罚项下最小化 vehicle-hours travelled。作者在约 24,000 条 NYC 高峰请求、2,000 辆容量二车辆的 rolling snapshot 模拟中，在 20--50% 时间 slack 下均报告 100% 服务率；该结果依赖 flexible-service 与 free-flow 路网假设。

## 方法与证据

- Phase 1 依据起终点和 earliest departure/latest arrival，在两种 pickup order 下生成可行 pair，得到 match graph；Phase 2 ILP 将每车分给一名 solo rider 或一个 pair，并计入空驶 repositioning 与未服务罚项（§2.1–2.2）。
- 约束保证每名 rider 恰为 unserved、solo 或 pair 之一，每车最多一次 assignment，pair 不重复/不反向重复；pair cost 为可行服务顺序的最小 route cost（§2.2）。
- 系统在 rolling windows 下以当前请求和车辆状态做 snapshot-optimal 决策，采用 eager dispatch，已在车上的乘客需保持连续性（§2.3）。
- NYC 08:00--09:00 Manhattan 约 24,000 requests、约 4,500 nodes、2,000 随机初始位置的双容量车；Java/MiniZinc/Gurobi。Table 1：20/30/40/50% slack 时均 service 100%，VHT 依次 1853/1661/1578/1536，solve time 37,295/67,046/106,919/140,080 ms；更大 slack 也降低 delayed rider 比例/平均延迟（§3）。

## 适用边界与复现

- 核心假设为两人容量、预计算 free-flow travel time、snapshot optimality、可容忍小延迟和随机初始 fleet；实际拥堵、取消、司机行为、公平服务、能源约束和软硬时间窗会改变可行性与运行时间。
- 复现要发布 NYC 过滤规则、路网与速度、rolling-window 长度、fleet initialisation、配对生成、未服务罚项、Gurobi/MiniZinc 参数、硬件/超时以及按区域/等待时间的服务分布。作者亦指出 hard deadlines 会显著增加复杂度。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/RVZN9394.pdf) 人工核对 ILP、实例规模和 Table 1；未将离线/模拟 snapshot 的 100% 服务率外推为城市实时运营承诺。
