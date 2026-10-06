---
name: hualun-explainer-video
description: 花伦解释视频：为任意一个概念生成 1–3 分钟、3Blue1Brown 风格的动画讲解视频（Manim 动画 + 火柴人/简笔画小剧场 + 本地配音 + 同步字幕 + 公式逐项标注），默认王虹手写风；另有白板马克笔风（网页手绘、汉字按真实笔顺一笔一笔写），全部本地免费运行。学习法（hualun-ai-learning-accelerator）讲课、复习时调用；其他 Agent 需要「把一个概念做成讲解视频」时也用它。触发词：「做个视频讲讲」「解释视频」「动画讲解」「3b1b风格」「讲解动画」「白板讲解」「手绘白板动画」。不做真人出镜、不做 AI 生成视频、不做剪辑。
version: 2.0.0
author: 花伦 (Hualun)
owner: hualun
metadata:
  watermark: hualun
  brand: 花伦
  provenance: original-user-work
---

# 花伦解释视频 2.0.0

## 原理（一句话）

AI 写分镜代码 → 一帧帧算出**无声画面**并记下每句旁白的开始秒数 → 共享语音 `hualun-local-tts` 配旁白 → ffmpeg 按秒数把每句贴回去并**逐句核对有声** → 成片。没有任何收费 API。

画面有两条路，配音、字幕、核对共用：
- **Manim 路线**（王虹手写 / 3B1B / 复古 / 像素）：`分镜.py` + `scripts/render.sh`
- **白板路线**（白板马克笔风）：`分镜.js` + `scripts/render_board.sh`。网页画白板、无头浏览器逐帧截图。Manim 做不出「笔一笔一笔写」的手感，所以单独走这条

## 依赖（都已装好，缺了先问用户，不自行重装）

| 部件 | 位置 | 作用 |
|---|---|---|
| Manim | `~/.venvs/learning-video` | 画动画 |
| TinyTeX（含 fontspec、unicode-math、lm-math） | `~/Library/TinyTeX` | 只负责 `MathTex` 公式排版，字母/数字/加减等号的字体跟随主题；没有公式用不到 |
| ffmpeg | Homebrew | 贴配音、量时长、核对 |
| 缝合像素字体 Fusion Pixel（OFL 开源） | `~/Library/Fonts/fusion-pixel-12px-proportional-zh_hans.otf` | 仅像素游戏风使用 |
| 白板路线依赖：playwright-core、汉字笔画数据 hanzi-writer-data（Arphic 开源，九千多字、真实笔顺）、单线手写英文字体 hersheytext（EMS Felix） | `~/.venvs/whiteboard-video/node_modules`（不放进 Vault） | 白板风逐帧截图、中文按笔顺写、英文数字公式单线写 |
| 无头浏览器 Chromium | `~/Library/Caches/ms-playwright/chromium_headless_shell-*` | 白板风截图 |
| 配音 | 共享 Skill `hualun-local-tts` | `edge`=Hermes 云夏（默认）；`clone`=本人克隆声音（VoxCPM2） |

## 风格（Manim 四套的唯一真源：`scripts/theme.py`；白板风在 `scripts/board/`）

| 主题名 | 叫法 | 样子 |
|---|---|---|
| `wanghong`（默认） | 王虹手写风 | 取自花伦原创共享 Skill `z-wanghong-handwritten-ppt`（灵感来自王虹获奖演讲的手写 PPT）的默认 cream 主题：HanziPen SC 手写字体（公式同字体）、暖白纸、深蓝墨水、蓝/玫红强调 |
| `3b1b` | 3B1B 深色风 | 仿 3Blue1Brown：深灰底、苹方字体、亮蓝/橙/金线条、教科书公式字体 |
| `retro` | 美式复古风 | 用户提供的美式复古配色参考：近黑底、复古黄 #FBC359 / 草绿 #73A642 / 灰蓝绿 #4B848A、红橙强调；中文兰亭特黑，公式 Futura Bold |
| `pixel` | 像素游戏风 | 用户提供的像素 RPG 海报参考：天空蓝底、米白粗黑描边像素对话框字幕、爱心红/草地绿/金币橙；全部文字和公式用缝合像素字体；左上角爱心 + Lv.1 经验条，每讲完一点弹「+1 XP」 |
| 白板马克笔风（白板路线） | 白板风 | 用户提供的 prompt-motion.com 白板讲解案例：深灰底上架一块白板；**所有内容都由马克笔写出来**——汉字按真实笔顺一笔一笔写、英文数字公式用单线手写体写、线条手画微抖，笔帽随墨水色（黑/蓝/红/绿）；标题板书式写在左上角加下划线；换内容用板擦擦（可只擦一块）；字幕在白板下方深色条 |

- Manim 四套切换：渲染前加 `EXPLAINER_THEME=retro`（或 `pixel`、`3b1b`）；新增 Manim 风格就在 theme.py 加一套，不改分镜。字体、背景、配色、**公式字体**一处改全部跟着变。
- 白板风是另一种分镜（`分镜.js`），和 Manim 分镜不能互换；见下方「白板风怎么做一集」。
- 分镜和简笔画只用语义色 `T.ink / T.c1 / T.c2 / T.key / T.accent / T.good / T.muted`，不写死颜色。

## 怎么做一集

1. **建集目录**（见下方「存放规则」），在里面写 `分镜.py`，照 `examples/supply_demand.py` 的结构：
   - `from explainer import *`，类继承 `NarratedScene`
   - **开场必须** `self.title_card(...)`，像老师上课一样口语、不赶：先报题「这节课我们来讲 X，也就是……」；只讲一个知识点就直接进入；分板块时用 `lines=[…]` 逐条说「我们分三点来讲。第一点，讲……」「第二点……」，每说一条亮一条，说完停一下再开讲
   - 分板块时，每块开头 `self.section("好，我们先来看第一点，……", 序号, "板块名")`，旁白和开场的「第一点/第二点」呼应；图表要接着用就加 `inline=True`（不清屏，只换右上角标签）
   - 每句旁白：`self.say("旁白原文", 动画…)`。旁白必须是字符串字面量；一句尽量 ≤ 25 字，超宽字幕会自动折两行
   - 版式：**左边图表讲原理，右边简笔画讲故事**（`RIGHT_SPOT` 一带）；讲到人用火柴人，讲到物用简笔画，表情随剧情变化
   - 清屏一律用 `self.clear_stage()`（保留状态栏和板块标签），不要 `FadeOut(Group(*self.mobjects))`；三点讲完可 `self.gain_xp(1.0)` 把经验条涨满（无状态栏的风格自动跳过）
   - 简笔画只从 `scripts/doodles.py` 取；缺新素材就**加进 doodles.py**（同样只用主题语义色），不在分镜里临时画
2. **草稿**：`bash scripts/render.sh <集目录>/分镜.py <类名> --draft` → `<集目录>/草稿.mp4`（约 1 分钟）
3. **抽帧自检**：`ffmpeg -i 草稿.mp4 -vf "fps=1/9,scale=427:-1,tile=4x4" -frames:v 1 检查.png`（检查图放临时目录），看有无文字压线、出画、重叠
4. **成片**：`bash scripts/render.sh <集目录>/分镜.py <类名> --final [--tts clone]` → `<集目录>/<主题>.mp4`，并删掉 `.work/` 和草稿
   - 渲染脚本自动逐句核对配音；报「有 N 句没声音」时不得交付

## 白板风怎么做一集

1. 建集目录，写 `分镜.js`，照 `examples/supply_demand_board.js` 的结构（`module.exports = (b) => { … }`）：
   - 画面 1280×720 像素，白板约 x 30–1250、y 20–622；左上角是板书标题，正文从 `b.headingBottom` 以下写
   - 开场 `b.title(旁白, 题目, [目录…], [逐条旁白…])`；分板块 `b.section(旁白, 序号, 名称, {keep: true}?, 要画的…)`，`keep` = 图表留着只换标题
   - 每句 `b.say(旁白, 要画的…)`：列出的东西按顺序由笔写出来，写字速度跟着这句话的长度自动调
   - 擦：`b.erase()` 擦正文留标题；`b.erase("all")` 全擦；`b.erase({x0, y0, x1, y1})` 只擦一块（如右侧笔记区）。都在下一句开头执行
   - 能画的：`text`（支持 `Q_{d}` 下标、`x^{2}` 上标）、`line`、`arrow`、`dash` 虚线、`curve` 过点曲线、`ellipse`、`circleAround` 圈重点、`underline`、`box`、`axes`（带 `.p(x, y)` 换算 0–10 数值）、`stick` 火柴人（mood / pose）、`bottle`、`mountain`；颜色用 `ink / blue / red / green / gray / orange`。缺新简笔画就加进 `scripts/board/engine.js`，不在分镜里临时拼
   - **自动排版优先，少写坐标**：`graph()` 左区标准坐标图；`note("文字", {color, doodle})` 右区笔记一行行往下记；`b.eraseNotes()` 擦右区、笔记从头记；`formula("Q_{d} = [a] - [b] · P", x, y)` 方括号部分可用 `f.parts.a` 取出，再 `note_on(部分, "注释")` 自动放注释和箭头；`center("文字", y)` 水平居中。只有简笔画小剧场才手写坐标
   - 板书式布局：左边画图讲原理，右边（x > 775）写笔记、画简笔画；同一个画好的东西不要在两句里重复传
2. 草稿：`bash scripts/render_board.sh <集目录>/分镜.js --draft` → `草稿.mp4`（150 秒一集：截图约 25 秒，新旁白配音另需 1–2 分钟）
3. 抽帧自检同上；成片：`bash scripts/render_board.sh <集目录>/分镜.js --final [--tts clone]`（1080p 截图约 45 秒；默认 4 个浏览器分段并行，`WHITEBOARD_WORKERS` 可调）
- 汉字笔画数据里没有的生僻字，会退回用手写字体淡入；需要时换个常用字

## 讲解深度与内容规矩

- **口吻是老师上课，深度是 5 岁小孩和小学生都能听懂（ELI5）**：先生活场景和简笔画故事，再给术语；一次一个概念。学习法场景下按 `state.md` 的「基础水平」调整：0 基础 = ELI5；有基础 = 一句话带过常识，时间留给难点
- 教序：开场主题/目录 → 困惑（生活场景）→ 类比 → 精确定义 → 例子 → （公式）→ 一句话回扣 → 问「哪一个画面你最不确定？」
- 学习场景下，内容只取自该书蒸馏三件套；没有蒸馏材料时在旁白或交付说明里注明「通用知识讲解」
- 一集 60–150 秒为宜；内容多就分板块，仍超 3 分钟就拆集
- **公式不能光秃秃出现**：每个符号用箭头标注「在本例里代表什么 + 单位」，再代入本例数字，最后把结果指回图上的点（见示范分镜 ⑥ 的 `note()`）。图上数值关系尽量取整数
- 语速默认 `+0%`（用户试听后定的）；本人声音档案自带 1.06 倍速。声音以后可换成其他已授权的克隆声音，换法见 `hualun-local-tts`

## 存放规则（不乱放）

| 场景 | 集目录 |
|---|---|
| 学习法 | `~/.hermes/learning/[领域名]/progress-assets/解释视频/YYYY-MM-DD-主题/` |
| 其他正式使用 | `~/Movies/解释视频/YYYY-MM-DD-主题/` |
| 试做、测试、调样式 | 会话临时目录，不进上面两处 |
| 用户说「留」的案例 | `~/Movies/解释视频/案例/YYYY-MM-DD-主题/`（只放分镜 + 成片） |

- 正式集目录 `--final` 后只留 `分镜.py` / `分镜.js`（便于以后改）和 `<主题>.mp4`
- **测试产物默认清理，不用用户提醒**：每次任务结束前，把这次试做产生的草稿、成片、抽帧图、音频缓存、`.work/`、试验脚本全部删掉；只有用户明确说「留」「这个当案例」的，才挪进上面的案例目录（只留分镜和成片）。用户还没看过的成片，先发给用户、交付说明里写明「看完不留就删」，下次开工时清掉
- 一律不写进 Obsidian Vault；音频、中间画面只在 `.work/` 里，成片后自动清掉
