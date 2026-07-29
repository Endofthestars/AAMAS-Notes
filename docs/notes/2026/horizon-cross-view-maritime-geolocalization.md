---
title: "Horizon Based Cross-View Geolocalization in Maritime Environment"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["robotics_embodied", "agent_engineering", "safety_verification"]
dblp_key: ""
doi: "10.65109/YIUE1134"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YIUE1134.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02w"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "dem_accuracy_dependence", "restricted_search_area", "four_log_evaluation", "no_navigation_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Horizon Based Cross-View Geolocalization in Maritime Environment

## 一句话总结

该文为 GNSS 受限的无人水面艇提出被动视觉定位：离线从 DEM 渲染候选地平线并训练 ResNet18+GeM siamese descriptor，机载端以 50° 相机图像做最近邻检索，再以 particle filter 过滤候选。四个测试日志、约 25 km² 搜索区中，最佳测试集的平均位置误差为 37.39 m，最佳平均航向误差为 7.38°；它要求已知大致工作区域和可用、准确的 DEM，不能从中推断在开阔海域、恶劣能见度或真实航行控制中可安全替代 GNSS。

## 方法与证据

- 离线从 topographic DEM 生成密集数字地平线，CNN descriptor 以欧氏最近邻检索匹配；Monte Carlo particle filter 据此抑制离群并连续估计位置。机载只保留模型和 descriptor database，减少在线计算（§2、图 1）。
- 使用 ResNet18+GeM，探索 256 以下的 descriptor dimensions；各网络相同数据/超参训练 10 epochs，以 weighted soft-margin triplet loss 按地理坐标相关性构造训练 triplet（§2）。
- 系统假设已大致知道运行区域以限制 DEM 搜索。测试为四个完整日志，按遮挡、观察距离、天气排序，使用 5,000 particles、200 simulations；表 1 的平均 position error 为 57.78/37.39/62.54/89.14 m，平均 heading error 为 7.38/18.17/14.24/16.05°（sets 0--3）（§3、表 1）。
- 文中“38 m、8°”分别来自不同表现最佳项，非同一 test set 的成对指标；图 2 所示 particle filter 在一个场景三次迭代附近收敛、遮挡帧段仍跟随真值（§3--4）。

## 适用边界与复现

- 适用于沿岸、可获得最新 DEM 且能预先限定区域的 GNSS-denied 辅助定位；DEM 高程误差、潮位、海平面/地平线可见性、镜头标定、天气、浪、船姿态和陆地遮挡都会破坏匹配。
- 未知起点是在 25 km² 受限搜索空间内，非全球无先验定位；50° FOV、日志选择和训练/描述符库决定真实可辨识性，视觉相似海岸可能产生多峰错误假设。
- 位置误差和航向误差不等于碰撞风险、航线可执行性或 spoofing/jamming 下的完整韧性。论文没有报告实时帧率、失锁/重捕获率、海试规模或与 GNSS/radar/INS 的安全融合。
- 复现应公开 DEM 版本、渲染采样/高度/姿态、相机内外参、搜索范围、日志/天气切分、网络/descriptor/索引、particle filter 噪声与 seed；报告全分位误差、置信度/拒答、失锁、跨海岸泛化和受控遮挡/DEM 变化测试，再与多传感器故障安全导航比较。

## 与 AAMAS 的关系与核验说明

该文研究嵌入式自主海事系统的被动感知定位。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/YIUE1134.pdf) 人工核对 DEM+descriptor+particle-filter 流程、50° FOV、四日志协议和表 1；未把限定区域的视觉检索结果表述为 GNSS 的通用安全替代。
