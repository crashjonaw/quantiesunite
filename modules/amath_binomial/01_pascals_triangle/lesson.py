TITLE = "Pascal's Triangle and Binomial Coefficients"

SECTIONS = [
    {
        "title": "Why Pascal's Triangle Matters",
        "body": """
        <div class="concept-box">
            <h3>The Core Idea</h3>
            <p >
                <strong>Why do we study combinations?</strong> Because many real situations ask:
                "In how many ways can we choose?" For example:
            </p>
            <ul >
                <li>How many ways can we select 3 people from a group of 8?</li>
                <li>What coefficients appear in algebraic expansions?</li>
                <li>What are the probabilities in coin flips or card games?</li>
            </ul>
            <p >
                The answer comes from a simple pattern: <strong>Pascal's Triangle</strong>.
            </p>
        </div>

        <h4 class="accent-heading" style="margin-top: 20px;">Discovering the Pattern</h4>
        <p >
            Pascal's Triangle is a triangular arrangement where each entry is the <strong>sum of the two numbers above it</strong>.
        </p>

        <svg viewBox="145 -3 310 242" xmlns="http://www.w3.org/2000/svg" style="margin: 20px auto; display: block; width: 100%; max-width: 500px;">
            <!-- Background -->
            <rect x="147" y="-1" width="306" height="238" fill='none' stroke='currentColor' stroke-width="2" rx='4' opacity='0.3'/>

            <!-- Row 0 -->
            <circle cx="300" cy="30" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="300" y="36" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>

            <!-- Row 1 -->
            <circle cx="270" cy="70" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="270" y="76" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>
            <circle cx="330" cy="70" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="330" y="76" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>

            <!-- Row 2 -->
            <circle cx="240" cy="110" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="240" y="116" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>
            <circle cx="300" cy="110" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="300" y="116" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>2</text>
            <circle cx="360" cy="110" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="360" y="116" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>

            <!-- Row 3 -->
            <circle cx="210" cy="150" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="210" y="156" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>
            <circle cx="270" cy="150" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="270" y="156" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>3</text>
            <circle cx="330" cy="150" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="330" y="156" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>3</text>
            <circle cx="390" cy="150" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="390" y="156" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>

            <!-- Row 4 -->
            <circle cx="180" cy="190" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="180" y="196" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>
            <circle cx="240" cy="190" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="240" y="196" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>4</text>
            <circle cx="300" cy="190" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="300" y="196" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>6</text>
            <circle cx="360" cy="190" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="360" y="196" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>4</text>
            <circle cx="420" cy="190" r="18" fill='none' stroke='#4f8ef7' stroke-width="2"/>
            <text x="420" y="196" text-anchor='middle' font-size='14' font-family='sans-serif' fill='currentColor' font-weight='bold'>1</text>

            <!-- Arrows showing addition -->
            <line x1="285" y1="90" x2="295" y2="100" stroke='currentColor' opacity='0.5' stroke-width="1.5" stroke-dasharray="3,3"/>
            <line x1="315" y1="90" x2="305" y2="100" stroke='currentColor' opacity='0.5' stroke-width="1.5" stroke-dasharray="3,3"/>

            <!-- Label -->
            <text x="300" y="222" text-anchor='middle' font-size='12' font-family='sans-serif' fill='currentColor' opacity='0.6' font-style='italic'>Each entry = sum of two above</text>
        </svg>

        <div class="worked-example" style="margin: 20px 0; padding: 15px; border-radius: 4px">
            <p style="margin: 0;">
                <strong class="accent-heading">Example:</strong> The center 6 in row 4 comes from 3 + 3 above it.
            </p>
        </div>
        """
    },
    {
        "title": "Binomial Coefficients: Counting Combinations",
        "body": """
        <h4 class="accent-heading">What Does C(n, k) Mean?</h4>
        <p >
            <strong>C(n, k)</strong> (read as "<strong>n choose k</strong>") counts the number of ways to select
            k objects from n objects <em>where order doesn't matter</em>.
        </p>

        <p style="text-align: center; margin: 20px 0; padding: 15px; border-radius: 4px">
            <strong style="font-size: 1.1em">C(n, k) = \\(\\frac{n!}{k!(n-k)!}\\)</strong>
        </p>

        <div class="concept-box">
            <h4 class="accent-heading">Why This Formula?</h4>
            <p >
                <strong>First principles:</strong> There are n! ways to arrange all n objects. But when choosing k objects,
                we don't care about the order of those k items or the order of the (n−k) unchosen items.
                So we divide by k! and (n−k)! to remove those orderings.
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;">
                <strong class="accent-heading">Example:</strong> Calculate C(5, 2) — ways to choose 2 people from 5.
            </p>
            <p style="margin: 5px 0;">
                C(5, 2) = \\(\\frac{5!}{2! \\cdot 3!}\\) = \\(\\frac{5 \\times 4}{2 \\times 1}\\) = 10
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                ✓ There are exactly 10 ways to pick 2 people from a group of 5.
            </p>
        </div>
        """
    },
    {
        "title": "Key Properties of Binomial Coefficients",
        "body": """
        <h4 class="accent-heading">Essential Patterns</h4>

        <div class="concept-box">
            <p style="margin: 5px 0;"><strong class="accent-heading">Property 1:</strong>
                C(n, 0) = 1 — One way to choose nothing (the empty set).
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 5px 0;"><strong class="accent-heading">Property 2:</strong>
                C(n, n) = 1 — One way to choose everything.
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 5px 0;"><strong class="accent-heading">Property 3 (Symmetry):</strong>
                C(n, k) = C(n, n−k) — Choosing k items is the same as choosing which n−k to <em>leave out</em>.
            </p>
        </div>

        <div class="concept-box">
            <p style="margin: 5px 0;"><strong class="accent-heading">Property 4 (Pascal's Identity):</strong>
                C(n, k) + C(n, k+1) = C(n+1, k+1)
            </p>
            <p style="margin: 5px 0; font-size: 0.95em">
                This is why adjacent entries in Pascal's Triangle sum to the entry below!
            </p>
        </div>

        <div class="worked-example">
            <p style="margin: 0;">
                <strong class="accent-heading">Example:</strong> Verify C(6, 2) = C(6, 4) using symmetry.
            </p>
            <p style="margin: 5px 0;">
                C(6, 2) = \\(\\frac{6!}{2! \\cdot 4!}\\) = 15
            </p>
            <p style="margin: 5px 0;">
                C(6, 4) = \\(\\frac{6!}{4! \\cdot 2!}\\) = 15 ✓
            </p>
        </div>
        """
    },
    {
        "title": "Connection to Binomial Expansion",
        "body": """
        <h4 class="accent-heading">How Pascal's Triangle Predicts Coefficients</h4>

        <p >
            The entries in <strong>row n</strong> of Pascal's Triangle are exactly the binomial coefficients
            \\(C(n,0), C(n,1), C(n,2), \ldots, C(n,n)\\) for the expansion of \\((a + b)^n\\).
        </p>

        <div class="concept-box">
            <p style="margin: 5px 0;">
                <strong>Row 3:</strong> 1, 3, 3, 1  →  These are the coefficients in \\((a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3\\)
            </p>
            <p style="margin: 5px 0;">
                <strong>Row 4:</strong> 1, 4, 6, 4, 1  →  These are the coefficients in \\((a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4\\)
            </p>
        </div>

        <div class="success-box" style="margin: 15px 0; padding: 12px;  border-left: 4px solid #3fb950; border-radius: 4px;">
            <p style="margin: 0;">
                ✓ <strong>Key Insight:</strong> Pascal's Triangle gives us coefficients instantly without computing
                factorials!
            </p>
        </div>
        """
    }
]
