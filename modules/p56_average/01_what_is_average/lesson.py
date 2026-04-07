TITLE = "What is Average?"

SECTIONS = [
    {
        "title": "Why We Need Averages",
        "body": '<h3>The Problem: Too Many Numbers</h3><p>Imagine your test scores for the term are: <strong>70, 85, 90, 75, 80</strong>.</p><p>Someone asks: <em>"How did you do overall?"</em></p><p>You could say all five scores, but that is a lot of information. What you really need is <strong>ONE number</strong> that represents all five scores. That is what an <strong>average</strong> does.</p><div class="concept-box"><strong>An average is a single number that summarizes a group of numbers.</strong></div><h3>Real-World Examples</h3><ul><li><strong>Weather:</strong> It was 18°C, 20°C, 19°C, 21°C, and 22°C on five days. The average temperature was about 20°C.</li><li><strong>Sports:</strong> A footballer scored 1, 2, 1, 3, 2 goals in five matches. His average was 1.8 goals per match.</li><li><strong>Shopping:</strong> Apples cost £0.50, £0.45, £0.55 each. Average price is about £0.50.</li></ul>'
    },
    {
        "title": "What Does Average Mean?",
        "body": '<h3>The Sharing Idea</h3><p>Think of average as <strong>"sharing equally"</strong>.</p><div class="worked-example"><p><strong>Example:</strong> Three friends have 5, 7, and 9 sweets.</p><p>If they pool their sweets and share equally:</p><ul><li>Total sweets = \(5 + 7 + 9 = 21\)</li><li>Number of friends = 3</li><li>Each friend gets = \(21 \div 3 =\) <strong>7 sweets</strong></li><li><strong>Average = 7</strong></li></ul></div><div class="success-box">After sharing equally, each person would have the same amount (7). This equal amount is the <strong>average</strong>.</div>'
    },
    {
        "title": "Visual Understanding",
        "body": """<h3>The Leveling-Out Idea</h3><p>Imagine water in containers at different heights:</p><svg width="460" height="230" viewBox="0 0 460 230" xmlns="http://www.w3.org/2000/svg">
<!-- Background -->
<rect x="0" y="0" width="460" height="230" fill="#1e1e2e" rx="4"/>

<!-- BEFORE section -->
<text x="80" y="30" font-family="sans-serif" font-size="14" font-weight="bold" fill="currentColor" text-anchor="middle">BEFORE</text>

<!-- Baseline for bars at y=190, top padding at y=40 -->
<!-- Bar heights: 5 units=50px, 7 units=70px, 9 units=90px -->
<!-- 3 bars, each 36px wide, 16px gap between them -->
<!-- Group starts at x=28, bars at 28, 80, 132 -->
<rect x="28" y="140" width="36" height="50" fill="#3498db" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="46" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">5</text>

<rect x="80" y="120" width="36" height="70" fill="#3498db" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="98" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">7</text>

<rect x="132" y="100" width="36" height="90" fill="#3498db" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="150" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">9</text>

<!-- Divider line -->
<line x1="210" y1="20" x2="210" y2="215" stroke="#8b949e" stroke-width="1" stroke-dasharray="4,4"/>

<!-- Arrow -->
<text x="230" y="120" font-family="sans-serif" font-size="20" fill="currentColor">&#x2192;</text>

<!-- AFTER section -->
<text x="345" y="30" font-family="sans-serif" font-size="14" font-weight="bold" fill="currentColor" text-anchor="middle">AFTER (Average = 7)</text>

<!-- 3 equal bars, each 36px wide, 16px gap, all height=70px -->
<!-- Group starts at x=259, bars at 259, 311, 363 -->
<rect x="259" y="120" width="36" height="70" fill="#2ecc71" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="277" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">7</text>

<rect x="311" y="120" width="36" height="70" fill="#2ecc71" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="329" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">7</text>

<rect x="363" y="120" width="36" height="70" fill="#2ecc71" stroke="#8b949e" stroke-width="2" rx="4"/>
<text x="381" y="206" font-family="sans-serif" font-size="13" fill="currentColor" text-anchor="middle">7</text>

<!-- Average line across AFTER bars -->
<line x1="253" y1="120" x2="405" y2="120" stroke="#f1c40f" stroke-width="2" stroke-dasharray="6,3"/>
</svg><p style="margin-top: 10px;">The bars of different heights "level out" to the same height when we find the average.</p>"""
    },
    {
        "title": "The Average Formula",
        "body": '<h3>How to Calculate Average</h3><p>The formula is simple:</p><div class="concept-box" style="text-align: center; font-size: 18px; padding: 15px;"><strong>Average = Sum of all values \(\div\) Number of values</strong></div><p>In short: <strong>Average = Total \(\div\) Count</strong></p><h3>Example with Test Scores</h3><p>Back to our first example: test scores 70, 85, 90, 75, 80</p><div class="worked-example"><ul><li><strong>Step 1:</strong> Add all scores = \(70 + 85 + 90 + 75 + 80 = 425\)</li><li><strong>Step 2:</strong> Count how many scores = 5</li><li><strong>Step 3:</strong> Divide = \(425 \div 5 =\) <strong>85</strong></li></ul><p>The average (or mean) test score is <strong>85</strong>.</p></div>'
    },
    {
        "title": "Types of Averages",
        "body": '<h3>There Are Three Types of Averages</h3><p>In this module, we will learn about three different types of averages:</p><div class="concept-box"><ol><li><strong>Mean</strong> - the most common type (what we just learned)</li><li><strong>Median</strong> - the middle value when numbers are sorted</li><li><strong>Mode</strong> - the number that appears most often</li></ol></div><p>Each type of average is useful in different situations:</p><ul><li><strong>Mean:</strong> Use when you want a typical value (like average test scores)</li><li><strong>Median:</strong> Use when there are very large or very small numbers that might skew the result</li><li><strong>Mode:</strong> Use when you want the most popular or common value</li></ul>'
    }
]
