# 参考文件总表

> 由 SKILL.md 3.0.1 原文整段迁出（2026-09-28 压缩），规则原样保留；冲突处已按主 SKILL.md 统一。

### 依赖

**写入使用当前可用的 Obsidian CLI 或文件工具，并遵守限定写入合同；不要假定旧 `obsidian` 别名一定存在。完整依赖清单（必需/可选 + 降级路径）见 `references/dependencies.md`。**

**本地书籍下载辅助**：`references/archive-download-proxy.md` — archive.org + Project Gutenberg 代理配置、可用的 Spinoza 资源 identifier（Gutenberg #3800 Elwes 译本）、下载命令模板。

**电子书宝库集成**：`references/ebook-treasure-chest-integration.md` — GitHub 电子书宝库搜索/下载流程，支持 epub/mobi/azw3 格式，来自帆书、微信读书、京东读书、喜马拉雅等平台。

**微信读书集成规则**：`references/weread-learning-integration.md` — 新书学习时优先用微信读书官方 Skill 获取中文目录骨架；不默认抓公开点评/热门划线；抓不到再回退本地教材蒸馏；只用 `/book/chapterinfo` 时必须透明说明这不是逐页原文蒸馏。

**微信读书 API 模式**：`references/weread-api-patterns.md` — 实测记录：书架接口是 `/shelf/sync` 不是 `/shelf/list`；业务参数必须平铺到 body 顶层；常见错误和修复方法。

**用户学情档案构建**：`references/user-profile-building.md` — 从微信读书获取阅读数据，分析知识领域，生成用户学情档案，用于教学中的类比选择和基础判断。

**经济学教材辨析**：`references/economics-textbook-clarification.md` — 区分曼昆《经济学原理》和萨缪尔森/诺德豪斯《经济学》，以及综合教材中微观/宏观章节边界的回答模板。

**经济学教材消歧**：`references/economics-textbook-disambiguation.md` — 区分曼昆《经济学原理》和萨缪尔森/诺德豪斯《经济学》；说明共同内容、风格差异、微信读书目录骨架 vs 正文蒸馏的透明边界。

**用户学情档案**：`references/user-knowledge-profile.md` — 跨学科用户知识档案系统：微信读书自动获取、学习反应词识别、教学节奏调整。

**运行时落地细节**：`references/runtime-workflow.md` — Obsidian 主库、教材路径优先级、章节复习图生成、每日复习 cron 的简明操作细节。

**信息图式章节复习图**：`references/infographic-mind-map-rendering.md` — 使用用户本地 `生图-信息图.md` 提示词、HTML/CSS/SVG → PNG 兜底、中文字体/配色约束、视觉核验与防截断规则。

**文章型学习 / RAG 入门参考**：`references/article-based-rag-primer.md` — 用户粘贴长文并要求“小白教学”时的轻量教学节奏、RAG 概念顺序、常见误区、以及结束时生成唯一章节复习图 + Obsidian 学习记录 + state.md 的闭环。

**教学提问设计**：`references/teaching-question-design.md` — 图形/曲线/坐标轴类问题必须先给 SVG/PNG，或改成现实语义题；避免让用户脑补“右上/右下”等抽象图形方向。

**苏格拉底追问误用实录**：`references/socratic-misfire-tool-teaching-20260801.md` — 实操类教学（工具操作/工作流）被错误使用哲学式态度追问的翻车案例。记录正确的 B 路径边界验证问法与 A/B 分流规则。

**编号极简答案处理**：`references/numbered-compact-assessment.md` — 用户用 `1 小 2买方 3上升` 等极简格式回答考核时的解析、判定与章节收尾核对清单。

**飞书图片发送模式**：`references/feishu-image-delivery-patterns.md` — Cron job 输出中 `MEDIA:/path` 格式成功发送图片的模式、直接回复中的已知失败路径、排查步骤。

**扫描版 PDF 的 OCR 提取**：`references/ocr-pdf-extraction.md` — 当 pdfplumber 提取返回空时，用 Tesseract OCR 提取文字；含安装命令、提取代码、目录定位技巧。

**书籍下载注意事项**：`references/book-download-workflow.md` — 下载前确认方向/版本、中文优先偏好、代理配置、版权教材处理。

**Memento 闪卡集成（可选）**：`references/memento-flashcards-integration.md` — 官方 `memento-flashcards` skill 的安装验证、卡片读写命令、以及接入每日复习 cron 的边界。Memento 只能作为原子记忆卡/轻量复习补充，不能替代 `state.md` 作为书籍进度、章节状态、误区、知识地图和 Obsidian 笔记的事实源。接入 AI 学习每日复习 cron 前必须获得用户明确同意；cron 只提醒到期卡片，不在自动任务里开始问答。

**抽卡复习工作流**：`references/draw-card-review-workflow.md` — 用户说「抽卡复习」时，先查 Memento 到期卡；为空则回退到 AI 学习 `state.md` 复习队列抽取到期项，只出一题，答后判定并更新状态。已合并原 draw-card-review-routing.md。

**学习知识卡 PNG 渲染**：`references/learning-card-png-rendering.md` — SVG 源文件 → Playwright 固定尺寸 HTML wrapper → 截图 PNG；含无滚动条/无截断/中文路径坑的核验与兜底。

**用户学情档案模板**：`references/user-profile-template.md` — `user-profile.md` 的标准模板：学习偏好、已学学科表、反应模式表。

**教学节奏与考核纠偏**：`references/teaching-pace-and-assessment-correction-2026-05-20.md` — 2026-05-20 用户纠偏实录：有基础用户概念调速（一句话点过）、考核不词面送分、章节收尾由助手直接输出总结（原记忆宫殿已废弃）。
