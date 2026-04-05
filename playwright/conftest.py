"""
Shared fixtures and debug.csv collector for Playwright tests.
Assumes the Flask app is already running on http://localhost:5001.
Start it with: python app.py (or ./run.sh)
"""

import csv
import os
import re
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:5001"
DEBUG_CSV = os.path.join(os.path.dirname(__file__), "debug.csv")

COLUMNS = [
    "#", "user", "page_link", "module", "topic", "title", "description",
    "priority", "category", "submitted_at", "fix_summary", "fixed?",
    "fixed_at", "fixed_by",
]

# Shared issue list — all test files append here
issues = []


def _extract_module_topic(page_url):
    """Parse module ID and label from a page URL."""
    m = re.match(r"/topic/([^/]+)", page_url)
    if m:
        return m.group(1), m.group(1).replace("_", " ").title()
    return "", ""


def add_issue(page_link, title, description, category):
    """Append an issue to the shared list."""
    issues.append({
        "page_link": page_link,
        "title": title[:60] + ("..." if len(title) > 60 else ""),
        "description": description,
        "category": category,
    })


def pytest_sessionfinish(session, exitstatus):
    """Write all collected issues to debug.csv after all tests complete."""
    with open(DEBUG_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i, issue in enumerate(issues, start=1):
            module_id, topic_name = _extract_module_topic(issue["page_link"])
            writer.writerow([
                i,                          # #
                "playwright",               # user
                issue["page_link"],         # page_link
                module_id,                  # module
                topic_name,                 # topic
                issue["title"],             # title
                issue["description"],       # description
                "",                         # priority
                issue["category"],          # category
                now,                        # submitted_at
                "",                         # fix_summary
                "no",                       # fixed?
                "",                         # fixed_at
                "",                         # fixed_by
            ])

    count = len(issues)
    if count:
        print(f"\n[debug.csv] {count} issue(s) written to {DEBUG_CSV}")
    else:
        print(f"\n[debug.csv] No issues found. Clean CSV at {DEBUG_CSV}")


# ── Fixtures ──────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def logged_in_page(browser):
    """A page that is already logged in as the default admin."""
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="identifier"]', "admin")
    page.fill('input[name="password"]', "123456")
    page.click('button[type="submit"]')
    page.wait_for_url(f"{BASE_URL}/**")
    yield page
    context.close()
