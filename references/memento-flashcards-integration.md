# Memento flashcards integration

Use this when adding local spaced-repetition flashcards to the AI 学习 workflow or daily review cron.

## Capability

Official optional skill: `official/productivity/memento-flashcards`.

Installed path after hub install:

```text
~/.hermes/skills/productivity/memento-flashcards/
```

Card data path:

```text
~/.hermes/skills/productivity/memento-flashcards/data/cards.json
```

Always use the script; do not edit `cards.json` directly.

```bash
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py <subcommand>
```

Useful subcommands:

```bash
# Stats
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py stats

# Add a card
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py add \
  --question "..." \
  --answer "..." \
  --collection "AI学习"

# Due cards
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py due
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py due --collection "AI学习"

# Rate after showing feedback to the user
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py rate \
  --id CARD_ID --rating easy|good|hard|retire --user-answer "..."

# Remove test or obsolete collection
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py delete-collection --collection "System Test"
```

## Smoke test pattern

For install verification, create a temporary `System Test` card, confirm it appears in `due`, retire/rate it, then delete the collection so no test data remains.

```bash
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py stats
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py add \
  --question 'Memento 测试卡：这张卡用于什么？' \
  --answer '验证 memento-flashcards 本地 JSON 读写和复习队列可用。' \
  --collection 'System Test' > /tmp/memento_add.json
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py due --collection 'System Test'
python3 - <<'PY'
import json, subprocess
card_id = json.load(open('/tmp/memento_add.json'))['card']['id']
subprocess.run([
  'python3', '~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py',
  'rate', '--id', card_id, '--rating', 'retire', '--user-answer', '测试完成'
], check=True)
PY
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py delete-collection --collection 'System Test'
python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py stats
```

## AI 学习 cron integration

Do not silently change the AI 学习 daily review cron. For this user, cron/channel behavior changes require explicit approval.

Recommended integration after approval:

1. Keep the existing `~/.hermes/learning/**/state.md` review queue as the primary learning-state source.
2. Add `memento-flashcards` as an additional skill on the daily review cron.
3. Add `terminal` if not already enabled.
4. Update the cron prompt so it checks both:
   - due rows in `~/.hermes/learning/**/state.md`
   - `memento_cards.py due`
5. If neither source has due items, final output must remain `[SILENT]`.
6. If Memento has due cards, send only a short reminder to the AI 学习群; do not start the quiz inside cron, because cron sessions cannot wait for user answers.

Suggested reminder text:

```text
📚 今日复习提醒
- 学习队列：N 个到期节点
- 闪卡队列：M 张 Memento 卡片到期
回复「复习一下」我就按队列出题。
```

## Boundary

Memento is for atomic recall cards and lightweight review. It should not replace `state.md` as the canonical source for book/chapter progress, misconceptions, knowledge maps, Obsidian notes, or chapter completion.
