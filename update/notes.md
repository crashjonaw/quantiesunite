# Update Notes

## 2026-03-25: SVG double-quote attribute fix (systematic)

**Problem:** SVG `fill`, `stroke`, `text-anchor`, `font-family`, `font-weight`, and `font-size` attributes used double quotes (`fill="#e6edf3"`) inside double-quoted Python strings in lesson.py files. This prematurely terminated the string, truncating the SVG — leaving it without a closing `</svg>` tag. The unclosed SVG swallowed all subsequent page content, making pages 2/3/4 appear blank.

**Scope:** 155 lesson.py files across all concept-based modules (3976 occurrences).

**Fix:** Replaced all double-quoted SVG attributes with single quotes (`fill='#e6edf3'`) across all `modules/*/0*/lesson.py` files.

**Status:** Fix applied. Server needs redeployment via `./run.sh`.

**Note:** This was not caught by the automated feedback loop — diagnosed and fixed manually in the main session.

## 2026-03-25: SVG single-quote conflict in single-quoted Python strings

**Problem:** The earlier SVG fix (above) replaced double-quoted SVG attributes with single-quoted ones. However, in `modules/p56_average/01_what_is_average/lesson.py`, the `body` value on line 14 was wrapped in single quotes (`'<h3>...'`), not triple-double-quotes. The single-quoted SVG attributes (`font-size='14'`) conflicted with the enclosing single-quoted Python string, causing a `SyntaxError` and preventing the entire `p56_average` module from loading.

**Scope:** 1 file affected: `modules/p56_average/01_what_is_average/lesson.py`.

**Fix:** Changed the body string from single quotes to triple-double-quotes (`"""..."""`).

**Status:** Fixed. Server redeployed.

## 2026-03-28: Inline math ($...$) not rendering in KaTeX (systematic)

**Problem:** KaTeX auto-render was configured with `$$...$$` (display) and `\(...\)` (inline) delimiters, but many lesson files use `$...$` for inline math. This caused inline formulas to appear as raw LaTeX text instead of rendered math.

**Scope:** All pages site-wide. Reported on `alevel_regression/01_correlation_scatter` but affects any lesson using `$...$` inline math.

**Fix:** Added `{left: '$', right: '$', display: false}` to KaTeX delimiter config in 3 locations: `base.html` onload, `_interactive_scripts.html` goToPage(), and `_interactive_scripts.html` DOMContentLoaded.

**Status:** Fixed. Server needs redeployment via `./run.sh`.

## 2026-03-30: KaTeX display math overflow clipping denominators (systematic)

**Problem:** `.katex-display` CSS rule had `overflow-y: hidden`, which clipped the bottom of tall rendered fractions. Denominators of complex formulas (e.g., Pearson correlation coefficient with `\sqrt{}` in denominator) were cut off and invisible.

**Scope:** All pages site-wide — any display math (`$$...$$`) with tall fractions was affected.

**Fix:** Changed `overflow-y: hidden` to `overflow-y: visible` in `.katex-display` rule in `static/css/style.css` (line 1168).

**Status:** Fixed. Server needs redeployment via `./run.sh`.

## 2026-03-30: KaTeX SVG elements styled as diagrams (systematic)

**Problem:** Theme-aware SVG CSS rules (`.section-body svg, .rich-content svg`) applied `background: var(--bg3) !important`, `border`, and `border-radius` to ALL SVGs — including KaTeX's internal inline SVGs used for `\sqrt{}` radical symbols and `\frac` lines. This gave math SVGs an opaque background and border, hiding denominator content beneath square roots.

**Scope:** All pages site-wide — any formula using `\sqrt{}`, `\frac`, or other KaTeX SVG-rendered elements was affected.

**Fix:** Added `.katex svg { background: none !important; border: none !important; border-radius: 0 !important; }` override in `static/css/style.css` (after the general SVG diagram rules) to exclude KaTeX's internal SVGs from diagram styling.

**Status:** Fixed. Server needs redeployment via `./run.sh`.

## 2026-04-03: Chart.js text colors invisible in bright/light mode (systematic)

**Problem:** Chart.js axis tick labels, axis titles, and chart titles did not adapt to the active theme. The `initChartsOnPage` function set tick and legend colors based on the theme at load time, but did not set axis title (`scales[axis].title.color`) or chart title (`plugins.title.color`) colors. Additionally, toggling the theme after charts were initialized did not update chart colors — charts retained their original dark-mode white text, making axis values invisible on a bright background.

**Scope:** All pages site-wide that use Chart.js `<canvas data-chart>` elements (primarily `p34_data` module but applies to any module with charts).

**Fix:** 
1. Added `getChartThemeColors()` helper and `applyChartThemeColors(chart)` function in `_interactive_scripts.html`.
2. `initChartsOnPage` now also sets `scales[axis].title.color` and `plugins.title.color`.
3. Added `updateAllChartsTheme()` function that iterates all initialized Chart.js canvases and updates colors via `Chart.getChart()`.
4. Hooked `updateAllChartsTheme()` into `toggleTheme()` in `base.html` so charts update live on theme switch.

**Status:** Fixed. Server needs redeployment via `./run.sh`.
