# Human Learning Book Project - Instructions

## Current State (Nov 23, 2025)

**Completed**: 3 chapters out of 11

- ✅ Chapter 1: The Spark (Bilingual)
- ✅ Chapter 5: The Habit (Bilingual)
- ✅ Chapter 11: The WHY System (English + Arabic in progress)

**Pending**: Chapters 2, 3, 4, 6, 7, 8, 9 (No titles or content decided yet)

## The Red Zone - Core Spine

The three completed chapters form the unbreakable spine of the book. All other chapters will support or extend these three pillars.

## Directory Structure

```
@human-learning/
├── DOCUMENTATION/
│   └── BOOK_DOCUMENTATION.md
├── CLAUDE.md (this file)
├── README.md
├── 01-THE-SPARK/
├── 02-CHAPTER/
├── 03-CHAPTER/
├── 04-CHAPTER/
├── 05-THE-HABIT/
├── 06-THE-BAD-HABIT/
├── 07-IF-X-THEN-Y/
├── 08-WHEN-WHERE/
├── 09-WHAT-IF/
├── 10-HOW-THEN/
├── 11-THE-WHY-SYSTEM/
├── human-learning-raw/ (source markdown)
├── human-learning/ (output bilingual docx)
└── bilingual-script/ (Python formatters)
```

## Process

1. Write raw markdown to `human-learning-raw/` with both English and Arabic
2. Create/adapt Python formatter script (e.g., `format_chapter[#].py`)
3. Run formatter to generate bilingual Word document with parallel columns
4. Save output to chapter directory
5. Archive markdown version in chapter directory

## Important

- Do NOT assume or guess content for undecided chapters
- Only document what is actually completed or decided
- When new chapters are written, follow the bilingual format established in Chapters 1 and 5

**Created**: May 5, 2025
**Updated**: November 23, 2025
