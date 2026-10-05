# 依赖清单

本 skill 的依赖分「必需」和「可选」两级。必需依赖缺失时核心流程跑不起来；可选依赖缺失时有降级路径。

## 必需依赖

| 依赖 | 用途 | 缺失后果 |
|---|---|---|
| 文件系统 `~/.hermes/learning/` | state.md、材料、小节记录持久化 | 无法记录进度，skill 无法运行 |
| `hualun-book-distillation-workflow`（>= 2.8） | 本地教材蒸馏（章节结构/类比库/误区库三件套） | 无法从本地 PDF/EPUB 蒸馏，只能走联网建课模式 |
| Obsidian Vault | 学习笔记、复习图、学习首页写入 | 无法沉淀笔记，只能靠 state.md 记录 |

## 可选依赖

| 依赖 | 用途 | 降级路径 |
|---|---|---|
| 微信读书（`WEREAD_API_KEY` + `weread-knowledge-integration`） | 优先找书 + 中文目录骨架 | 无 → 本地教材目录 → Gutenberg/archive.org → 用户提供文件 |
| 飞书（`feishu-image-sender`） | 发章节复习图、发文件 | 无 → 只保存本地，不推送 |
| Memento 闪卡（`memento-flashcards`） | 原子闪卡复习 | 无 → 只用 state.md 复习队列 |
| archive.org / Project Gutenberg | 公版书下载 | 无 → 用户提供文件 |
| 生图（`image_generate`） | 章节复习图 | 无 → HTML/CSS/SVG 兜底导出 PNG |

## 环境路径

当前读写入口见 `references/storage-routing.md`（相对本 Skill 根目录）和 `scripts/learning_paths.py`。更换路径必须同时核对主 Skill、运行流程与对应教学参考中的读写地址；不能仅修改配置段就假定完整工作流兼容。教材与学习运行状态目录仍遵循主 Skill 的当前运行配置。


个人学习笔记由本Skill直接维护，不进入小助手队列；授课与本人理解混合页使用 identity: ai、creation_mode: co-created、topics: [学习与知识]、type: learning-note、uses: [个人学习]，明确分节作者。只有逐字原话区可当本人表达。外部教材来源按统一合同外部身份保存；学习断点/成绩不变。
