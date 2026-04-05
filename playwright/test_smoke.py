"""
Basic smoke tests — verify core pages load and key flows work.
Run: pytest playwright/ -v
"""

from conftest import BASE_URL


def test_homepage_loads(page):
    page.goto(BASE_URL)
    assert page.title()
    assert page.locator("body").is_visible()


def test_login_page_loads(page):
    page.goto(f"{BASE_URL}/login")
    assert page.locator('input[name="identifier"]').is_visible()
    assert page.locator('input[name="password"]').is_visible()


def test_login_flow(page):
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="identifier"]', "admin")
    page.fill('input[name="password"]', "123456")
    page.click('button[type="submit"]')
    page.wait_for_url(f"{BASE_URL}/**")
    # Should not be on the login page anymore
    assert "/login" not in page.url


def test_curriculum_page(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/curriculum")
    assert logged_in_page.locator("body").is_visible()


def test_graph_page(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/graph")
    assert logged_in_page.locator("#graph-ui").is_visible()


def test_account_page(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/account")
    assert logged_in_page.locator("body").is_visible()


def test_search(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/search?q=algebra")
    assert logged_in_page.locator("body").is_visible()
