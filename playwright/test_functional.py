"""
Functional tests — broken links, JS console errors, KaTeX render failures.
Issues are collected into debug.csv via the shared conftest collector.
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

# Broken internal links — <a> with href starting with / that might 404
BROKEN_LINKS_JS = """
() => {
    const results = [];
    const seen = new Set();
    for (const a of document.querySelectorAll('a[href]')) {
        const href = a.getAttribute('href');
        if (!href || !href.startsWith('/')) continue;
        // Skip anchors and JS links
        if (href === '#' || href.startsWith('/#') || href.startsWith('/logout')) continue;
        if (seen.has(href)) continue;
        seen.add(href);
        results.push({
            href: href,
            text: a.textContent.substring(0, 50).trim(),
        });
    }
    return results;
}
"""

# KaTeX render errors — elements with class .katex-error
KATEX_ERRORS_JS = """
() => {
    const results = [];
    for (const el of document.querySelectorAll('.katex-error')) {
        const parent = el.closest('.lesson-section, .section-body, .quiz-question');
        results.push({
            title: el.getAttribute('title') || '',
            text: el.textContent.substring(0, 80).trim(),
            parentClass: parent ? parent.className : '',
            parentId: parent ? (parent.id || '') : '',
        });
    }
    return results;
}
"""


# ═══════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════

def _check_js_errors(page, url):
    """Load page while capturing console errors."""
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

    page.goto(url, wait_until="networkidle")
    path = urlparse(url).path

    for err in errors:
        # Skip common non-actionable errors
        if "favicon" in err.lower():
            continue
        add_issue(
            path,
            f"JS error: {err[:50]}",
            f"JavaScript console error: {err}",
            "js-error",
        )

    return path


def _check_broken_links(page, path):
    """Check all internal links on the current page for 404s."""
    links = page.evaluate(BROKEN_LINKS_JS)
    for link in links:
        resp = page.request.get(f"{BASE_URL}{link['href']}")
        if resp.status == 404:
            add_issue(
                path,
                f"Broken link: {link['href'][:50]}",
                f"Link to \"{link['href']}\" returns 404."
                f" Link text: \"{link['text']}\"",
                "broken-link",
            )


def _check_katex_errors(page, path):
    """Check for KaTeX render failures."""
    katex_errors = page.evaluate(KATEX_ERRORS_JS)
    for k in katex_errors:
        add_issue(
            path,
            f"KaTeX error: {k['text'][:50]}",
            f"KaTeX failed to render: \"{k['text']}\"."
            f" Error: \"{k['title']}\"."
            f" Parent: class=\"{k['parentClass']}\" id=\"{k['parentId']}\"",
            "katex-error",
        )


# ═══════════════════════════════════════════════════════════════════
# TESTS — JS ERRORS & KATEX ON STATIC PAGES
# ═══════════════════════════════════════════════════════════════════

STATIC_PAGES = [
    ("/", "Homepage"),
    ("/curriculum", "Curriculum"),
    ("/account", "Account"),
    ("/progress", "Progress"),
    ("/admin", "Admin"),
]


@pytest.mark.parametrize("path_str,label", STATIC_PAGES)
def test_static_js_errors(logged_in_page, path_str, label):
    _check_js_errors(logged_in_page, f"{BASE_URL}{path_str}")


# ═══════════════════════════════════════════════════════════════════
# TESTS — BROKEN LINKS (checked on key pages with many links)
# ═══════════════════════════════════════════════════════════════════

def test_homepage_broken_links(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/", wait_until="networkidle")
    _check_broken_links(logged_in_page, "/")


def test_curriculum_broken_links(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/curriculum", wait_until="networkidle")
    _check_broken_links(logged_in_page, "/curriculum")


def test_progress_broken_links(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/progress", wait_until="networkidle")
    _check_broken_links(logged_in_page, "/progress")


def test_admin_broken_links(logged_in_page):
    logged_in_page.goto(f"{BASE_URL}/admin", wait_until="networkidle")
    _check_broken_links(logged_in_page, "/admin")


# ═══════════════════════════════════════════════════════════════════
# TESTS — ALL TOPICS: JS errors + KaTeX errors
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_topic_js_and_katex(logged_in_page, tid):
    path = _check_js_errors(logged_in_page, f"{BASE_URL}/topic/{tid}")
    _check_katex_errors(logged_in_page, path)


@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_quiz_js_and_katex(logged_in_page, tid):
    path = _check_js_errors(logged_in_page, f"{BASE_URL}/topic/{tid}/quiz")
    _check_katex_errors(logged_in_page, path)


# ═══════════════════════════════════════════════════════════════════
# TESTS — TOPIC PAGES: broken links
# ═══════════════════════════════════════════════════════════════════

SAMPLE_TOPICS_FOR_LINKS = [
    "k_numbers", "p12_add_sub", "p34_fractions", "p56_percentage",
    "sec12_algebra", "olevel_quadratic", "alevel_complex",
    "la_matrix_ops", "ps_probability", "py_basics", "dl_neural_nets",
]


@pytest.mark.parametrize("tid", SAMPLE_TOPICS_FOR_LINKS)
def test_topic_broken_links(logged_in_page, tid):
    logged_in_page.goto(f"{BASE_URL}/topic/{tid}", wait_until="networkidle")
    path = urlparse(logged_in_page.url).path
    _check_broken_links(logged_in_page, path)
