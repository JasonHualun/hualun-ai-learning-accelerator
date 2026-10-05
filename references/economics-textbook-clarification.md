# Economics textbook clarification notes

Use when AI 学习法 teaches economics from WeRead/book skeletons and the user asks whether the book is “经济学原理”, microeconomics, or macroeconomics.

## Durable lesson

Do not conflate these two common intro textbooks:

| Chinese common title | Authors | English title | Nature |
|---|---|---|---|
| 《经济学原理》 | N. Gregory Mankiw / 曼昆 | Principles of Economics | Modern beginner-friendly principles textbook; often split into 微观经济学分册 / 宏观经济学分册. |
| 《经济学》 | Paul A. Samuelson + William D. Nordhaus / 萨缪尔森、诺德豪斯 | Economics | Classic comprehensive textbook covering both micro and macro. |

For the current WeRead bookId `3300174856`, the learning state identified it as:

```text
《经济学：第19版》
作者：[美] 保罗·萨缪尔森、威廉·诺德豪斯
主译：萧琛
```

WeRead `/book/chapterinfo` showed 31 main chapters. In that edition’s table of contents, chapters 1–18 are mainly microeconomics / foundational micro topics, and chapters 19–31 are mainly macroeconomics.

## Response pattern

When the user asks whether the current economics book is correct:

1. Check `state.md` for `学习材料` and `bookId`.
2. If possible, call WeRead `/book/chapterinfo` to count chapters and inspect section boundaries.
3. Answer plainly:
   - “You are learning Samuelson/Nordhaus 《经济学》, not Mankiw 《经济学原理》.”
   - “It is not wrong; it is a classic comprehensive economics textbook.”
   - “Mankiw is usually smoother for first-pass beginner intuition; Samuelson/Nordhaus is broader and more classic.”
4. If continuing with Samuelson/Nordhaus, teach with a Mankiw-like style: concrete, conversational, applied to the user’s live-commerce/business scenarios.

## Pitfall

If only WeRead `/book/chapterinfo` was used, say “目录骨架 + 通用经济学知识蒸馏”, not “逐章原文蒸馏”. This distinction matters for user trust.
