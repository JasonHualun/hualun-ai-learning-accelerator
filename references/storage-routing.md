# 个人学习存储路由

先读 Vault `LLM Wiki/AGENTS.md` 的个人学习合同。本页只提供路径解析，不覆盖教学、考核、复习提醒或发送授权。

## 用法

```bash
python3 ~/.hermes/skills/hualun-ai-learning-accelerator/scripts/learning_paths.py
python3 ~/.hermes/skills/hualun-ai-learning-accelerator/scripts/learning_paths.py --subject "经济学" --course "微观经济学" --chapter "第六章"
```

工具仅返回规划，不写入、不建目录。先调用默认模式检查首页和规则入口。课程的 `--subject` 是“学习与知识”内的实际分类，例如 `经济学`、`控制论`、`AI与Agent/设计模式`，不是一律 AI与Agent；先复用现有学科。

旧会话或 state.md 给出历史路径时，用 `--legacy "<完整旧路径>"` 查获批迁移映射。解析成功后读 `resolved`；解析失败应报告缺口，不能创建旧目录，也不能重新教已通过章节。旧 Raw 卡片继续只读引用，不搬动。

## 每次写入前后

1. 核对 state.md 与已有章节笔记；路径工具的 `note_exists` 和实际文件存在时先读再更新，保持原 id、来源、privacy/scope。
2. 新笔记按实际学科创建；记录稳定 id、课程、章节、来源与来源完整度、updated、privacy: scoped、scope: [personal/learning]。通过考核的概念与外部未经实测的主张分开。
3. 同一章节的 HTML/PNG 复习卡保持原命名，Vault 副本写到工具返回的 cards_dir，本地副本仍在该课程 progress-assets。笔记直接使用工具返回的 card_html_link 与 card_png_link（已编码的 Vault 相对链接）关联卡片，不能沿用旧 `../知识卡/` 相对地址。文件真实存在后才加链接。
4. 同步专门学习首页的简短状态与对应学科索引；不覆盖“学习与知识/00-入口.md”的其他内容。新文件只在有实际内容时创建，不先建空目录。
5. 校验笔记与卡片存在、链接可解析、原 state.md 仍是断点真源，再追加 log；不得因路径迁移修改过去考试结果或声称未完成的章节已经完成。

新收藏的外部原文或 Skill 走 Capture；本学习会话已经产出的章节笔记按限定个人学习合同写入，不重复提交小助手。


个人学习笔记由本Skill直接维护，不进入小助手队列；授课与本人理解混合页使用 identity: ai、creation_mode: co-created、topics: [学习与知识]、type: learning-note、uses: [个人学习]，明确分节作者。只有逐字原话区可当本人表达。外部教材来源按统一合同外部身份保存；学习断点/成绩不变。
