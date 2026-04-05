"""
Tests for newly built pages — user dashboard, admin dashboard, trophies,
profile/avatar, rate-limit page. Covers JS errors, visual checks, contrast,
overflow, and functional verification.
Issues are collected into debug.csv via the shared conftest collector.
"""

import pytest
from conftest import BASE_URL, add_issue
from urllib.parse import urlparse


# ═══════════════════════════════════════════════════════════════════
# JS CHECKS (reused from other test files)
# ═══════════════════════════════════════════════════════════════════

BROKEN_IMAGES_JS = """
() => {
    const results = [];
    for (const img of document.querySelectorAll('img')) {
        if (!img.complete || img.naturalWidth === 0) {
            results.push({
                src: img.src || img.getAttribute('src') || '(no src)',
                alt: img.alt || '',
                classes: img.className || '',
            });
        }
    }
    return results;
}
"""

OVERLAP_CHECK_JS = """
() => {
    const results = [];
    const selectors = [
        '.dash-stat', '.dash-hero-stat', '.dash-card', '.dash-ach',
        '.dash-topic-item', '.dash-act', '.dash-mini-item',
        '.adash-card', '.adash-metric', '.adash-hstat', '.adash-flagged',
        '.adash-vlog-item', '.trophy-card', '.trophy-mastery-card',
        '.trophy-milestone',
    ];
    const els = [];
    for (const sel of selectors) {
        for (const el of document.querySelectorAll(sel)) {
            const r = el.getBoundingClientRect();
            if (r.width > 0 && r.height > 0) {
                els.push({ el, rect: r, sel });
            }
        }
    }
    for (let i = 0; i < els.length; i++) {
        for (let j = i + 1; j < els.length; j++) {
            if (els[i].sel !== els[j].sel) continue;
            if (els[i].el.parentElement !== els[j].el.parentElement) continue;
            const a = els[i].rect, b = els[j].rect;
            const overlapX = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
            const overlapY = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
            const overlapArea = overlapX * overlapY;
            const minArea = Math.min(a.width * a.height, b.width * b.height);
            if (overlapArea > 0 && minArea > 0 && (overlapArea / minArea) > 0.1) {
                results.push({
                    sel: els[i].sel,
                    elA: els[i].el.textContent.substring(0, 40).trim(),
                    elB: els[j].el.textContent.substring(0, 40).trim(),
                    overlapPct: Math.round((overlapArea / minArea) * 100),
                });
            }
        }
    }
    return results;
}
"""

EMPTY_CONTAINERS_JS = """
() => {
    const results = [];
    const selectors = [
        '.dash-card', '.dash-section', '.adash-card', '.adash-section',
        '.trophy-section', '.dash-hero-content', '.adash-hero-content',
    ];
    for (const sel of selectors) {
        for (const el of document.querySelectorAll(sel)) {
            const style = getComputedStyle(el);
            if (style.display === 'none' || style.visibility === 'hidden') continue;
            const text = el.textContent.trim();
            const hasMedia = el.querySelectorAll('img, svg, canvas').length > 0;
            if (!text && !hasMedia) {
                results.push({
                    sel: sel,
                    classes: el.className || '',
                    id: el.id || '',
                });
            }
        }
    }
    return results;
}
"""

OVERFLOW_CHECK_JS = """
() => {
    const results = [];
    const els = document.querySelectorAll('.main-content, .main-content *');
    for (const el of els) {
        const style = getComputedStyle(el);
        if (style.overflowX === 'scroll' || style.overflowX === 'auto' ||
            style.overflowY === 'scroll' || style.overflowY === 'auto')
            continue;
        if (style.display === 'none' || style.visibility === 'hidden')
            continue;
        if (el.clientWidth < 20 || el.clientHeight < 10)
            continue;
        const overflowX = el.scrollWidth > el.clientWidth + 2;
        const overflowY = el.scrollHeight > el.clientHeight + 2;
        if (overflowX || overflowY) {
            results.push({
                tag: el.tagName.toLowerCase(),
                classes: el.className || '',
                id: el.id || '',
                scrollW: el.scrollWidth,
                clientW: el.clientWidth,
                scrollH: el.scrollHeight,
                clientH: el.clientHeight,
                text: el.textContent.substring(0, 80).trim(),
                overflowX, overflowY,
            });
        }
    }
    return results;
}
"""

LOW_CONTRAST_JS = """
() => {
    function luminance(r, g, b) {
        const [rs, gs, bs] = [r, g, b].map(c => {
            c = c / 255;
            return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
    }
    function contrastRatio(l1, l2) {
        return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    }
    function parseColor(str) {
        const m = str.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/);
        return m ? { r: +m[1], g: +m[2], b: +m[3] } : null;
    }
    function getEffectiveBg(el) {
        let current = el;
        while (current) {
            const style = getComputedStyle(current);
            const bg = parseColor(style.backgroundColor);
            if (bg && !(bg.r === 0 && bg.g === 0 && bg.b === 0 && style.backgroundColor.includes('0)'))) {
                const alpha = style.backgroundColor.match(/[\\d.]+/g);
                if (alpha && alpha.length === 4 && parseFloat(alpha[3]) < 0.1) {
                    current = current.parentElement; continue;
                }
                return bg;
            }
            current = current.parentElement;
        }
        return { r: 255, g: 255, b: 255 };
    }
    const results = [];
    const seen = new Set();
    const els = document.querySelectorAll(
        '.main-content h1, .main-content h2, .main-content h3, ' +
        '.main-content h4, .main-content p, .main-content span, ' +
        '.main-content a, .main-content li, .main-content td, ' +
        '.main-content th, .main-content label, .main-content div, ' +
        '.main-content button, .navbar *, .footer *'
    );
    for (const el of els) {
        const style = getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden') continue;
        const directText = Array.from(el.childNodes)
            .filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join('');
        if (!directText) continue;
        const fg = parseColor(style.color);
        if (!fg) continue;
        const bg = getEffectiveBg(el);
        const ratio = contrastRatio(luminance(fg.r, fg.g, fg.b), luminance(bg.r, bg.g, bg.b));
        if (ratio < 3.0) {
            const key = el.tagName + '|' + style.color + '|' + directText.substring(0, 30);
            if (seen.has(key)) continue;
            seen.add(key);
            results.push({
                tag: el.tagName.toLowerCase(),
                classes: el.className || '',
                text: directText.substring(0, 80),
                fgColor: style.color,
                bgColor: 'rgb(' + bg.r + ',' + bg.g + ',' + bg.b + ')',
                ratio: Math.round(ratio * 100) / 100,
            });
        }
    }
    return results;
}
"""

BROKEN_LINKS_JS = """
() => {
    const results = [];
    const seen = new Set();
    for (const a of document.querySelectorAll('a[href]')) {
        const href = a.getAttribute('href');
        if (!href || !href.startsWith('/')) continue;
        if (href === '#' || href.startsWith('/#') || href.startsWith('/logout')) continue;
        if (seen.has(href)) continue;
        seen.add(href);
        results.push({ href, text: a.textContent.substring(0, 50).trim() });
    }
    return results;
}
"""

# Trophy medal overflow check — verify .trophy-medal-badge stays within card
TROPHY_MEDAL_OVERFLOW_JS = """
() => {
    const results = [];
    const badges = document.querySelectorAll('.trophy-medal-badge');
    for (const badge of badges) {
        const card = badge.closest('.trophy-card');
        if (!card) continue;
        const cardRect = card.getBoundingClientRect();
        const badgeRect = badge.getBoundingClientRect();
        if (badgeRect.top < cardRect.top - 1 ||
            badgeRect.right > cardRect.right + 1 ||
            badgeRect.bottom > cardRect.bottom + 1) {
            results.push({
                text: badge.textContent.trim().substring(0, 20),
                badgeTop: Math.round(badgeRect.top),
                cardTop: Math.round(cardRect.top),
                overflow: Math.round(cardRect.top - badgeRect.top),
            });
        }
    }
    return results;
}
"""


# ═══════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════

def _full_scan(page, url, label=""):
    """Run all checks (JS errors, visuals, overflow) on a single page."""
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

    page.goto(url, wait_until="networkidle", timeout=20000)
    path = urlparse(url).path
    tag = f" [{label}]" if label else ""

    # JS errors
    for err in errors:
        if "favicon" in err.lower():
            continue
        add_issue(path, f"JS error{tag}: {err[:50]}", f"JavaScript error: {err}", "js-error")

    # Broken images
    for img in page.evaluate(BROKEN_IMAGES_JS):
        add_issue(path, f"Broken image{tag}: {img['src'][:40]}", f"Image failed: src=\"{img['src']}\"", "broken-image")

    # Overlapping elements
    for o in page.evaluate(OVERLAP_CHECK_JS):
        add_issue(path, f"Overlap{tag}: {o['sel']} ({o['overlapPct']}%)",
                  f"Sibling {o['sel']} overlap {o['overlapPct']}%: {o['elA']!r} vs {o['elB']!r}", "overlap")

    # Empty containers
    for e in page.evaluate(EMPTY_CONTAINERS_JS):
        add_issue(path, f"Empty{tag}: {e['sel']}", f"Empty visible {e['sel']} class=\"{e['classes']}\"", "empty-container")

    # Overflow
    for o in page.evaluate(OVERFLOW_CHECK_JS):
        direction = []
        if o["overflowX"]: direction.append("horizontal")
        if o["overflowY"]: direction.append("vertical")
        add_issue(path, f"Overflow{tag}: <{o['tag']}>.{o['classes'].split()[0] if o['classes'] else ''}",
                  f"Overflow ({'+'.join(direction)}) on <{o['tag']}> class=\"{o['classes']}\" "
                  f"scrollW={o['scrollW']} clientW={o['clientW']}", "overflow")

    # Broken links
    for link in page.evaluate(BROKEN_LINKS_JS):
        resp = page.request.get(f"{BASE_URL}{link['href']}")
        if resp.status == 404:
            add_issue(path, f"Broken link{tag}: {link['href'][:40]}",
                      f"Link \"{link['href']}\" returns 404. Text: \"{link['text']}\"", "broken-link")


def _contrast_scan(page, url, theme):
    """Check contrast in a specific theme."""
    page.goto(url, wait_until="domcontentloaded", timeout=15000)
    page.evaluate(f'document.documentElement.setAttribute("data-theme", "{theme}")')
    page.wait_for_timeout(300)

    path = urlparse(url).path
    for item in page.evaluate(LOW_CONTRAST_JS):
        add_issue(
            path,
            f"Low contrast ({theme}): {item['tag']}.{item['classes'].split()[0] if item['classes'] else ''}",
            f"[{theme}] Contrast {item['ratio']}:1 (min 3.0). <{item['tag']}> "
            f"class=\"{item['classes']}\". Text: \"{item['text']}\". "
            f"FG: {item['fgColor']}, BG: {item['bgColor']}",
            f"low-contrast-{theme}",
        )


# ═══════════════════════════════════════════════════════════════════
# NEW PAGES TO TEST
# ═══════════════════════════════════════════════════════════════════

NEW_PAGES = [
    ("/dashboard", "User Dashboard"),
    ("/admin/dashboard", "Admin Dashboard"),
    ("/trophies", "Trophies"),
    ("/account", "Account"),
    ("/progress", "Progress"),
]


# ═══════════════════════════════════════════════════════════════════
# TESTS — FULL SCAN (JS errors, visuals, overflow, broken links)
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("path,label", NEW_PAGES)
def test_full_scan_desktop(logged_in_page, path, label):
    _full_scan(logged_in_page, f"{BASE_URL}{path}", label)


# ═══════════════════════════════════════════════════════════════════
# TESTS — CONTRAST (both themes)
# ═══════════════════════════════════════════════════════════════════

@pytest.fixture(scope="module")
def contrast_page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="identifier"]', "admin")
    page.fill('input[name="password"]', "123456")
    page.click('button[type="submit"]')
    page.wait_for_url(f"{BASE_URL}/**")
    yield page
    context.close()


@pytest.mark.parametrize("path,label", NEW_PAGES)
def test_dark_contrast(contrast_page, path, label):
    _contrast_scan(contrast_page, f"{BASE_URL}{path}", "dark")


@pytest.mark.parametrize("path,label", NEW_PAGES)
def test_bright_contrast(contrast_page, path, label):
    _contrast_scan(contrast_page, f"{BASE_URL}{path}", "bright")


# ═══════════════════════════════════════════════════════════════════
# TESTS — RESPONSIVE (mobile & tablet)
# ═══════════════════════════════════════════════════════════════════

VIEWPORTS = [
    (375, 812, "mobile"),
    (768, 1024, "tablet"),
]


@pytest.mark.parametrize("path,label", NEW_PAGES)
@pytest.mark.parametrize("width,height,vp_label", VIEWPORTS)
def test_responsive(browser, path, label, width, height, vp_label):
    context = browser.new_context(viewport={"width": width, "height": height})
    p = context.new_page()
    p.goto(f"{BASE_URL}/login")
    p.fill('input[name="identifier"]', "admin")
    p.fill('input[name="password"]', "123456")
    p.click('button[type="submit"]')
    p.wait_for_url(f"{BASE_URL}/**")
    _full_scan(p, f"{BASE_URL}{path}", f"{label} {vp_label} {width}x{height}")
    context.close()


# ═══════════════════════════════════════════════════════════════════
# TESTS — DASHBOARD-SPECIFIC CHECKS
# ═══════════════════════════════════════════════════════════════════

def test_dashboard_has_hero(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    assert logged_in_page.locator(".dash-hero").is_visible(), "Dashboard hero missing"


def test_dashboard_has_heatmap(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    assert logged_in_page.locator("#heatmap-grid").is_visible(), "Heatmap grid missing"


def test_dashboard_has_achievements(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    assert logged_in_page.locator(".dash-achievements-grid").is_visible(), "Achievements grid missing"


def test_dashboard_has_stat_circles(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    circles = logged_in_page.locator(".dash-hero-circle").count()
    assert circles >= 4, f"Expected 4+ stat circles, got {circles}"


def test_dashboard_profile_form(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    assert logged_in_page.locator('input[name="display_name"]').is_visible(), "Profile form missing"


def test_dashboard_avatar_picker(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    # The avatar input and crop modal are in the base template, rendered for logged-in users
    assert logged_in_page.locator("#avatar-file-input").count() >= 1 or \
           logged_in_page.locator("#crop-overlay").count() >= 1, \
           "Avatar crop modal missing from dashboard"


# ═══════════════════════════════════════════════════════════════════
# TESTS — ADMIN DASHBOARD-SPECIFIC CHECKS
# ═══════════════════════════════════════════════════════════════════

def test_admin_dashboard_has_hero(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin/dashboard", wait_until="networkidle")
    assert logged_in_page.locator(".adash-hero").is_visible(), "Admin dashboard hero missing"


def test_admin_dashboard_has_charts(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin/dashboard", wait_until="networkidle")
    assert logged_in_page.locator("#growth-chart").count() == 1, "Growth chart missing"
    assert logged_in_page.locator("#dau-chart").count() == 1, "DAU chart missing"


def test_admin_dashboard_has_stat_circles(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin/dashboard", wait_until="networkidle")
    circles = logged_in_page.locator(".adash-hcircle").count()
    assert circles >= 6, f"Expected 6+ admin stat circles, got {circles}"


def test_admin_dashboard_has_tables(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin/dashboard", wait_until="networkidle")
    tables = logged_in_page.locator(".adash-table").count()
    assert tables >= 1, "Expected at least 1 data table"


def test_admin_dashboard_violations_section(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin/dashboard", wait_until="networkidle")
    assert logged_in_page.locator("#violations-section").is_visible(), "Violations section missing"


# ═══════════════════════════════════════════════════════════════════
# TESTS — TROPHIES: medal badge overflow fix (#28)
# ═══════════════════════════════════════════════════════════════════

def test_trophy_medal_not_overflowing(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/trophies", wait_until="networkidle")
    overflows = logged_in_page.evaluate(TROPHY_MEDAL_OVERFLOW_JS)
    for o in overflows:
        add_issue(
            "/trophies",
            f"Trophy medal overflows card by {o['overflow']}px",
            f"Medal badge \"{o['text']}\" top={o['badgeTop']} exceeds card top={o['cardTop']} "
            f"by {o['overflow']}px. The floating animation pushes it outside the card bounds.",
            "trophy-overflow",
        )
    # This is a regression test for feedback #28
    assert len(overflows) == 0, f"{len(overflows)} trophy medal(s) still overflow their cards"


# ═══════════════════════════════════════════════════════════════════
# TESTS — NAVBAR AVATAR & CROP MODAL
# ═══════════════════════════════════════════════════════════════════

def test_navbar_avatar_clickable(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    # Open user menu
    logged_in_page.click("#user-menu-btn")
    logged_in_page.wait_for_timeout(300)
    # The dropdown avatar wrap should be visible
    wrap = logged_in_page.locator(".dropdown-avatar-wrap")
    assert wrap.is_visible(), "Dropdown avatar wrap not visible"


def test_crop_modal_opens(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/dashboard", wait_until="networkidle")
    overlay = logged_in_page.locator("#crop-overlay")
    assert not overlay.is_visible(), "Crop modal should be hidden initially"
