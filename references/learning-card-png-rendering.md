# 学习知识卡 PNG 渲染与核验

当用户要“作图”“图片知识卡片”“看图片复习”时，SVG 只能作为源文件；最终应发 PNG。

## 推荐流程

1. 生成 SVG 源文件到 Obsidian 知识卡目录。
2. 用 Playwright/Chromium 把 SVG 嵌入固定尺寸 HTML wrapper，再截图成 PNG。
3. 用视觉检查确认：无滚动条、无截断、文字清晰、布局完整。
4. 飞书回复中使用 `MEDIA:/absolute/path.png`。
5. Obsidian 学习笔记与学习首页链接优先指向 PNG，SVG 可保留为可编辑源。

## Playwright 模板

```python
from pathlib import Path
from playwright.sync_api import sync_playwright

svg_path = Path('/absolute/path/card.svg')
png_path = svg_path.with_suffix('.png')
svg = svg_path.read_text(encoding='utf-8')
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html, body {{ margin:0; padding:0; width:1200px; height:1600px; overflow:hidden; background:#fbf7ef; }}
svg {{ display:block; width:1200px; height:1600px; }}
</style></head><body>{svg}</body></html>'''
html_path = svg_path.with_suffix('.render.html')
html_path.write_text(html, encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path='/snap/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page(viewport={'width':1200,'height':1600}, device_scale_factor=1)
    page.goto(html_path.as_uri(), wait_until='load')
    page.screenshot(path=str(png_path), full_page=False)
    browser.close()
```

## Pitfall

Direct `chromium --screenshot file://card.svg` can capture the browser page with scrollbars or crop the bottom. The durable lesson is not “Chromium is broken”; it is to wrap SVG in a fixed-size no-overflow HTML document before screenshotting.

If the SVG/HTML path contains spaces or non-ASCII characters, headless Chromium `file://...` CLI screenshots may silently render Chrome’s `ERR_FILE_NOT_FOUND` page even though the output PNG exists. Safer pattern: write the wrapper under an ASCII temp directory, serve it with `python3 -m http.server --bind 127.0.0.1`, screenshot `http://127.0.0.1:<port>/wrapper.html`, then kill the temp server. Always run visual verification on the PNG; a successful `file`/nonzero size check is not enough.
