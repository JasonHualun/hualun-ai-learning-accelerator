# Article-Based RAG Primer Session Pattern

Use this reference when the user pastes a long AI/RAG article and asks to be taught as a beginner, especially outside a formal book-learning flow.

## Teaching pattern that worked

- Treat the pasted article as source material, but do not dump a full summary.
- Teach in tiny steps: one concept → one plain-language explanation → one concrete example → one small check question.
- Use the user's answer to confirm or correct before moving on.
- Keep concepts in this order for RAG primers:
  1. RAG = AI first retrieves relevant material, then answers from it.
  2. Embedding = turns text into numeric meaning coordinates.
  3. Chunk = a small content slice that preserves a complete meaning.
  4. Skill vs Chunk = Skill is a workflow/SOP; Chunk is searchable knowledge content.
  5. Vector database = stores embeddings and finds nearby meaning coordinates.
  6. Metadata = the document's identity card, used for filtering and weighting.
  7. BM25 = keyword search for exact terms, names, IDs, dates, fixed phrases.
  8. Hybrid retrieval = narrow sense BM25 + Embedding; broad sense multiple retrieval/filter/ranking signals together.
  9. Coarse retrieval/recall and fine ranking/Rerank = first don't miss, then rank accurately.
  10. Query expansion = rewrite one user query into several likely search phrasings.
  11. Feedback learning / Learning to Rank = learn which retrieved results should rank higher from clicks, explicit feedback, and labels.

## Beginner-friendly distinctions

- Chunk is not Skill: Chunk is knowledge; Skill is method.
- Chunking is not fixed-size chopping: enterprise RAG should identify document type, preserve structure, and store one complete meaning per chunk.
- Hybrid retrieval is not only BM25 + Embedding in the broad engineering sense; metadata, time decay, source weight, rerank, and feedback can also be signals.
- Query expansion does not require a perfect company-wide thesaurus at launch; start with high-frequency terms, existing business terms, document headings, FAQs, and search failures, then iterate.
- Learning to Rank is not answer generation and not embedding; it learns which search results should be first.

## Good knowledge-card takeaway

> 资料越多，越不能一股脑塞给 AI；要先整理、筛选、检索，再让 AI 回答。

## Save/closeout pattern

When the user says today's learning is done and asks for a card/record:

1. Generate a concise SVG knowledge card under Obsidian `LLM Wiki/wiki/学习/AI学习/复习卡/`.
2. Write a learning note under `LLM Wiki/wiki/学习/AI学习/<实际学科>/` with frontmatter and sections: progress, concepts, corrected misunderstandings, personal knowledge-base advice, next directions.
3. Write/update `~/.hermes/learning/<topic>/state.md` with current node, covered concepts, misunderstandings, and 1/7/30-day review queue.
4. Update Obsidian `LLM Wiki/wiki/学习/AI学习/00-入口.md` with a short index entry and knowledge-card link.
5. Tell the user exactly what was written and explicitly state whether Hermes memory was changed.