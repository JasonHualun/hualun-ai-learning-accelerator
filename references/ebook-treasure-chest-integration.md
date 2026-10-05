# 电子书宝库下载集成

## 资源来源

**GitHub 仓库**：`jbiaojerry/ebook-treasure-chest`
**在线搜索**：https://jbiaojerry.github.io/ebook-treasure-chest/
**内容**：帆书app(原樊登读书)、微信读书、京东读书、喜马拉雅等读书app的大部分电子书
**格式**：epub、mobi、azw3

## 使用流程

当用户需要下载书籍时，按以下优先级查找：

1. **微信读书**（优先）— 若已配置 `WEREAD_API_KEY`，先调微信读书搜索
2. **电子书宝库**（次优先）— 微信读书找不到时，访问在线搜索站查找
3. **本地教材目录** — 检查 `~/Downloads/书籍/`
4. **Project Gutenberg / archive.org** — 公版书回退

## 在线搜索命令

```bash
# 搜索书籍（替换书名）
curl -s "https://jbiaojerry.github.io/ebook-treasure-chest/" | grep -i "书名关键词"
```

或直接让用户访问搜索站：
https://jbiaojerry.github.io/ebook-treasure-chest/

## 下载文件存放

下载的书籍统一存放到：
```text
~/Downloads/书籍/[学科名]/
```

## 支持的格式

| 格式 | 适用设备 |
|------|---------|
| epub | 大部分电子书阅读器、微信读书 |
| mobi | Kindle |
| azw3 | Kindle（新格式） |

## 注意事项

- 该仓库资源来自多个读书平台，仅供个人学习使用
- 搜索站支持实时搜索，推荐优先使用
- 如果搜索站不可用，可直接浏览 GitHub 仓库用 Ctrl+F 查找
