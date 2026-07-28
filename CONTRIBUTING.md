# 贡献与审核

## 添加或修改笔记

1. 不要手工修改 DBLP/IFAAMAS 可提供的题目、作者、年份、DOI 或官方标识。
2. 从 `templates/paper-note.md` 创建笔记。
3. 所有数值结论都注明对应表格、图或章节。
4. 将“论文明确陈述”“我们的解释”“尚未确认”分开书写。
5. `reviewed` 状态至少需要核对方法、主要实验、基线和局限四部分。

## Pull Request 检查

- [ ] `python3 scripts/validate_repository.py` 通过
- [ ] 没有重复 `dblp_key`、DOI 或笔记路径
- [ ] 未提交论文 PDF 或未经许可的大段原文
- [ ] 自动生成内容明确标为草稿
- [ ] `reviewed` 状态包含核验人和核验日期
