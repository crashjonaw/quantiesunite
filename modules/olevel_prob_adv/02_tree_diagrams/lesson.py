TITLE = "Tree Diagrams: Sequential Events"

SECTIONS = [
    {
        "title": "Why Tree Diagrams? Organizing Complex Experiments",
        "body": """
        <h3>From Listing Outcomes to Drawing Trees</h3>
        <p>When experiments have multiple stages, listing all outcomes in a sample space becomes messy. <strong>Tree diagrams</strong> provide a visual, organized way to track all possible paths and their probabilities.</p>

        <h4>The Core Principle</h4>
        <p>A tree diagram represents an experiment that unfolds in <em>stages</em>. Each branch shows what can happen at each stage, labeled with its probability. Following a complete path from root to leaf shows one possible outcome sequence.</p>

        <h4>Why This Matters</h4>
        <ul>
            <li>Ensures you don't forget any outcomes</li>
            <li>Makes the structure of the problem visible</li>
            <li>Clearly shows which events are dependent (later probabilities depend on earlier outcomes)</li>
            <li>Makes calculating complex probabilities straightforward</li>
        </ul>

        <h4>Basic Structure</h4>
        <svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; margin: 20px 0; border-radius: 8px">
            <!-- Define arrow markers -->
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <!-- Root -->
            <circle cx="100" cy="200" r="15" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>

            <!-- First stage branches -->
            <line x1="115" y1="185" x2="220" y2="100" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="115" y1="215" x2="220" y2="300" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>

            <!-- First stage outcomes -->
            <circle cx="250" cy="100" r="15" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>
            <circle cx="250" cy="300" r="15" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>

            <!-- Labels for first stage -->
            <text x="160" y="135" fill='currentColor' font-size='14' font-family='monospace'>p₁</text>
            <text x="160" y="275" fill='currentColor' font-size='14' font-family='monospace'>p₂</text>
            <text x="270" y="85" fill='currentColor' font-size='14' font-family='monospace'>Event A</text>
            <text x="270" y="315" fill='currentColor' font-size='14' font-family='monospace'>Event B</text>

            <!-- Second stage branches from A -->
            <line x1="265" y1="115" x2="370" y2="50" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="265" y1="115" x2="370" y2="150" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>

            <!-- Second stage branches from B -->
            <line x1="265" y1="285" x2="370" y2="250" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>
            <line x1="265" y1="285" x2="370" y2="350" stroke='#30363d' stroke-width="2" marker-end="url(#arrowhead)"/>

            <!-- Final outcomes -->
            <circle cx="400" cy="50" r="12" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>
            <circle cx="400" cy="150" r="12" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>
            <circle cx="400" cy="250" r="12" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>
            <circle cx="400" cy="350" r="12" fill='#4f8ef7' stroke='#30363d' stroke-width="2"/>

            <!-- Second stage labels -->
            <text x="310" y="75" fill='currentColor' font-size='12' font-family='monospace'>q₁</text>
            <text x="310" y="130" fill='currentColor' font-size='12' font-family='monospace'>q₂</text>
            <text x="310" y="230" fill='currentColor' font-size='12' font-family='monospace'>q₃</text>
            <text x="310" y="330" fill='currentColor' font-size='12' font-family='monospace'>q₄</text>

            <!-- Outcome labels -->
            <text x="420" y="55" fill='currentColor' font-size='12' font-family='monospace'>A∩C</text>
            <text x="420" y="155" fill='currentColor' font-size='12' font-family='monospace'>A∩D</text>
            <text x="420" y="255" fill='currentColor' font-size='12' font-family='monospace'>B∩C</text>
            <text x="420" y="355" fill='currentColor' font-size='12' font-family='monospace'>B∩D</text>
        </svg>

        <p><strong>Reading the diagram:</strong> Start at the root (left). Each path to a leaf represents one complete sequence of outcomes. Labels on branches are probabilities. The product of probabilities along a path equals the probability of that complete outcome.</p>

        <div class="concept-box">
            <h4>Example 1: Rolling Two Dice Sequentially</h4>
            <p><strong>First die:</strong> \\(P(\\text{any outcome}) = \\frac{1}{6}\\)</p>
            <p><strong>Second die:</strong> \\(P(\\text{any outcome}) = \\frac{1}{6}\\)</p>
            <p><strong>Sample space:</strong> \\(6 \\times 6 = 36\\) outcomes</p>
            <p><strong>\\(P(\\text{first die} = 3 \\text{ AND second die} = 5) = \\frac{1}{6} \\times \\frac{1}{6} = \\frac{1}{36}\\)</strong></p>
            <p>The tree has 6 branches from the root (first die), then 6 branches from each endpoint (second die), creating 36 total paths.</p>
        </div>
        """
    },
    {
        "title": "With and Without Replacement",
        "body": """
        <h3>How Outcomes Change (or Don't) After Drawing</h3>
        <p>A critical distinction: when we draw something from a collection, does it go back or not? This fundamentally changes the probabilities for subsequent draws.</p>

        <h4>Without Replacement: Probabilities Change</h4>
        <p><strong>Without replacement</strong> means once an item is drawn, it's gone. The sample space shrinks, and probabilities for subsequent draws change.</p>

        <div class="concept-box">
            <h4>Example 2: Drawing Two Balls Without Replacement</h4>
            <p><strong>Bag contents:</strong> 3 red, 2 blue (5 total)</p>
            <p><strong>First draw:</strong></p>
            <ul>
                <li>\\(P(\\text{Red}) = \\frac{3}{5}\\)</li>
                <li>\\(P(\\text{Blue}) = \\frac{2}{5}\\)</li>
            </ul>
            <p><strong>Second draw (depends on first):</strong></p>
            <ul>
                <li>If first was red: 2 red and 2 blue remain. \\(P(\\text{Red}) = \\frac{2}{4} = \\frac{1}{2}\\), \\(P(\\text{Blue}) = \\frac{2}{4} = \\frac{1}{2}\\)</li>
                <li>If first was blue: 3 red and 1 blue remain. \\(P(\\text{Red}) = \\frac{3}{4}\\), \\(P(\\text{Blue}) = \\frac{1}{4}\\)</li>
            </ul>
            <p><strong>\\(P(\\text{both red}) = \\frac{3}{5} \\times \\frac{2}{4} = \\frac{6}{20} = \\frac{3}{10}\\)</strong></p>
            <p><strong>\\(P(\\text{red then blue}) = \\frac{3}{5} \\times \\frac{2}{4} = \\frac{6}{20} = \\frac{3}{10}\\)</strong></p>
            <p><strong>\\(P(\\text{blue then red}) = \\frac{2}{5} \\times \\frac{3}{4} = \\frac{6}{20} = \\frac{3}{10}\\)</strong></p>
            <p><strong>\\(P(\\text{both blue}) = \\frac{2}{5} \\times \\frac{1}{4} = \\frac{2}{20} = \\frac{1}{10}\\)</strong></p>
        </div>

        <p><strong>Key insight:</strong> The probability of the second event depends on what happened first. These are <em>dependent</em> events.</p>

        <h4>With Replacement: Probabilities Stay the Same</h4>
        <p><strong>With replacement</strong> means after drawing, the item goes back. Probabilities for subsequent draws remain identical to the first draw.</p>

        <div class="concept-box">
            <h4>Example 3: Drawing Two Balls With Replacement</h4>
            <p><strong>Bag contents:</strong> 3 red, 2 blue (5 total)</p>
            <p><strong>First draw:</strong></p>
            <ul>
                <li>\\(P(\\text{Red}) = \\frac{3}{5}\\)</li>
                <li>\\(P(\\text{Blue}) = \\frac{2}{5}\\)</li>
            </ul>
            <p><strong>Second draw:</strong> Ball returned. Same bag, same probabilities!</p>
            <ul>
                <li>\\(P(\\text{Red}) = \\frac{3}{5}\\)</li>
                <li>\\(P(\\text{Blue}) = \\frac{2}{5}\\)</li>
            </ul>
            <p><strong>\\(P(\\text{both red}) = \\frac{3}{5} \\times \\frac{3}{5} = \\frac{9}{25}\\)</strong></p>
            <p><strong>\\(P(\\text{red then blue}) = \\frac{3}{5} \\times \\frac{2}{5} = \\frac{6}{25}\\)</strong></p>
            <p><strong>\\(P(\\text{blue then red}) = \\frac{2}{5} \\times \\frac{3}{5} = \\frac{6}{25}\\)</strong></p>
            <p><strong>\\(P(\\text{both blue}) = \\frac{2}{5} \\times \\frac{2}{5} = \\frac{4}{25}\\)</strong></p>
        </div>

        <p><strong>Key insight:</strong> Probabilities don't change between draws. These are <em>independent</em> events (despite being sequential).</p>

        <h4>Spot the Difference</h4>
        <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <tr class="formula-box">
                <td style="padding: 12px;"><strong>Aspect</strong></td>
                <td style="padding: 12px;"><strong>Without Replacement</strong></td>
                <td style="padding: 12px;"><strong>With Replacement</strong></td>
            </tr>
            <tr >
                <td style="padding: 12px;">Sample space shrinks</td>
                <td style="padding: 12px;">Yes</td>
                <td style="padding: 12px;">No</td>
            </tr>
            <tr >
                <td style="padding: 12px;">Later probabilities change</td>
                <td style="padding: 12px;">Yes</td>
                <td style="padding: 12px;">No</td>
            </tr>
            <tr >
                <td style="padding: 12px;">Events are independent</td>
                <td style="padding: 12px;">No (dependent)</td>
                <td style="padding: 12px;">Yes (independent)</td>
            </tr>
            <tr >
                <td style="padding: 12px;">Real-world example</td>
                <td style="padding: 12px;">Drawing cards from a deck</td>
                <td style="padding: 12px;">Rolling dice multiple times</td>
            </tr>
        </table>

        <div class="warning-box">
            <h4>Common Mistake</h4>
            <p>Students often forget to change the denominator without replacement. If you draw from 5 items and don't return, the next draw has 4 items available, not 5!</p>
        </div>
        """
    },
    {
        "title": "The Multiplication Rule: Following Paths",
        "body": """
        <h3>Calculating Probabilities from Tree Diagrams</h3>
        <p>Tree diagrams reveal the most important probability rule: <strong>to find the probability of a complete sequence, multiply the probabilities along the path.</strong></p>

        <h4>The Multiplication Rule (for sequences)</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>\\(P(A \\text{ and } B) = P(A) \\times P(B|A)\\)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Read: "Probability of A AND B equals probability of A times probability of B given A"</p>
        </div>

        <p><strong>Why multiply?</strong> Because each step represents a <em>fraction</em> of the previous outcomes. Following a complete path means narrowing down step by step.</p>

        <div class="worked-example">
            <h4>Example 4: Coin Flip Then Die Roll</h4>
            <p><strong>Step 1:</strong> Flip a coin. \\(P(\\text{Heads}) = \\frac{1}{2}\\)</p>
            <p><strong>Step 2:</strong> Roll a die. \\(P(\\text{Rolling a 4}) = \\frac{1}{6}\\)</p>
            <p><strong>\\(P(\\text{Heads AND 4}) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12}\\)</strong></p>
            <p><strong>Why:</strong> Out of all coin flips, 1/2 are heads. Out of those heads, 1/6 will be followed by a 4. So 1/2 × 1/6 = 1/12 of all trials have both.</p>
        </div>

        <div class="worked-example">
            <h4>Example 5: Drawing Cards Without Replacement</h4>
            <p><strong>Draw 1:</strong> \\(P(\\text{Heart}) = \\frac{13}{52} = \\frac{1}{4}\\)</p>
            <p><strong>Draw 2:</strong> \\(P(\\text{Heart} | \\text{first was Heart}) = \\frac{12}{51}\\)</p>
            <p><strong>\\(P(\\text{both Hearts}) = \\frac{13}{52} \\times \\frac{12}{51} = \\frac{156}{2652} = \\frac{1}{17} \\approx 0.0588\\)</strong></p>
            <p><strong>Why?:</strong> First we narrow from 52 cards to those that are hearts (13/52). Then, from 51 remaining cards, we need a heart (12/51). Multiplying gives the probability both conditions hold.</p>
        </div>

        <h4>Summing Multiple Paths</h4>
        <p>If we want the probability of a general event (not a specific path), we sum the probabilities of all paths that lead to that event.</p>

        <div class="concept-box">
            <h4>Example 6: Getting At Least One Heads in Two Flips</h4>
            <p><strong>Paths that work:</strong></p>
            <ul>
                <li>Path 1: Heads then Heads: \\(\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}\\)</li>
                <li>Path 2: Heads then Tails: \\(\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}\\)</li>
                <li>Path 3: Tails then Heads: \\(\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}\\)</li>
            </ul>
            <p><strong>\\(P(\\text{at least one Heads}) = \\frac{1}{4} + \\frac{1}{4} + \\frac{1}{4} = \\frac{3}{4}\\)</strong></p>
            <p><strong>Note:</strong> The path "Tails then Tails" doesn't work, so we don't include it. \\(P(\\text{Tails, Tails}) = \\frac{1}{4}\\), and indeed \\(\\frac{3}{4} + \\frac{1}{4} = 1\\). ✓</p>
        </div>

        <p><strong>Workflow:</strong> Identify all paths that satisfy your condition. Calculate probability of each path (multiply). Sum all satisfying probabilities.</p>
        """
    }
]
