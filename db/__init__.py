"""
QuantiesUnite — Database Package

Re-exports all functions so existing code using `import database as db`
continues to work after switching to `from db import ...` or `import db`.
"""

# Core
from db.core import get_db, init_db

# Users
from db.users import (
    create_user, get_user_by_email, get_user_by_id, get_user_by_username,
    verify_credentials, update_target_level, set_current_level, update_username, update_password,
    all_users, toggle_admin, delete_user, site_stats, ensure_default_admin,
    register_session, is_session_valid, remove_session, get_user_sessions,
)

# Progress
from db.progress import (
    get_progress, mark_topic_complete, save_quiz_score, reset_progress,
    add_target, remove_target, get_targets, get_user_full_progress,
)

# Questions & Quizzes
from db.questions import (
    insert_questions, get_question_count, sample_quiz, get_all_questions,
    save_quiz_attempt, get_wrong_question_ids, get_seen_question_ids,
    sample_practice_quiz, get_practice_stats, get_attempt_count,
    get_question_stats,
)

# Profiles, Activity, Streaks, Achievements, Study Sessions, Dashboard
from db.profiles import (
    ensure_profile, get_profile, update_profile,
    log_activity, get_activity_heatmap, get_recent_activity,
    get_activity_summary, get_weekly_activity,
    get_streak, grant_achievement, get_user_achievements,
    check_and_grant_achievements, ACHIEVEMENTS,
    start_study_session, end_study_session, get_total_study_time,
    get_study_time_by_topic, get_study_time_by_day,
    get_dashboard_data,
)

# Violations
from db.violations import (
    VIOLATION_TYPES, log_violation, get_violations, get_violation_count,
    resolve_violation, resolve_all_user_violations, get_flagged_users,
    admin_violation_timeline,
)

# Admin Analytics
from db.admin_analytics import (
    admin_site_overview, admin_user_growth, admin_daily_active_users,
    admin_top_users, admin_top_topics, admin_get_full_dashboard,
)

# Exams
from db.exams import (
    insert_exam_questions, get_exam_question_count, sample_exam_questions,
    get_all_exam_questions, get_all_exam_questions_by_ids,
    get_exam_wrong_question_ids, get_exam_seen_question_ids,
    save_exam_attempt, has_passed_exam,
    get_exam_attempt_count, get_best_exam_score, get_all_exam_status,
)
