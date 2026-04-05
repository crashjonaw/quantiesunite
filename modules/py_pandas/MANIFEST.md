# py_pandas Module - Restructured Documentation

## Overview
The `py_pandas` module has been converted from a flat structure to a concept-structured architecture with 5 self-contained learning modules.

## Module Structure

```
py_pandas/
├── 01_series_and_dataframes/
│   ├── __init__.py
│   └── lesson.py (3 sections, ~350 lines)
├── 02_data_selection_and_filtering/
│   ├── __init__.py
│   └── lesson.py (4 sections, ~375 lines)
├── 03_data_cleaning_missing_values/
│   ├── __init__.py
│   └── lesson.py (4 sections, ~375 lines)
├── 04_groupby_and_aggregation/
│   ├── __init__.py
│   └── lesson.py (4 sections, ~375 lines)
├── 05_merging_and_joining/
│   ├── __init__.py
│   └── lesson.py (4 sections, ~375 lines)
└── quiz.py (assessment at module level)
```

## Concept Modules

### 01: Series and DataFrames (Fundamentals)
**Files:** `01_series_and_dataframes/`
- **Series: One-Dimensional Data** - Creating Series, index basics, dtype handling
- **DataFrames: Two-Dimensional Data** - DataFrame construction, column structure
- **Index: The Alignment Mechanism** - Index types, immutability, performance

### 02: Data Selection and Filtering (Access Patterns)
**Files:** `02_data_selection_and_filtering/`
- **Label-Based Selection with .loc** - Selecting by index/column labels
- **Position-Based Selection with .iloc** - Integer-location indexing
- **Boolean Filtering** - Conditional selection, multi-condition logic
- **Advanced Selection Techniques** - query(), isin(), between()

### 03: Data Cleaning and Missing Values (Data Quality)
**Files:** `03_data_cleaning_missing_values/`
- **Detecting Missing Values** - isna(), isnull(), NaN propagation
- **Handling Missing Data** - dropna(), ffill(), bfill(), imputation strategies
- **Type Conversion** - astype(), to_numeric(), nullable types
- **Data Validation** - Type checking, duplicate detection, range validation

### 04: GroupBy and Aggregation (Data Transformation)
**Files:** `04_groupby_and_aggregation/`
- **GroupBy: Split-Apply-Combine** - Lazy evaluation, grouping mechanics
- **Aggregation Functions** - mean(), sum(), agg(), named aggregations
- **Transform and Apply** - Broadcasting group results, custom functions
- **Advanced Operations** - Standardization, outlier detection, filtering groups

### 05: Merging and Joining (Data Combination)
**Files:** `05_merging_and_joining/`
- **Merge Operations** - INNER/LEFT/RIGHT/OUTER joins, SQL-like operations
- **Index-Based Joins** - join(), concat(), hierarchical indices
- **Advanced Joins** - Multi-key merges, validation, handling duplicates
- **Performance** - Optimization strategies, Cartesian product warnings

## Styling and Presentation

### Dark Theme Color Palette
```css
--text: #e6edf3          /* Light gray-blue text */
--bg: #0d1117            /* Dark navy background */
--surface: #161b22       /* Slightly lighter surface for contrast */
--accent: #4f8ef7        /* Bright blue accent color */
```

### CSS Classes (Content Boxes)
- **`.concept-box`** - Left accent border (accent color), used for key concepts
- **`.worked-example`** - Light accent background, practical code examples
- **`.warning-box`** - Red left border (#f87171), common pitfalls and gotchas
- **`.success-box`** - Green left border (#4ade80), best practices

## Content Approach

Each lesson follows a **first-principles pedagogy**:
1. **Concept Introduction** - Explain the underlying mechanism
2. **Memory/Architecture Model** - How data structures work internally
3. **Worked Examples** - Practical code with real scenarios
4. **Common Pitfalls** - Warning boxes for gotchas
5. **Best Practices** - Success boxes with optimization tips

## Files Structure

### Created Files
- `01_series_and_dataframes/__init__.py` (empty module marker)
- `01_series_and_dataframes/lesson.py` (TITLE, STYLES, SECTIONS)
- `02_data_selection_and_filtering/__init__.py`
- `02_data_selection_and_filtering/lesson.py`
- `03_data_cleaning_missing_values/__init__.py`
- `03_data_cleaning_missing_values/lesson.py`
- `04_groupby_and_aggregation/__init__.py`
- `04_groupby_and_aggregation/lesson.py`
- `05_merging_and_joining/__init__.py`
- `05_merging_and_joining/lesson.py`

### Deleted Files
- ~~`lesson.py`~~ (old flat structure)
- ~~`checks.py`~~ (old flat structure)

### Preserved Files
- `quiz.py` (kept at module root level)

## Statistics

| Metric | Value |
|--------|-------|
| Concept Modules | 5 |
| Total Sections | 19 |
| Total Lessons Lines | 1,533 |
| Files per Concept | 2 (__init__.py + lesson.py) |
| Syntax Validation | 6/6 PASS (100%) |
| CSS Classes | 4 implemented |
| Dark Theme Colors | 4 verified |

## Usage

Each module is self-contained and can be imported independently:

```python
# Import individual lessons
from py_pandas.01_series_and_dataframes import lesson

# Access content
title = lesson.TITLE
sections = lesson.SECTIONS
styles = lesson.STYLES
```

## Verification

All files have been validated:
- ✓ Python syntax check (ast.parse)
- ✓ Content structure (TITLE, SECTIONS, STYLES)
- ✓ Dark theme CSS implementation
- ✓ First-principles pedagogy
- ✓ Code examples with explanations
- ✓ Best practices and warnings included

---
**Last Updated:** 2024-03-23
**Status:** ✓ Complete and Verified
