# CHANGELOG

## 3.4.0（2026-10-06）配套 Skill 一起发布、笔记位置可自定义

- GitHub 仓库新增 `companion-skills/`：自带找书蒸馏 `hualun-book-distillation-workflow`、解释视频 `hualun-explainer-video`（2.0.0，新增白板马克笔风：汉字按真实笔顺一笔一笔写）、本地配音 `hualun-local-tts`，下载学习法不再缺块
- README 新增「配套 Skill 与安装」：每个依赖做什么、缺了会怎样、怎么装；女娲、show-me、Obsidian 等第三方 Skill 只放原作者链接
- `learning_paths.py` 支持环境变量 `LEARNING_VAULT`：没装 Obsidian 也能把笔记存到任意文件夹（笔记是普通 Markdown）

## 3.3.0（2026-10-05）讲解形式与解释视频

- 新增 `references/teaching-formats.md`（讲解形式唯一真源）：讲新概念时按类型主动选流程图 / 关系图 / 互动网页 / 文字类比，不再只在卡住时才用视觉手段
- 接入共享 Skill `hualun-explainer-video`：用户要求或章节收尾同意后，后台生成 1–3 分钟解释视频（ELI5 深度、老师口吻、王虹手写风、本地配音），存 `progress-assets/解释视频/YYYY-MM-DD-主题/`
- 新触发词「ELI5」「说人话」「做个视频讲讲」；卡住升级顺序改为：换类比 → 视觉范本 → 解释视频或寓言
- `teaching-steps.md` 原视觉范本段落迁入 `teaching-formats.md`，原处只留指向
- 文件夹与运行时入口改名为 `hualun-ai-learning-accelerator`（正式名不变）
- 未采用：ASD-STE100（与正文蒸馏模式「定义照搬原文」冲突）
- 公开发布：MIT 许可，新增 README.md、LICENSE；文件内本机用户路径统一改为 `~`、代理地址改为占位符，`learning_paths.py` 改用 `Path.home()`

## 3.2.0（2026-09-28）互动练习页

- 新增 `references/interactive-practice.md` 与 `templates/practice-template.html`：跨章综合/用户要练习时生成手机练习页，做完复制答题码粘贴回来，按 PID 对回原题判分并写误区与复习队列
- 结果回传方式按用户决定为复制粘贴（不启用 webhook、不做飞书卡片）

## 3.1.0（2026-09-28，压缩版副本，待试课后替换）

- 主 SKILL.md 80KB → 约 16KB：只留主流程、铁律和按场景读取表
- 细则整段原文迁到 references：teaching-steps / book-sourcing / chapter-closing / state-and-review / short-replies-and-recovery / reference-index
- 统一冲突：找书顺序（book-sourcing 顶部为准）；「会了/上过了」记为已覆盖直接前进，说"考我"才出题；章节综合题一道一道出；讲解来源分「正文蒸馏模式 / 目录骨架模式」；开场流程只保留一份；短答防串规则合并为一处；删除失效行号引用

## 3.0.1（2026-09-28）搬家与路径修复

- 从 `~/.hermes/skills/dabaodai/` 搬入 `LLM Wiki/shared/skills/`，Hermes 以软链接加载
- Wiki 路径改到现行结构：笔记 `wiki/学习/AI学习/<学科>/`，首页 `wiki/学习/AI学习/00-入口.md`，复习卡 `wiki/学习/AI学习/复习卡/`
- `learning_paths.py`：旧映射目标已移走时，在 `wiki/学习` 内按文件名找唯一匹配
- 作者 perspective 改为按名字 `skill_view` 查，不再指向不存在的 `skills/learning/`
- 删除不存在的 `fable-teaching-method` 依赖，寓言规范以本 skill 为准
- 并入 `feynman-teaching-system`：独有的教学质量红线存 `references/teaching-quality-redlines.md`；「费曼学习」改由本 skill 触发

## 3.0.0（2026-08-17）开源化改造

### 新增
- **蒸馏可靠性四规则**：原文留档 + 流程兜底 + 证据列 + 原文映射表，把「蒸馏有损」从隐患变成可控特性
- `references/dependencies.md`：依赖清单（必需/可选 + 降级路径）

### 清理（去重）
- 删除重复段落：速查表、初始化流程「步骤零/步骤一」四标题打架、联网模式两段、下载分支两版、章节复习图损坏标题
- 合并重复 reference：`draw-card-review-routing.md` → `draw-card-review-workflow.md`
- 补齐 3 个 orphan reference 的索引（learning-card-png-rendering、user-profile-template、teaching-pace-and-assessment-correction）

### 脱敏（开源准备）
- 移除硬编码称呼「大哥」
- 行业场景从「直播/电商」硬编码改为读取 `user-profile.md` 可配置

## 2.x（历史）

版本历史此前记录散落，3.0.0 起规范化。
