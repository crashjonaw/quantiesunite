"""
Database core — connection, schema initialization.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "quantiesunite.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            username      TEXT     UNIQUE NOT NULL,
            email         TEXT     UNIQUE NOT NULL,
            password_hash TEXT     NOT NULL,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            target_level  TEXT     DEFAULT 'Deep Learning Advanced',
            plan          TEXT     DEFAULT 'free',
            is_admin      INTEGER  DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS user_targets (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id   INTEGER NOT NULL,
            topic_id  TEXT    NOT NULL,
            added_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id)
        );

        CREATE TABLE IF NOT EXISTS user_progress (
            id           INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER  NOT NULL,
            topic_id     TEXT     NOT NULL,
            complete     INTEGER  DEFAULT 0,
            quiz_score   INTEGER,
            quiz_total   INTEGER,
            completed_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, topic_id)
        );

        CREATE TABLE IF NOT EXISTS quiz_questions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id    TEXT    NOT NULL,
            question    TEXT    NOT NULL,
            answer      TEXT    NOT NULL,
            options     TEXT,
            explanation TEXT,
            difficulty  INTEGER DEFAULT 1,
            concept     TEXT,
            tags        TEXT,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_qq_topic ON quiz_questions(topic_id);
        CREATE INDEX IF NOT EXISTS idx_qq_diff  ON quiz_questions(topic_id, difficulty);

        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id           INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER  NOT NULL,
            topic_id     TEXT     NOT NULL,
            question_ids TEXT     NOT NULL,
            answers      TEXT     NOT NULL,
            score        INTEGER  NOT NULL,
            total        INTEGER  NOT NULL,
            passed       INTEGER  DEFAULT 0,
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_qa_user  ON quiz_attempts(user_id, topic_id);

        CREATE TABLE IF NOT EXISTS user_profiles (
            user_id        INTEGER PRIMARY KEY,
            display_name   TEXT,
            bio            TEXT     DEFAULT '',
            avatar_url     TEXT     DEFAULT '',
            school         TEXT     DEFAULT '',
            grade          TEXT     DEFAULT '',
            birth_year     INTEGER,
            timezone       TEXT     DEFAULT 'Asia/Singapore',
            preferences    TEXT     DEFAULT '{}',
            updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS user_activity (
            id          INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER  NOT NULL,
            activity_date DATE   NOT NULL,
            activity_type TEXT   NOT NULL,
            topic_id    TEXT,
            detail      TEXT     DEFAULT '',
            points      INTEGER  DEFAULT 1,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_ua_user_date ON user_activity(user_id, activity_date);
        CREATE INDEX IF NOT EXISTS idx_ua_type      ON user_activity(user_id, activity_type);

        CREATE TABLE IF NOT EXISTS user_streaks (
            user_id         INTEGER PRIMARY KEY,
            current_streak  INTEGER DEFAULT 0,
            longest_streak  INTEGER DEFAULT 0,
            last_active_date DATE,
            total_active_days INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS user_achievements (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id       INTEGER  NOT NULL,
            achievement_id TEXT    NOT NULL,
            earned_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            UNIQUE(user_id, achievement_id)
        );
        CREATE INDEX IF NOT EXISTS idx_uach_user ON user_achievements(user_id);

        CREATE TABLE IF NOT EXISTS user_study_sessions (
            id          INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER  NOT NULL,
            topic_id    TEXT     NOT NULL,
            started_at  TIMESTAMP NOT NULL,
            ended_at    TIMESTAMP,
            duration_s  INTEGER  DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_uss_user  ON user_study_sessions(user_id, topic_id);
        CREATE INDEX IF NOT EXISTS idx_uss_date  ON user_study_sessions(user_id, started_at);

        CREATE TABLE IF NOT EXISTS policy_violations (
            id            INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id       INTEGER,
            ip_address    TEXT,
            violation_type TEXT    NOT NULL,
            severity      TEXT    DEFAULT 'warning',
            detail        TEXT    DEFAULT '',
            endpoint      TEXT    DEFAULT '',
            resolved      INTEGER DEFAULT 0,
            resolved_by   TEXT,
            resolved_at   TIMESTAMP,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
        );
        CREATE INDEX IF NOT EXISTS idx_pv_user ON policy_violations(user_id);
        CREATE INDEX IF NOT EXISTS idx_pv_type ON policy_violations(violation_type);
        CREATE INDEX IF NOT EXISTS idx_pv_date ON policy_violations(created_at);

        -- ── Exam Question Bank (separate from quiz questions) ────────
        CREATE TABLE IF NOT EXISTS exam_questions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id    TEXT    NOT NULL,
            question    TEXT    NOT NULL,
            answer      TEXT    NOT NULL,
            options     TEXT,
            explanation TEXT,
            difficulty  INTEGER DEFAULT 2,
            concept     TEXT,
            tags        TEXT,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_eq_topic ON exam_questions(topic_id);

        -- ── Exam Attempts ─────────────────────────────────────────────
        CREATE TABLE IF NOT EXISTS exam_attempts (
            id           INTEGER  PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER  NOT NULL,
            exam_id      TEXT     NOT NULL,
            question_ids TEXT     NOT NULL,
            answers      TEXT     NOT NULL,
            score        INTEGER  NOT NULL,
            total        INTEGER  NOT NULL,
            passed       INTEGER  DEFAULT 0,
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_ea_user ON exam_attempts(user_id, exam_id);

        CREATE TABLE IF NOT EXISTS user_sessions (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER NOT NULL,
            session_id   TEXT NOT NULL UNIQUE,
            device_info  TEXT,
            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_active  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        CREATE INDEX IF NOT EXISTS idx_us_user ON user_sessions(user_id);
    """)
    db.commit()
    db.close()
