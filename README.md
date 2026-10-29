# IRIS-Investment-Deck

Private workspace for refining the **IRIS Investment Summary** (IRIS Intelligence Pty Ltd; AUD $750K pre-seed SAFE at a $7.5M cap). Claude develops the presentation; ChatGPT reviews it as an independent investment committee; the project owner approves. Read `CLAUDE.md` first.

## Branches

- `main` — the approved baseline. Immutable during refinement. Protected: no direct pushes, no deletion; changes only by an approved pull request from the refinement branch.
- `refinement/institutional-v2` — the working branch. All presentation revisions happen here. Nothing merges to `main` without the project owner's explicit approval.

## Baseline

Tag `baseline-v307`: the deck as published on 29 October 2026 (Slides artifact version id `1793270675-17c7`; deck version 307 plus the owner's in-page edits to that point). The commit hash is recorded in `review/review-decisions.md` (D-14) once the first commit is made; `git rev-parse baseline-v307` prints it.

## Layout

```
deck/source/            deck.json + slides/*.html (editable source) · measure.py · format-reference/
deck/assets/            fonts and images (none at baseline)
deck/exports/           PDF exports of approved versions (none at baseline)
financial-model/        build_model.py · IRIS_model_36m.xlsx (controlled source) · README.md
research/               source-register.md · market-evidence.md
review/                 investment-thesis.md · investment-critique.md · claims-register.md · change-log.md · review-decisions.md
CLAUDE.md               project instructions, standards, constraints, procedures
```

## Workflow

1. Open an issue naming the slides affected and the intended investment improvement.
2. Implement on `refinement/institutional-v2`; measure line fits (`deck/source/measure.py`), run the banned-word check, keep page numbers and `deck.json` consistent.
3. Render the PDF into `deck/exports/`.
4. Record the change in `review/change-log.md`; update `review/claims-register.md` if a claim changed.
5. Open or update the pull request `refinement/institutional-v2 → main` for review.
6. ChatGPT records findings in `review/investment-critique.md` or as PR comments; the owner marks each accepted, rejected or deferred.
7. Claude addresses accepted findings; the owner approves; the owner (or Claude on the owner's instruction) merges. Never auto-merge.

## Confidentiality

Private. No credentials, no private record sets, no notes naming prospects, employers, lenders or projects. The three project examples on the deck are altered and must stay unidentifiable.

## Baseline inventory

Committed files with size and the first 16 hex of the SHA-256 (full hashes: `git ls-files | xargs sha256sum`).

| File | Bytes | SHA-256 (prefix) |
|---|---|---|
| `.gitignore` | 164 | `366b5ab75ab501f9` |
| `CLAUDE.md` | 9,354 | `e0107c2d7197ca1b` |
| `deck/assets/README.md` | 155 | `79458ca0c6601c17` |
| `deck/exports/README.md` | 398 | `deeddd4d2125b4f1` |
| `deck/source/deck.json` | 1,447 | `28ef970b05efca3e` |
| `deck/source/format-reference/SKILL.md` | 16,062 | `ce65b744681610b5` |
| `deck/source/format-reference/craft.md` | 11,598 | `49c67a742f359852` |
| `deck/source/format-reference/deck-files.md` | 16,021 | `b10bccc76c0420f9` |
| `deck/source/format-reference/diagram-recipes.md` | 14,555 | `9ff69058b0ef21c1` |
| `deck/source/format-reference/diagrams.md` | 15,934 | `b9ecc6d915bb76df` |
| `deck/source/format-reference/fonts.md` | 13,656 | `43aebf54206513e6` |
| `deck/source/format-reference/format.md` | 16,247 | `b39026f68e7cdd6c` |
| `deck/source/format-reference/images.md` | 8,005 | `4f97d6a815c98e03` |
| `deck/source/format-reference/layout.md` | 11,145 | `744fc7fd7b40db8b` |
| `deck/source/format-reference/questions.md` | 4,273 | `70ba904f7bcb4084` |
| `deck/source/format-reference/styles.md` | 7,994 | `9bee74605ed03ea2` |
| `deck/source/format-reference/view-state.md` | 9,654 | `b81f6ddd448ca8fb` |
| `deck/source/measure.py` | 1,738 | `bad79664a8e9ebc8` |
| `deck/source/slides/apx-model.html` | 7,149 | `a4a06a9072030282` |
| `deck/source/slides/apx-pack.html` | 8,898 | `2bda994c01da1573` |
| `deck/source/slides/apx-risks.html` | 6,174 | `6697fd794e5e446e` |
| `deck/source/slides/apx-sizing.html` | 7,023 | `7af13d96b1e21ca0` |
| `deck/source/slides/apx-sources.html` | 3,920 | `4093ad9919f32e42` |
| `deck/source/slides/close.html` | 4,857 | `d2aca742c8286058` |
| `deck/source/slides/competition.html` | 8,352 | `6431d5395ca1917e` |
| `deck/source/slides/cover.html` | 4,259 | `7ce6718f1f36a6b0` |
| `deck/source/slides/decisions.html` | 4,954 | `2cf5fef72bba8ee9` |
| `deck/source/slides/economics.html` | 10,341 | `610d1c0b2117732b` |
| `deck/source/slides/evidence.html` | 5,298 | `d96608da1ae3a19b` |
| `deck/source/slides/go-to-market.html` | 6,464 | `7e2a2224dd1f4da7` |
| `deck/source/slides/market.html` | 4,350 | `044115822ff7e709` |
| `deck/source/slides/mechanism.html` | 9,605 | `169fb8585c137e08` |
| `deck/source/slides/preempting.html` | 6,968 | `b2a811dd6afcd6f6` |
| `deck/source/slides/product.html` | 9,339 | `a9c98694bbf5e331` |
| `deck/source/slides/raise.html` | 7,122 | `aff26eac3918e70e` |
| `deck/source/slides/reach.html` | 6,960 | `fbb5cea234f53d08` |
| `deck/source/slides/recovery.html` | 5,579 | `1035455d42455bdb` |
| `deck/source/slides/since-2021.html` | 7,497 | `8d658e3715a1004d` |
| `deck/source/slides/stakes.html` | 8,091 | `58f6d914c552d1fa` |
| `deck/source/slides/summary.html` | 4,789 | `48f0d6ba1a68bcfb` |
| `deck/source/slides/systems.html` | 6,589 | `c497b75776fec545` |
| `deck/source/slides/team.html` | 3,116 | `d79d9246fccb6bf8` |
| `deck/source/slides/why-now.html` | 6,252 | `86f19f80bb18d3ad` |
| `financial-model/IRIS_model_36m.xlsx` | 55,574 | `9cc97552202c6ca3` |
| `financial-model/README.md` | 1,606 | `fbe0cb4dfc6ce7c8` |
| `financial-model/build_model.py` | 42,474 | `3302061237b11e2a` |
| `research/market-evidence.md` | 5,325 | `b23815f313d161ac` |
| `research/source-register.md` | 8,929 | `3daec986583cef45` |
| `review/change-log.md` | 5,184 | `0024523a553d11d5` |
| `review/claims-register.md` | 6,636 | `e66b718199161eb4` |
| `review/investment-critique.md` | 2,973 | `f443ace1aec44ea2` |
| `review/investment-thesis.md` | 4,286 | `01738b2933898696` |
| `review/review-decisions.md` | 4,491 | `e0c7c13aa94cf8f2` |
