"""
Contrast tests — detect text that is invisible or nearly invisible against
its background, especially in light (bright) theme mode.
Issues are collected into debug.csv via the shared conftest collector.
"""

import pytest
from conftest import BASE_URL, add_issue
from urllib.parse import urlparse


@pytest.fixture(scope="module")
def contrast_page(browser):
    """Single logged-in page reused across all contrast tests."""
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"{BASE_URL}/login")
    page.fill('input[name="identifier"]', "admin")
    page.fill('input[name="password"]', "123456")
    page.click('button[type="submit"]')
    page.wait_for_url(f"{BASE_URL}/**")
    yield page
    context.close()

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

# JS: compute relative luminance and contrast ratio per WCAG 2.0
# Returns elements where text contrast ratio < 3.0 (very hard to read)
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
        const lighter = Math.max(l1, l2);
        const darker = Math.min(l1, l2);
        return (lighter + 0.05) / (darker + 0.05);
    }

    function parseColor(str) {
        const m = str.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)/);
        if (m) return { r: +m[1], g: +m[2], b: +m[3] };
        return null;
    }

    function getEffectiveBg(el) {
        let current = el;
        while (current) {
            const style = getComputedStyle(current);
            const bg = parseColor(style.backgroundColor);
            if (bg && !(bg.r === 0 && bg.g === 0 && bg.b === 0 &&
                style.backgroundColor.includes('0)'))) {
                // Not fully transparent
                const alpha = style.backgroundColor.match(/[\\d.]+/g);
                if (alpha && alpha.length === 4 && parseFloat(alpha[3]) < 0.1) {
                    current = current.parentElement;
                    continue;
                }
                return bg;
            }
            current = current.parentElement;
        }
        // Default to white for bright theme
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

        // Only check elements with direct text content
        const directText = Array.from(el.childNodes)
            .filter(n => n.nodeType === 3)
            .map(n => n.textContent.trim())
            .join('');
        if (!directText) continue;

        const fg = parseColor(style.color);
        if (!fg) continue;

        const bg = getEffectiveBg(el);
        const fgLum = luminance(fg.r, fg.g, fg.b);
        const bgLum = luminance(bg.r, bg.g, bg.b);
        const ratio = contrastRatio(fgLum, bgLum);

        if (ratio < 3.0) {
            const key = el.tagName + '|' + style.color + '|' + directText.substring(0, 30);
            if (seen.has(key)) continue;
            seen.add(key);

            results.push({
                tag: el.tagName.toLowerCase(),
                classes: el.className || '',
                id: el.id || '',
                text: directText.substring(0, 80),
                fgColor: style.color,
                bgColor: `rgb(${bg.r},${bg.g},${bg.b})`,
                ratio: Math.round(ratio * 100) / 100,
            });
        }
    }
    return results;
}
"""


def _check_contrast(page, url, theme):
    """Switch to theme, load page, and check for low contrast text."""
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
    except Exception:
        # Retry once on connection issues
        page.wait_for_timeout(500)
        page.goto(url, wait_until="domcontentloaded", timeout=15000)
    # Switch theme
    page.evaluate(f'document.documentElement.setAttribute("data-theme", "{theme}")')
    # Wait for CSS to apply
    page.wait_for_timeout(300)

    issues = page.evaluate(LOW_CONTRAST_JS)
    path = urlparse(url).path

    for item in issues:
        add_issue(
            path,
            f"Low contrast ({theme}): {item['tag']}.{item['classes'].split()[0] if item['classes'] else ''}",
            f"[{theme} theme] Text barely visible (contrast ratio: {item['ratio']}:1, "
            f"minimum 3.0:1). Tag: <{item['tag']}> class=\"{item['classes']}\" "
            f"id=\"{item['id']}\". Text: \"{item['text']}\". "
            f"Foreground: {item['fgColor']}, Background: {item['bgColor']}",
            f"low-contrast-{theme}",
        )


# ═══════════════════════════════════════════════════════════════════
# TESTS — BRIGHT (LIGHT) THEME
# ═══════════════════════════════════════════════════════════════════

STATIC_PAGES = [
    ("/", "Homepage"),
    ("/curriculum", "Curriculum"),
    ("/account", "Account"),
    ("/progress", "Progress"),
    ("/search?q=algebra", "Search"),
    ("/admin", "Admin"),
]


@pytest.mark.parametrize("path_str,label", STATIC_PAGES)
def test_bright_static_contrast(contrast_page, path_str, label):
    _check_contrast(contrast_page, f"{BASE_URL}{path_str}", "bright")


@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_bright_topic_contrast(contrast_page, tid):
    _check_contrast(contrast_page, f"{BASE_URL}/topic/{tid}", "bright")


@pytest.mark.parametrize("tid", ALL_TOPICS)
def test_bright_quiz_contrast(contrast_page, tid):
    _check_contrast(contrast_page, f"{BASE_URL}/topic/{tid}/quiz", "bright")


# ═══════════════════════════════════════════════════════════════════
# TESTS — DARK THEME (also check, in case of dark-on-dark issues)
# ═══════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("path_str,label", STATIC_PAGES)
def test_dark_static_contrast(contrast_page, path_str, label):
    _check_contrast(contrast_page, f"{BASE_URL}{path_str}", "dark")


SAMPLE_TOPICS = [
    "k_numbers", "p12_add_sub", "p34_fractions", "p56_percentage",
    "sec12_algebra", "olevel_quadratic", "alevel_complex",
    "la_matrix_ops", "ps_probability", "py_basics", "dl_neural_nets",
]


@pytest.mark.parametrize("tid", SAMPLE_TOPICS)
def test_dark_topic_contrast(contrast_page, tid):
    _check_contrast(contrast_page, f"{BASE_URL}/topic/{tid}", "dark")
