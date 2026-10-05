# Paper Kit 黑白手绘线框章节思维导图渲染规则

Use when a completed learning chapter needs a visual mind-map / chapter review image, or when the user asks for “黑白手绘线框 / Paper Kit / wireframe” style.

## Source prompt

Default style is **黑白手绘线框 Paper Kit / Wireframe UI 风格**.

### English prompt

```text
A black-and-white hand-drawn wireframe mind map, Paper Kit UI style, dotted paper background, thick black outlines, slightly imperfect sketch lines, low-fidelity product prototype look, sticky note cards, speech bubbles, tag labels, connector arrows, sticker-like buttons, simple monochrome icons, clean structure, generous whitespace, grayscale palette, subtle paper texture, minimal shadows, premium editorial layout for complex information architecture.
```

### Chinese prompt

```text
请生成一张黑白手绘线框风格的思维导图。画面像 Paper Kit / Wireframe UI 原型稿，背景是白色点阵纸，所有节点都是粗黑色描边的便签卡片或气泡标签，节点之间用手绘箭头和连线连接。整体不要彩色，不要渐变，不要真实照片。风格要像设计师在纸上画产品结构图，清晰、有层级、留白充足，适合展示主题、分支、子任务、流程和标签。
```

### Reusable formula

```text
主题：{章节主题}
风格：黑白手绘线框 Paper Kit 风格，点阵纸背景，粗黑描边，低保真产品原型，便签节点，气泡标签，手绘箭头，黑白灰配色。
结构：中心主题在中间，四到六个一级分支环绕，每个分支有二到四个子节点，层级清晰，留白充足。
要求：像设计师画的思维导图/产品工作流草图，不要彩色，不要3D，不要真实照片。
```

### Negative prompt

```text
不要彩色渐变，不要赛博朋克，不要3D，不要真实照片，不要复杂插画，不要科技蓝光，不要玻璃拟态，不要过度装饰，不要花哨背景，不要卡通人物占主体，不要密集文字，不要杂乱排版。
```

## Content boundary

- Use the chapter concept map as the content source: chapter topic → 4-6 main branches → 2-4 child nodes each → relationship arrows.
- Keep text short: preferably 4-12 Chinese characters per node. Split complex concepts into multiple nodes instead of long sentences.
- Do not add self-test questions, long explanations, slogans, decorative filler, cartoon characters, or unrelated copy.
- For economics concept maps, make core relationships visual with simple black line mini-diagrams when helpful, e.g. supply/demand curves, equilibrium point, arrows for shifts.

## Visual requirements

- Style: black-and-white hand-drawn wireframe Paper Kit UI, like a designer’s low-fidelity product structure sketch on paper.
- Background: white or light-gray dotted paper with subtle paper texture.
- Nodes: thick black outlined rounded sticky-note cards, speech bubbles, tag labels, sticker-like buttons.
- Connectors: hand-drawn arrows and solid/dotted connector lines; relationships must be clear.
- Palette: grayscale only; avoid gradients, cyberpunk, tech-blue glow, glassmorphism, fluorescent colors, or rainbow palettes.
- Typography: readable Chinese system fonts: `Noto Sans CJK SC`, `Microsoft YaHei`, `PingFang SC`, `Source Han Sans SC`; avoid weird art fonts or distorted Chinese.
- Mobile/Feishu friendly: portrait PNG is fine; extend height rather than cramming or clipping.

## Stable HTML/CSS → PNG fallback

When exact Chinese text matters, build an HTML/CSS/SVG card and render to PNG with Chromium/Playwright instead of asking an image model to render Chinese text.

Example command:

```bash
/snap/bin/chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --screenshot='/absolute/output.png' \
  --window-size=1200,2350 \
  'file:///absolute/card.html'
```

If Chromium outputs `N bytes written` but the requested output path is missing, re-run with a path under `/private/tmp/` and copy from there. The durable lesson is to verify the file exists and inspect it, not to assume success from stdout.

## Verification checklist before sending

- PNG exists at the path you will send.
- No browser error page, missing `file://` asset, or blank screenshot.
- No top/bottom clipping; bottom modules are fully visible.
- No scrollbars captured.
- Chinese is readable and not garbled.
- Font looks normal, not weird decorative glyphs.
- Colors are coherent and not dirty/random.
- No forbidden extra content was added.

If any check fails, fix and re-render before sending. Do not send a known-bad image and explain it away.
