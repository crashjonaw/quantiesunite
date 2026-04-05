"""
Visual & layout tests — broken images, overlapping elements, empty containers,
z-index issues. Issues are collected into debug.csv via the shared conftest.
"""

import pytest
from conftest import BASE_URL, add_issue
from urllib.parse import urlparse

ALL_TOPICS = [
    "alevel_complex", "alevel_counting", "alevel_de", "alevel_diff_adv",
    "alevel_distributions", "alevel_functions", "alevel_hypothesis",
    "alevel_int_adv", "alevel_regression", "alevel_sequences", "alevel_vectors3d",
    "amath_binomial", "amath_diff_intro", "amath_exp_log", "amath_int_intro",
    "amath_polynomials", "amath_trig_adv",
    "dl_activations", "dl_attention", "dl_backprop", "dl_gradient", "dl_loss",
    "dl_lstm", "dl_modern_lm", "dl_neural_nets", "dl_rnn", "dl_self_attention",
    "dl_sequence", "dl_transformer",
    "k_addition", "k_counting", "k_numbers", "k_shapes", "k_subtraction",
    "la_determinants", "la_eigenvalues", "la_gauss", "la_linear_trans",
    "la_matrix_ops", "la_orthogonality", "la_svd", "la_systems", "la_vector_spaces",
    "olevel_circles", "olevel_graphs", "olevel_inequalities", "olevel_matrices",
    "olevel_prob_adv", "olevel_quadratic", "olevel_sets", "olevel_stats_adv",
    "olevel_trigonometry", "olevel_vectors2d",
    "p12_add_sub", "p12_divide", "p12_fractions_basic", "p12_measurement",
    "p12_multiply", "p12_time", "p12_whole_1000",
    "p34_all_tables", "p34_angles", "p34_data", "p34_decimals", "p34_fractions",
    "p34_long_mult_div", "p34_perimeter_area", "p34_symmetry", "p34_whole_100k",
    "p56_algebra_intro", "p56_average", "p56_data_analysis", "p56_fractions_adv",
    "p56_percentage", "p56_problem_solving", "p56_ratio", "p56_volume",
    "ps_bayesian", "ps_clt", "ps_expectation", "ps_inference", "ps_markov",
    "ps_probability", "ps_random_vars",
    "py_basics", "py_control", "py_data_structs", "py_functions", "py_matplotlib",
    "py_numpy", "py_oop", "py_pandas", "py_scipy",
    "sec12_algebra", "sec12_coordinates", "sec12_geometry", "sec12_indices",
    "sec12_probability", "sec12_pythagoras", "sec12_simultaneous", "sec12_statistics",
]


# ═══════════════════════════════════════════════════════════════════
# JS CHECKS
# ═══════════════════════════════════════════════════════════════════

# 1. Broken images — <img> that failed to load
BROKEN_IMAGES_JS = """
() => {
    const results = [];
    for (const img of document.querySelectorAll('img')) {
        if (!img.complete || img.naturalWidth === 0) {
            results.push({
                src: img.src || img.getAttribute('src') || '(no src)',
                alt: img.alt || '',
                classes: img.className || '',
                id: img.id || '',
            });
        }
    }
    return results;
}
"""

# 2. Overlapping elements — key containers whose bounding boxes collide
OVERLAP_CHECK_JS = """
() => {
    const results = [];
    const selectors = [
        '.lesson-section', '.concept-card', '.topic-card', '.stat-card',
        '.path-card', '.feature-card', '.account-section', '.admin-stat-card',
        '.mindmap-concept', '.formula-item', '.quiz-question',
        '.sidebar-concept', '.lp-card', '.target-card',
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
            // Only compare siblings with same selector
            if (els[i].sel !== els[j].sel) continue;
            if (els[i].el.parentElement !== els[j].el.parentElement) continue;
            const a = els[i].rect, b = els[j].rect;
            const overlapX = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
            const overlapY = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
            const overlapArea = overlapX * overlapY;
            const minArea = Math.min(a.width * a.height, b.width * b.height);
            // Flag if overlap is more than 10% of the smaller element
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

# 3. Empty containers — visible elements that should have content but don't
EMPTY_CONTAINERS_JS = """
() => {
    const results = [];
    const selectors = [
        '.section-body', '.rich-content', '.lesson-section',
        '.concept-card', '.quiz-question', '.mindmap-concept',
    ];
    for (const sel of selectors) {
        for (const el of document.querySelectorAll(sel)) {
            const style = getComputedStyle(el);
            if (style.display === 'none' || style.visibility === 'hidden') continue;
            const text = el.textContent.trim();
            const hasImages = el.querySelectorAll('img, svg, canvas').length > 0;
            if (!text && !hasImages) {
                results.push({
                    sel: sel,
                    classes: el.className || '',
                    id: el.id || '',
                    parent: el.parentElement ? el.parentElement.className : '',
                });
            }
        }
    }
    return results;
}
"""

# 4. Z-index / hidden elements — important elements obscured by others
ZINDEX_CHECK_JS = """
() => {
    const results = [];
    const important = document.querySelectorAll(
        'button, a.btn, .feedback-fab, nav, .page-nav-btn'
    );
    for (const el of important) {
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) continue;
        const style = getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden') continue;
        // Check if center point is covered by another element
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const topEl = document.elementFromPoint(cx, cy);
        if (topEl && topEl !== el && !el.contains(topEl) && !topEl.contains(el)) {
            results.push({
                blocked: el.tagName.toLowerCase() + (el.className ? '.' + el.className.split(' ')[0] : ''),
                blockedText: el.textContent.substring(0, 40).trim(),
                blocker: topEl.tagName.toLowerCase() + (topEl.className ? '.' + topEl.className.split(' ')[0] : ''),
                blockerText: topEl.textContent.substring(0, 40).trim(),
            });
        }
    }
    return results;
}
"""


# ═══════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════

def _scan_page(page, url):
    """Run all visual checks on a page and collect issues."""
    page.goto(url, wait_until="networkidle")
    path = urlparse(url).path

    # Broken images
    broken = page.evaluate(BROKEN_IMAGES_JS)
    for img in broken:
        add_issue(
            path,
            f"Broken image: {img['src'][:50]}",
            f"Image failed to load. src=\"{img['src']}\" alt=\"{img['alt']}\""
            f" class=\"{img['classes']}\" id=\"{img['id']}\"",
            "broken-image",
        )

    # Overlapping elements
    overlaps = page.evaluate(OVERLAP_CHECK_JS)
    for o in overlaps:
        add_issue(
            path,
            f"Overlap: {o['sel']} ({o['overlapPct']}%)",
            f"Sibling {o['sel']} elements overlap by {o['overlapPct']}%."
            f" Element A: {o['elA']!r}. Element B: {o['elB']!r}",
            "overlap",
        )

    # Empty containers
    empties = page.evaluate(EMPTY_CONTAINERS_JS)
    for e in empties:
        add_issue(
            path,
            f"Empty container: {e['sel']}",
            f"Visible {e['sel']} element has no text or media content."
            f" class=\"{e['classes']}\" id=\"{e['id']}\""
            f" parent class=\"{e['parent']}\"",
            "empty-container",
        )

    # Z-index / hidden behind
    zissues = page.evaluate(ZINDEX_CHECK_JS)
    for z in zissues:
        add_issue(
            path,
            f"Hidden behind: {z['blocked']}",
            f"Interactive element {z['blocked']} (\"{z['blockedText']}\")"
            f" is obscured by {z['blocker']} (\"{z['blockerText']}\").",
            "z-index",
        )


# ═══════════════════════════════════════════════════════════════════
# TESTS — STATIC PAGES
# ═══════════════════════════════════════════════════════════════════

STATIC_PAGES = [
    ("/", "Homepage"),
    ("/curriculum", "Curriculum"),
    ("/account", "Account"),
    ("/progress", "Progress"),
    ("/search?q=algebra", "Search"),
    ("/admin", "Admin"),
]


@pytest.mark.parametrize("path,label", STATIC_PAGES)
def test_static_page_visual(logged_in_page, path, label):
    _scan_page(logged_in_page, f"{BASE_URL}{path}")


# ═══════════════════════════════════════════════════════════════════
# TESTS — ALL TOPIC PAGES (concept/lesson view)
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_topic_visual(logged_in_page, tid):
    _scan_page(logged_in_page, f"{BASE_URL}/topic/{tid}")


# ═══════════════════════════════════════════════════════════════════
# TESTS — ALL QUIZ PAGES
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_quiz_visual(logged_in_page, tid):
    _scan_page(logged_in_page, f"{BASE_URL}/topic/{tid}/quiz")
