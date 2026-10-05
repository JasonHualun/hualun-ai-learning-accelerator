# AI Learning Runtime Additions

Session-derived durable workflow details for `hualun-ai-learning-accelerator`.

## Obsidian-first learning storage

- Main learning library: `~/Documents/Obsidian Vault/LLM Wiki/wiki/学习/AI学习/`
- Keep `~/.hermes/learning-notes/` as cache/backup only.
- Maintain a short homepage at `LLM Wiki/wiki/学习/AI学习/00-入口.md`; do not turn it into a long log.
- Long notes go under `LLM Wiki/wiki/学习/AI学习/<实际学科>/`; review cards go under `LLM Wiki/wiki/学习/AI学习/复习卡/`.

## Book file lookup order

1. `~/Downloads/书籍/` — current local textbook directory on macOS.

## Review-card workflow

After a chapter is completed:

1. Extract 3-5 concepts into a concept file, one per line:
   ```text
   icon | 名称 | 一句话解释 | blue|peach|sage|gold
   ```
2. Generate an SVG card:
   ```bash
   /usr/bin/python3 ~/.hermes/skills/hualun-ai-learning-accelerator/scripts/make_learning_card.py \
     "书名" "第X章 章节名" /tmp/concepts.txt \
     "~/Documents/Obsidian Vault/LLM Wiki/wiki/学习/AI学习/复习卡/书名-第X章-YYYY-MM-DD.svg"
   ```
3. Link it from the chapter note:
   ```markdown
   ![知识卡](<LLM%20Wiki/wiki/学习/AI学习/复习卡/书名-第X章-YYYY-MM-DD.svg>)
   ```
4. Update `LLM Wiki/wiki/学习/AI学习/00-入口.md` with only a short link/status row.

## Per-section progress notes

After every completed smallest learning unit (小节/子项), keep the record lightweight. The goal is only to prevent repeated teaching in a new conversation.

Prefer updating `state.md` directly. If a separate note is needed, write only:

```text
~/.hermes/learning/[领域名]/section-notes/[书名]-第X章-[小节编号]-YYYY-MM-DD.md
```

Minimal note format:

```markdown
# [书名] 第X章 [小节标题]
日期：YYYY-MM-DD
状态：已通过 / 暂停 / 需重学
已通过概念：[概念A、概念B]
下次从这里继续：[下一小节/当前断点]
备注：[必要误区或用户纠正；没有写“无”]
```

Do not write detailed concept explanations, examples, test transcripts, or long reflections for each small section. Detailed notes, misconception summaries, knowledge cards, and mind maps are created only after a major section/chapter is completed.

## Chapter mind-map workflow

After a major section/chapter is passed:

1. Use the chapter concept map as the only content source: chapter theme → main branches → definitions/relations → result splits.
2. Apply the local infographic design principles from:
   ```text
   ~/Documents/Obsidian Vault/LLM Wiki/wiki/外部知识与参考/视觉与AIGC/图像生成/生图-信息图.md
   ```
3. Generate exactly one information-design mind-map card. Do not use the deleted `生图-知识导图卡片.md`; do not make it hand-drawn/cute; do not add life examples, self-test questions, slogans, or memory hooks unless the user explicitly asks.
4. Typography/color constraints: readable Chinese system font, restrained palette, clear grid/spacing, visible connectors/arrows, no random colors or weird art fonts.
5. Save a copy to local learning progress:
   ```text
   ~/.hermes/learning/[领域名]/progress-assets/[书名]-第X章-思维导图-YYYY-MM-DD.png
   ```
6. Save/copy a copy to Obsidian:
   ```text
   ~/Documents/Obsidian Vault/LLM Wiki/wiki/学习/AI学习/复习卡/[书名]-第X章-思维导图-YYYY-MM-DD.png
   ```
7. Send the PNG to Feishu with `MEDIA:/absolute/path.png`.
8. Visually verify the image: Chinese readable, fonts normal, colors coherent, no truncation, no layout overflow, and no forbidden extra content. If AI image text fails, build an HTML/SVG Chinese-layout version and screenshot it to PNG.

## Daily review cron pattern

A daily cron should scan `~/.hermes/learning/**/state.md` for due review items and deliver only when there are due items. If none are due, return exactly `[SILENT]`.

The cron must remind only; it must not start teaching because cron sessions cannot wait for user replies.
