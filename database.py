"""
QuantiesUnite — Database Layer (backward-compatible re-export)

All database functions have been organized into the db/ package:
  db/core.py          — connection, schema
  db/users.py         — user CRUD & auth
  db/progress.py      — progress, targets
  db/questions.py     — quiz questions, attempts, practice
  db/profiles.py      — profiles, activity, streaks, achievements, study sessions
  db/violations.py    — policy violations
  db/admin_analytics.py — admin dashboard data
  db/exams.py         — exam questions, attempts, scoring

This file re-exports everything so `import database as db` still works.
"""

from db import *  # noqa: F401,F403
