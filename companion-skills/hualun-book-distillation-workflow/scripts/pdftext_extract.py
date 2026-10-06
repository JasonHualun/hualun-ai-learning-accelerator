#!/usr/bin/env python3
"""
PyMuPDF (fitz) PDF → plaintext extractor with empty-page detection.
Drop-in replacement for pdfplumber when the latter is unavailable or returns garbage.

Usage:
    python3 pdftext_extract.py path/to/file.pdf  [output.txt]

Output is written as fulltext.txt (or custom name) with '=== PAGE N ===' headers
for easy read_file() pagination later.

Requires: pip install pymupdf
"""

import sys
from pathlib import Path

def extract(pdf_path: str, output_path: str = None):
    import fitz
    doc = fitz.open(pdf_path)
    total = len(doc)
    blocks = []
    empty_count = 0
    for i, page in enumerate(doc):
        t = page.get_text()
        if not t.strip():
            empty_count += 1
        blocks.append(f'=== PAGE {i + 1} ===\n' + t)
    full = '\n'.join(blocks)
    out = Path(output_path) if output_path else Path(pdf_path).parent / 'fulltext.txt'
    out.write_text(full, encoding='utf-8')
    chars = len(full)
    print(f"Extracted {total} pages ({empty_count} empty), {chars:,} chars → {out}")
    return chars

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 pdftext_extract.py <pdf_path> [output_path]")
        sys.exit(1)
    extract(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
