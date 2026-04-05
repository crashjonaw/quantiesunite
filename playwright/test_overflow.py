"""
Visual overflow tests — detect text/content spilling out of containers.
Includes SVG text boundary checks for diagrams and charts.
Issues are collected into debug.csv via the shared conftest collector.
"""

import pytest
from conftest import BASE_URL, add_issue
from urllib.parse import urlparse

# JS: finds all elements with visible overflow issues.
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


# JS: finds SVG <text> elements that extend beyond their parent SVG viewBox.
SVG_TEXT_OVERFLOW_JS = """
() => {
    const results = [];
    const svgs = document.querySelectorAll('.main-content svg');
    for (const svg of svgs) {
        // Get the effective coordinate system from viewBox or fallback to client size
        let svgX = 0, svgY = 0, svgW = 0, svgH = 0;
        const vbAttr = svg.getAttribute('viewBox');
        if (vbAttr) {
            const parts = vbAttr.trim().split(/[\\s,]+/).map(Number);
            if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) {
                svgX = parts[0];
                svgY = parts[1];
                svgW = parts[2];
                svgH = parts[3];
            }
        }
        if (svgW === 0 || svgH === 0) {
            // No viewBox — use pixel dimensions
            svgW = svg.clientWidth || parseFloat(svg.getAttribute('width')) || 0;
            svgH = svg.clientHeight || parseFloat(svg.getAttribute('height')) || 0;
        }
        if (svgW === 0 || svgH === 0) continue;

        // Skip KaTeX-generated SVGs (sqrt lines, frac lines)
        if (svg.closest('.katex') || svg.closest('.katex-display')) continue;

        const texts = svg.querySelectorAll('text');
        for (const t of texts) {
            try {
                // Skip text with transforms (rotated axis labels etc.)
                // getBBox returns untransformed coords which give false positives
                if (t.getAttribute('transform') || t.closest('g[transform]')) continue;

                const bbox = t.getBBox();
                // Allow 2px tolerance for anti-aliasing
                const tol = 2;
                const overLeft   = bbox.x < svgX - tol;
                const overRight  = bbox.x + bbox.width > svgX + svgW + tol;
                const overTop    = bbox.y < svgY - tol;
                const overBottom = bbox.y + bbox.height > svgY + svgH + tol;
                if (overLeft || overRight || overTop || overBottom) {
                    const dirs = [];
                    if (overLeft)   dirs.push('left');
                    if (overRight)  dirs.push('right');
                    if (overTop)    dirs.push('top');
                    if (overBottom) dirs.push('bottom');
                    results.push({
                        text: t.textContent.trim().substring(0, 60),
                        bboxX: Math.round(bbox.x),
                        bboxY: Math.round(bbox.y),
                        bboxW: Math.round(bbox.width),
                        bboxH: Math.round(bbox.height),
                        svgW: Math.round(svgW),
                        svgH: Math.round(svgH),
                        dirs: dirs.join('+'),
                        svgId: svg.id || '',
                        svgClass: svg.className.baseVal || '',
                    });
                }
            } catch(e) { /* getBBox can fail on hidden elements */ }
        }
    }
    return results;
}
"""

# JS: count total pages and return page count
PAGE_COUNT_JS = "() => typeof TOTAL_PAGES !== 'undefined' ? TOTAL_PAGES : 0"


def _collect_svg_text_overflows(page, url, page_label=""):
    """Check all SVG text elements on all paginated pages at a URL."""
    page.goto(url, wait_until="networkidle")
    path = urlparse(url).path

    # Get page count for pagination
    total_pages = page.evaluate(PAGE_COUNT_JS)
    pages_to_check = max(total_pages, 1)

    for pg in range(pages_to_check):
        if pg > 0:
            page.evaluate(f"goToPage({pg})")
            page.wait_for_timeout(300)

        hits = page.evaluate(SVG_TEXT_OVERFLOW_JS)

        for h in hits:
            label = f"p{pg}" if pages_to_check > 1 else ""
            if page_label:
                label = f"{page_label} {label}".strip()

            desc = (
                f"SVG text overflows {h['dirs']}:"
                f" \"{h['text']}\""
                f" bbox=({h['bboxX']},{h['bboxY']} {h['bboxW']}x{h['bboxH']})"
                f" svgSize=({h['svgW']}x{h['svgH']})"
            )
            if label:
                desc = f"[{label}] {desc}"

            title = f"SVG text overflow: \"{h['text'][:30]}\""
            if label:
                title += f" ({label})"

            add_issue(path, title, desc, "svg-text-overflow")


def _collect_overflows(page, url, viewport_label=""):
    page.goto(url, wait_until="networkidle")
    overflows = page.evaluate(OVERFLOW_CHECK_JS)
    path = urlparse(url).path

    for o in overflows:
        direction = []
        if o["overflowX"]:
            direction.append("horizontal")
        if o["overflowY"]:
            direction.append("vertical")

        desc = (
            f"Overflow ({' + '.join(direction)}) on <{o['tag']}>"
            f" class=\"{o['classes']}\" id=\"{o['id']}\"."
            f" scrollW={o['scrollW']} clientW={o['clientW']},"
            f" scrollH={o['scrollH']} clientH={o['clientH']}."
            f" Content: {o['text']!r}"
        )
        if viewport_label:
            desc = f"[{viewport_label}] {desc}"

        title = f"Overflow: <{o['tag']}>"
        if o["classes"] and isinstance(o["classes"], str):
            title += f".{o['classes'].split()[0]}"
        if viewport_label:
            title += f" ({viewport_label})"

        add_issue(path, title, desc, "overflow")


# ── Static pages ──────────────────────────────────────────────────

def test_homepage_overflow(logged_in_page):
    _collect_overflows(logged_in_page, BASE_URL)

def test_login_overflow(page):
    _collect_overflows(page, f"{BASE_URL}/login")

def test_register_overflow(page):
    _collect_overflows(page, f"{BASE_URL}/register")

def test_curriculum_overflow(logged_in_page):
    _collect_overflows(logged_in_page, f"{BASE_URL}/curriculum")

def test_account_overflow(logged_in_page):
    _collect_overflows(logged_in_page, f"{BASE_URL}/account")

def test_progress_overflow(logged_in_page):
    _collect_overflows(logged_in_page, f"{BASE_URL}/progress")

def test_search_overflow(logged_in_page):
    _collect_overflows(logged_in_page, f"{BASE_URL}/search?q=algebra")

def test_admin_overflow(logged_in_page):
    _collect_overflows(logged_in_page, f"{BASE_URL}/admin")


# ── Topic & quiz pages ───────────────────────────────────────────

SAMPLE_TOPICS = [
    "k_numbers", "p12_add_sub", "p34_fractions", "p56_percentage",
    "sec12_algebra", "olevel_quadratic", "alevel_complex",
]

@pytest.mark.parametrize("tid", SAMPLE_TOPICS)
def test_topic_overflow(logged_in_page, tid):
    _collect_overflows(logged_in_page, f"{BASE_URL}/topic/{tid}")

@pytest.mark.parametrize("tid", SAMPLE_TOPICS)
def test_quiz_overflow(logged_in_page, tid):
    _collect_overflows(logged_in_page, f"{BASE_URL}/topic/{tid}/quiz")


# ── Responsive viewports ─────────────────────────────────────────

VIEWPORTS = [
    (375, 812, "mobile"),
    (768, 1024, "tablet"),
    (1920, 1080, "desktop"),
]

@pytest.mark.parametrize("width,height,label", VIEWPORTS)
def test_homepage_responsive_overflow(browser, width, height, label):
    context = browser.new_context(viewport={"width": width, "height": height})
    p = context.new_page()
    p.goto(f"{BASE_URL}/login")
    p.fill('input[name="identifier"]', "admin")
    p.fill('input[name="password"]', "123456")
    p.click('button[type="submit"]')
    p.wait_for_url(f"{BASE_URL}/**")
    _collect_overflows(p, BASE_URL, f"{label} {width}x{height}")
    context.close()

@pytest.mark.parametrize("width,height,label", VIEWPORTS)
def test_topic_responsive_overflow(browser, width, height, label):
    context = browser.new_context(viewport={"width": width, "height": height})
    p = context.new_page()
    p.goto(f"{BASE_URL}/login")
    p.fill('input[name="identifier"]', "admin")
    p.fill('input[name="password"]', "123456")
    p.click('button[type="submit"]')
    p.wait_for_url(f"{BASE_URL}/**")
    _collect_overflows(p, f"{BASE_URL}/topic/k_numbers", f"{label} {width}x{height}")
    context.close()

@pytest.mark.parametrize("width,height,label", VIEWPORTS)
def test_curriculum_responsive_overflow(browser, width, height, label):
    context = browser.new_context(viewport={"width": width, "height": height})
    p = context.new_page()
    p.goto(f"{BASE_URL}/login")
    p.fill('input[name="identifier"]', "admin")
    p.fill('input[name="password"]', "123456")
    p.click('button[type="submit"]')
    p.wait_for_url(f"{BASE_URL}/**")
    _collect_overflows(p, f"{BASE_URL}/curriculum", f"{label} {width}x{height}")
    context.close()


# ── SVG text overflow detection ─────────────────────────────────

# Discovers all concept learn pages for a module by scanning links on the topic page.
DISCOVER_CONCEPT_URLS_JS = """
(baseUrl) => {
    const links = document.querySelectorAll('a[href*="/learn/"]');
    const urls = [];
    for (const a of links) {
        const href = a.getAttribute('href');
        if (href && href.includes('/learn/')) {
            urls.push(new URL(href, baseUrl).href);
        }
    }
    return [...new Set(urls)];
}
"""

# All modules known to contain SVG diagrams in lesson content
SVG_TOPICS = [
    "k_numbers", "k_addition", "k_counting", "k_shapes", "k_subtraction",
    "p12_add_sub", "p12_divide", "p12_fractions_basic", "p12_measurement",
    "p12_multiply", "p12_time", "p12_whole_1000",
    "p34_all_tables", "p34_angles", "p34_data", "p34_decimals",
    "p34_fractions", "p34_perimeter_area", "p34_symmetry", "p34_whole_100k",
    "p56_average", "p56_fractions_adv", "p56_percentage",
    "p56_problem_solving", "p56_ratio", "p56_volume",
    "sec12_algebra", "sec12_coordinates", "sec12_geometry",
    "sec12_indices", "sec12_probability", "sec12_pythagoras", "sec12_statistics",
    "olevel_circles", "olevel_graphs", "olevel_inequalities", "olevel_matrices",
    "olevel_prob_adv", "olevel_sets", "olevel_trigonometry", "olevel_vectors2d",
    "alevel_functions", "amath_binomial", "la_systems",
]


@pytest.mark.parametrize("tid", SVG_TOPICS)
def test_svg_text_overflow(logged_in_page, tid):
    """Visit every concept page for this topic and check SVG text bounds."""
    # First discover all concept URLs from the topic overview
    logged_in_page.goto(f"{BASE_URL}/topic/{tid}", wait_until="networkidle")
    concept_urls = logged_in_page.evaluate(DISCOVER_CONCEPT_URLS_JS, BASE_URL)

    if not concept_urls:
        return  # No concept pages found (module might not have learn pages)

    for url in concept_urls:
        _collect_svg_text_overflows(logged_in_page, url)
