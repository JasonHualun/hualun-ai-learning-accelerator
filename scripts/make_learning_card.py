#!/usr/bin/env python3
"""Generate a lightweight SVG review card for AI learning notes.

Usage:
  python make_learning_card.py <book> <chapter> <concept_file> <output.svg>

Concept file lines:
  icon | name | explanation | color_key
color_key: blue / peach / sage / gold
"""
from __future__ import annotations
import html
import sys
from pathlib import Path
from datetime import date, timedelta

PALETTE = {
    "bg": "#F6F3EF",
    "ink": "#333333",
    "muted": "#6D6A66",
    "line": "#D8D0C7",
    "blue": "#9BB7C8",
    "peach": "#D8A6A1",
    "sage": "#A9BFA8",
    "gold": "#C3A56B",
}
DECOR = ["RECALL", "CONNECT", "APPLY", "REVIEW", "INSIGHT"]

def wrap(text: str, width: int = 28):
    text = text.strip()
    if not text:
        return [""]
    lines, cur, n = [], "", 0
    for ch in text:
        w = 2 if ord(ch) > 127 else 1
        if n + w > width and cur:
            lines.append(cur)
            cur, n = ch, w
        else:
            cur += ch
            n += w
    if cur:
        lines.append(cur)
    return lines[:3]

def parse_concepts(path: Path):
    if not path.exists():
        return []
    items = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        parts = [p.strip() for p in raw.split("|")]
        while len(parts) < 4:
            parts.append("")
        icon, name, desc, color = parts[:4]
        items.append({"icon": icon or "●", "name": name, "desc": desc, "color": color or "blue"})
    return items[:5]

def main():
    if len(sys.argv) < 5:
        print(__doc__, file=sys.stderr)
        raise SystemExit(2)
    book, chapter, concept_file, output = sys.argv[1:5]
    output = Path(output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    concepts = parse_concepts(Path(concept_file).expanduser())
    if not concepts:
        concepts = [
            {"icon": "1", "name": "核心概念", "desc": "用一句话说清它解决什么问题。", "color": "blue"},
            {"icon": "2", "name": "关键误区", "desc": "复习时先检查自己有没有踩这个坑。", "color": "peach"},
            {"icon": "3", "name": "应用场景", "desc": "换一个真实情境，看看能不能用出来。", "color": "sage"},
        ]
    today = date.today()
    review = f"复习：{today+timedelta(days=1)} / {today+timedelta(days=7)} / {today+timedelta(days=30)}"
    h = 260 + len(concepts) * 112
    rows = []
    y = 178
    for i, c in enumerate(concepts):
        color = PALETTE.get(c.get("color", "blue"), PALETTE["blue"])
        name = html.escape(c.get("name", ""))
        icon = html.escape(c.get("icon", "●"))
        decor = DECOR[i % len(DECOR)]
        desc_lines = wrap(c.get("desc", ""), 34)
        desc_svg = "".join(f'<tspan x="150" dy="{24 if j else 0}">{html.escape(line)}</tspan>' for j, line in enumerate(desc_lines))
        rows.append(f'''
  <g transform="translate(0,{y})">
    <circle cx="92" cy="10" r="22" fill="{color}" opacity="0.92"/>
    <text x="92" y="17" text-anchor="middle" font-size="19" fill="white" font-weight="700">{icon}</text>
    <text x="150" y="0" font-size="26" fill="{PALETTE['ink']}" font-weight="700">{name}</text>
    <text x="690" y="0" text-anchor="end" font-size="14" fill="#C7BFB5" letter-spacing="2">{decor}</text>
    <text x="150" y="34" font-size="18" fill="{PALETTE['muted']}">{desc_svg}</text>
  </g>''')
        y += 112
    insight_y = h - 105
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="{h}" viewBox="0 0 800 {h}">
  <rect width="800" height="{h}" rx="34" fill="{PALETTE['bg']}"/>
  <text x="400" y="64" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',Arial" font-size="34" fill="{PALETTE['ink']}" font-weight="800">{html.escape(book)}</text>
  <text x="400" y="104" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',Arial" font-size="22" fill="#607D8B">{html.escape(chapter)}</text>
  <line x1="110" y1="130" x2="690" y2="130" stroke="{PALETTE['line']}" stroke-width="2"/>
  {''.join(rows)}
  <rect x="72" y="{insight_y}" width="656" height="70" rx="18" fill="#3F3A36"/>
  <rect x="98" y="{insight_y+18}" width="5" height="34" rx="2" fill="{PALETTE['gold']}"/>
  <text x="125" y="{insight_y+30}" font-size="15" fill="{PALETTE['gold']}" font-weight="700">REVIEW CARD</text>
  <text x="125" y="{insight_y+55}" font-size="18" fill="#F7F2EA">{html.escape(review)}｜自测：不用看笔记，讲给一个外行听。</text>
</svg>'''
    output.write_text(svg, encoding="utf-8")
    print(str(output))

if __name__ == "__main__":
    main()
