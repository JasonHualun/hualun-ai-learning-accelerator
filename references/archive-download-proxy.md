# Archive.org / Gutenberg 下载与代理配置

## 当前代理配置
- 工具：Clash Verge
- HTTP 代理：按本机代理软件的端口填写（例：`http://127.0.0.1:<端口>`）
- 验证：`curl -x http://127.0.0.1:<端口> -L -o /tmp/test.pdf <url>`

---

## 公共资源优先级

**首选：Project Gutenberg**（比 archive.org 更可靠）
- 网址：`https://www.gutenberg.org/ebooks/search/?query=spinoza+ethics`
- 优势：plain text 格式，无 DRM，无需猜测 identifier
- 哲学几何式结构著作用 `.txt` 比 PDF 更好（方便 grep 定位命题/证明）

**备选：archive.org**（Gutenberg 没有时用）

---

## 已验证可用的 Spinoza《伦理学》资源

### ✅ Project Gutenberg（首选，2026-05 实测有效）

| 资源 | ebook ID | 格式 | 大小 | 说明 |
|------|----------|------|------|------|
| 完整五部分 | `#3800` | Plain Text | 531KB | **Elwes 译本；推荐** |
| Part I | `#919` | | | |
| Part II | `#920` | | | |
| Part III | `#948` | | | |
| Part IV | `#971` | | | |
| Part V | `#975` | | | |

**下载命令（实测 531KB）：**
```bash
mkdir -p ~/Downloads/书籍/斯宾诺莎
curl -x http://127.0.0.1:<端口> -L -s \
  -o ~/Downloads/书籍/斯宾诺莎/伦理学-英文.txt \
  "https://www.gutenberg.org/cache/epub/3800/pg3800.txt"
```

### ❌ archive.org（已废弃，勿用）
- `spinozaethic00spinuoft` — 返回 404，item 不存在

---

## 下载命令模板

### Project Gutenberg plain text
```bash
curl -x http://127.0.0.1:<端口> -L -s \
  -o ~/Downloads/书籍/[作者]/[书名]-英文.txt \
  "https://www.gutenberg.org/cache/epub/[ebook_id]/pg[ebook_id].txt"
```

### archive.org PDF（备选）
```bash
curl -x http://127.0.0.1:<端口> -L \
  -o ~/Downloads/书籍/[学科名]/[书名].pdf \
  "https://archive.org/download/[identifier]/[identifier]_text.pdf"
```

---

## Archive.org 搜索技巧
- 搜索词加 `geometrical` 可精准定位《伦理学》版本
- 下载前先在浏览器确认 identifier 存在（`archive.org/details/[identifier]`）
- PDF 文本格式 identifier 通常是 `{identifier}_text.pdf`
