# QuantiesUnite — Project Summary

**QuantiesUnite** is a comprehensive **adaptive math e-learning platform** aligned with Singapore's curriculum, spanning **Kindergarten to Deep Learning** (131 topics across 12 levels).

## Tech Stack

- **Backend:** Flask + SQLite + Waitress
- **Frontend:** Jinja2 templates, KaTeX (math rendering), Chart.js, Vis.js (graph), vanilla JS
- **Themes:** Dark/bright toggle, age-group styling (kindergarten=aqua, primary=green, secondary=blue, adult=purple)

## Core Architecture

- **`app.py`** — All Flask routes (auth, learning, admin, API)
- **`curriculum_data.py`** — 131 topics with prerequisites, levels, metadata
- **`modules/`** — Per-topic content in two formats:
  - **Flat (legacy):** `lesson.py` + `checks.py` + `quiz.py`
  - **Concept-based (new):** `01_concept/lesson.py` + `01_concept/checks.py` + `quiz.py`
- **`lesson_content.py`** — Content loader with fallback generation
- **`database.py`** — SQLite ops (users, progress tracking)

## Key Features

- **Prerequisite chains** — topics unlock only after dependencies are completed
- **Level-based access** — users pick a target level, everything below is accessible
- **70% pass threshold** on quizzes to mark topics complete
- **In-lesson check questions** (ungraded) + graded end-of-topic quizzes
- **Admin dashboard** — user management, stats, per-user progress views
- **Interactive graph** — Vis.js network visualization of the curriculum tree
- **Search, progress tracking, account management**

## Database

Two tables:

- **`users`** — auth, target_level, plan, is_admin
- **`user_progress`** — per-topic completion, quiz scores

## Directory Structure

```
quantiesunite/
├── app.py                  # Main Flask app + all routes
├── lesson_content.py       # Content loader & fallback generation
├── curriculum_data.py      # Full topic graph (131 topics, prerequisites, metadata)
├── database.py             # SQLite operations (users, progress)
├── modules/                # Per-topic content folders
│   ├── __init__.py         # Dynamic lesson loader
│   ├── k_numbers/          # Example: Kindergarten topic
│   ├── p12_whole_1000/     # Example: Primary 1-2 topic
│   ├── alevel_complex/     # Example: Concept-based module
│   │   ├── 01_concept/
│   │   │   ├── lesson.py
│   │   │   └── checks.py
│   │   ├── 02_concept/
│   │   └── quiz.py
│   └── amath_binomial/     # Example: Legacy flat module
│       ├── lesson.py
│       ├── checks.py
│       └── quiz.py
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── quiz.html
│   ├── topic.html
│   ├── concept.html
│   ├── pages/              # Full-page templates
│   ├── lesson/             # Reusable lesson partials
│   ├── admin/              # Admin dashboard
│   ├── auth/               # Login/register
│   └── partials/           # Navbar, footer, flash messages
├── static/
│   ├── css/style.css
│   └── js/graph.js
└── quantiesunite.db        # SQLite database
```

## Learner Journey

1. **Register** — create account, first user becomes admin
2. **Set target level** — controls which levels are accessible
3. **Browse curriculum** — topics organized by level with prerequisite gates
4. **Learn** — read through concept pages or flat sections with check questions
5. **Quiz** — 70% required to pass and unlock dependent topics
6. **Track progress** — per-level breakdown, interactive graph visualization
