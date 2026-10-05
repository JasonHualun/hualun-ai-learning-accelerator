# 微信读书 API 调用模式（实测记录）

## 关键发现

### 书架接口：`/shelf/sync`，不是 `/shelf/list`

2026-05-26 实测：调用 `/shelf/list` 返回 `{"errcode":-2003,"errmsg":"缺少 api_name 参数"}`（499状态码）。

**正确接口是 `/shelf/sync`**，无参数，自动识别用户身份。

```json
{"api_name": "/shelf/sync", "skill_version": "1.0.3"}
```

返回 `books[]`（电子书）、`albums[]`（有声书）、`archive[]`（书单）、`mp`（文章收藏）。

### 常见错误

| 错误 | 原因 | 修复 |
|------|------|------|
| 499 + "缺少 api_name 参数" | 接口名写错（如 `/shelf/list`） | 改为 `/shelf/sync` |
| 业务参数不生效 | 参数包在 `params` 内 | 参数平铺到 body 顶层 |
| 分页失效 | `lastSort` 包在 `params` 内 | 平铺到 body 顶层 |

### 可用接口列表

发送 `{"api_name": "/_list", "skill_version": "1.0.3"}` 获取完整接口列表。

### 返回字段（书架）

- `books[].bookId`：书籍ID
- `books[].title`：书名
- `books[].author`：作者
- `books[].category`：分类
- `books[].finishReading`：是否读完（1=读完）
- `books[].readUpdateTime`：最近阅读时间（Unix时间戳）
- `books[].secret`：是否私密（1=私密）
- `albums[]`：有声书/专辑
- `archive[].name`：书单名称
- `archive[].bookIds`：书单内的bookId列表
