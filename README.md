# AI 学习法（hualun-ai-learning-accelerator）

> 一个让 AI 当你「一对一私教」的 Agent Skill：费曼教学法 + 误区库 + 知识地图 + 进度不丢 + 间隔复习。
> 作者：**AI训练师花伦**　·　版本 3.4.0　·　MIT 许可

## 它能做什么

你说「开始学习」，告诉它想学的学科、作者或书名，它会：

1. **找书、拆书**：把教材每一章拆成「章节结构 / 类比库 / 误区库」三件套，讲课只依据书里的内容，不瞎编。
2. **像老师一样一对一地教**：先抛一个让你困惑的生活现象 → 用类比搭桥 → 再给精确定义 → 举例 → 追问边界。一次只讲一个概念。
3. **换着形式讲**：有顺序的画流程图，讲关系的画关系图，有数值的做能拖滑块的互动网页；听不懂还能做一段 1–3 分钟的**动画讲解视频**，5 岁小孩都能听懂（ELI5）。
4. **真的考你**：每小节一道一道出题，考的是迁移和反例，不是背定义。
5. **记住进度**：断在哪、哪里错过，都写进文件，下次说「继续」接着来。
6. **帮你复习**：每章生成复习卡和笔记，按 1 / 7 / 30 天安排复习。

## 怎么用

这是一个 Agent Skill（`SKILL.md` + `references/` 细则 + `scripts/` 脚本），可放进支持 Skill 的 AI Agent（如 Claude Code、Codex、Hermes）的 skills 目录使用。

常用说法：

| 你说 | 它做 |
|---|---|
| 开始学习 / 继续学习 | 列出进行中的课题，或从断点继续 |
| 学经济学 / 学《经济学原理》 | 找书、拆章节、开讲 |
| 太难了 / 听不懂 | 换类比 → 视觉图解 → 讲解视频或寓言 |
| ELI5 / 说人话 | 切到最简单的讲法 |
| 做个视频讲讲 | 生成当前概念的动画讲解视频 |
| 复习一下 / 抽卡复习 | 按复习队列出题 |

## 文件结构

```
SKILL.md          主流程和铁律（先读）
references/       按场景读取的细则（教学步骤、讲解形式、章节收尾、复习……）
scripts/          路径解析、复习卡生成等小脚本
templates/        互动练习页模板
CHANGELOG.md      版本历史
companion-skills/ 配套 Skill（仅 GitHub 仓库里有，见下）
```

## 配套 Skill 与安装

学习法的核心（找书拆书之外的讲解、考核、记进度、复习）单独就能用；下面这些让它更完整。把需要的文件夹和学习法一起放进你的 Agent 的 skills 目录即可。

### 本仓库自带（`companion-skills/`）

| Skill | 在学习法里做什么 | 缺了会怎样 | 另需安装 |
|---|---|---|---|
| `hualun-book-distillation-workflow` 找书蒸馏 | 找教材、把每章拆成「章节结构 / 类比库 / 误区库」，讲课只依据书 | 只能用 AI 通用知识讲，不保证贴着原书 | 无（微信读书接口可选，需自己的 `WEREAD_API_KEY`） |
| `hualun-explainer-video` 解释视频 | 「做个视频讲讲」：1–3 分钟动画讲解，5 种风格（王虹手写、3B1B、复古、像素、白板马克笔） | 没有视频，其他讲解形式照常 | 见下方「解释视频的软件」 |
| `hualun-local-tts` 本地配音 | 给解释视频配旁白 | 解释视频做不了 | `pip install edge-tts`（免费、需联网）；克隆本人声音为可选，需自行部署 VoxCPM2 并设 `VOXCPM_DIR` |

**解释视频的软件**（都免费、本地运行）：

```bash
brew install ffmpeg
python3 -m venv ~/.venvs/learning-video && ~/.venvs/learning-video/bin/pip install manim   # 4 种 Manim 风格
mkdir -p ~/.venvs/whiteboard-video && cd ~/.venvs/whiteboard-video && npm init -y && npm i playwright-core hanzi-writer-data hersheytext && npx playwright-core install chromium-headless-shell   # 白板马克笔风
```

目前只在 macOS（Apple 芯片）上实测过。公式排版另需 TinyTeX（可选，没有公式用不到）；像素风需要开源「缝合像素字体」Fusion Pixel。字体与路径细节见 `companion-skills/hualun-explainer-video/SKILL.md`。配音脚本默认放在 `~/.hermes/skills/hualun-local-tts/`，放在别处时改 `explainer.py` 里的 `SPEAK` 与 `prepare_audio.py` 里的 `TTS_SKILL`。

### 第三方 Skill（请到原作者处安装）

| Skill | 在学习法里做什么 | 缺了会怎样 |
|---|---|---|
| [女娲 nuwa-skill](https://github.com/alchaincyf/nuwa-skill)（花叔） | 学一本书前，蒸馏出作者的思维框架、常用例子和误区，讲课带「作者视角」 | 讲课只靠 AI 通用知识和书本身 |
| [show-me](https://github.com/charlie947/show-me) | 难点做成能拖、能点的互动网页；章节结束生成互动复习卡 | 只用文字和简单图表讲，复习卡不是互动版 |
| [obsidian-skills](https://github.com/kepano/obsidian-skills)（kepano） | 按 Obsidian 格式写学习笔记（双链、属性） | 笔记照写，只是少了 Obsidian 专属格式 |

### 笔记存哪

学完每一节会写一份 Markdown 笔记，默认存到 `~/Documents/Obsidian Vault/LLM Wiki/wiki/学习/AI学习/`。**没装 Obsidian 也可以**：笔记是普通文本文件，任何编辑器都能打开；想换位置就设环境变量 `LEARNING_VAULT=/你的文件夹`，笔记会放在它下面的同样结构里。

## 说明

- 部分能力依赖其他 Skill（见上方「配套 Skill 与安装」），没有时会退化为纯对话教学。
- 文件里的路径（如 `~/.hermes/learning/`、`~/Documents/Obsidian Vault/`）是作者本人的环境，使用前按自己的目录调整。

## 许可

[MIT](LICENSE) © 2026 AI训练师花伦
