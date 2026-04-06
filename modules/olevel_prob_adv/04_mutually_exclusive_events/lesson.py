TITLE = "Mutually Exclusive & Non-Mutually Exclusive Events"

SECTIONS = [
    {
        "title": "Mutually Exclusive Events: The Simple Case",
        "body": """
        <h3>When Two Things Cannot Happen at Once</h3>
        <p>Some events cannot occur simultaneously. When you roll a die, you cannot get both a 3 and a 5 on the same roll. These are <strong>mutually exclusive</strong> (or <strong>disjoint</strong>) events.</p>

        <h4>Definition</h4>
        <p>Events A and B are <strong>mutually exclusive</strong> if they cannot both occur at the same time.</p>

        <p><strong>Mathematically:</strong> \\(P(A \\cap B) = 0\\) (the intersection is empty)</p>

        <h4>The Addition Rule (Mutually Exclusive)</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="font-size: 1.1em; margin: 0"><strong>\\(P(A \\text{ or } B) = P(A) + P(B)\\)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Only works when A and B are mutually exclusive!</p>
        </div>

        <p><strong>Why add?</strong> Since A and B don't overlap, we can simply add the number of favorable outcomes for A and for B, then divide by the total.</p>

        <div class="worked-example">
            <h4>Example 1: Rolling a Die</h4>
            <p><strong>Question:</strong> What's P(rolling a 3 or a 5)?</p>
            <p><strong>Sample space:</strong> {1, 2, 3, 4, 5, 6}</p>
            <p><strong>Outcomes for "3 or 5":</strong> {3, 5} — two outcomes</p>
            <p><strong>\\(P(3 \\text{ or } 5) = \\frac{2}{6} = \\frac{1}{3}\\)</strong></p>
            <p><strong>Using the formula:</strong> \\(P(3) + P(5) = \\frac{1}{6} + \\frac{1}{6} = \\frac{2}{6} = \\frac{1}{3}\\) ✓</p>
            <p><strong>Why these are mutually exclusive:</strong> A single die roll cannot show both 3 and 5.</p>
        </div>

        <div class="concept-box">
            <h4>Example 2: Drawing a Marble</h4>
            <p><strong>Bag:</strong> 5 red, 3 blue, 2 green (10 total)</p>
            <p><strong>Question:</strong> P(drawing red or green)?</p>
            <p><strong>Favorable outcomes:</strong> 5 red + 2 green = 7</p>
            <p><strong>\\(P(\\text{red or green}) = \\frac{7}{10}\\)</strong></p>
            <p><strong>Using the formula:</strong> \\(P(\\text{red}) + P(\\text{green}) = \\frac{5}{10} + \\frac{2}{10} = \\frac{7}{10}\\) ✓</p>
        </div>

        <h4>Identifying Mutually Exclusive Events</h4>
        <p>Ask yourself: "Can both happen in a single trial?" If the answer is "no," they're mutually exclusive.</p>

        <ul>
            <li><strong>Die showing 3 AND die showing 5:</strong> No → Mutually exclusive</li>
            <li><strong>Card is red AND card is black:</strong> No → Mutually exclusive</li>
            <li><strong>Coin is heads AND coin is tails:</strong> No → Mutually exclusive</li>
            <li><strong>Card is red AND card is a heart:</strong> Yes (red hearts exist!) → NOT mutually exclusive</li>
        </ul>

        <div class="warning-box">
            <h4>Common Mistake</h4>
            <p>Assuming "or" always means mutually exclusive. In reality, many "or" statements allow overlap. The next section shows when.</p>
        </div>
        """
    },
    {
        "title": "Non-Mutually Exclusive Events: Adding with Overlap",
        "body": """
        <h3>When Events Can Both Happen</h3>
        <p>Some events can occur together. A card can be both red and a face card. A person can be both tall and have blue eyes. These are <strong>non-mutually exclusive</strong> events, and we must handle the overlap carefully.</p>

        <h4>Why Overlap Matters</h4>
        <p>If we naively add P(A) + P(B), we count the overlap twice. We must subtract it once to correct.</p>

        <h4>The Addition Rule (Non-Mutually Exclusive)</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="font-size: 1.1em; margin: 0"><strong>\\(P(A \\text{ or } B) = P(A) + P(B) - P(A \\text{ and } B)\\)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Works for any two events, mutually exclusive or not</p>
        </div>

        <p><strong>Visualizing with a Venn diagram:</strong></p>

        <svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; margin: 20px 0; border-radius: 8px">
            <!-- Circle A -->
            <circle cx="150" cy="175" r="100" fill='#4f8ef7' opacity='0.3' stroke='#4f8ef7' stroke-width="2"/>
            <!-- Circle B -->
            <circle cx="350" cy="175" r="100" fill='#7ee787' opacity='0.3' stroke='#7ee787' stroke-width="2"/>

            <!-- Labels -->
            <text x="110" y="140" fill='currentColor' font-size='16' font-weight='bold'>A</text>
            <text x="390" y="140" fill='currentColor' font-size='16' font-weight='bold'>B</text>
            <text x="250" y="185" fill='currentColor' font-size='14' font-weight='bold'>A ∩ B</text>

            <!-- Descriptive text -->
            <text x="20" y="30" fill='currentColor' font-size='14'>Blue region: Only A</text>
            <text x="20" y="55" fill='currentColor' font-size='14'>Green region: Only B</text>
            <text x="20" y="80" fill='currentColor' font-size='14'>Purple overlap: Both A and B</text>

            <!-- Formula annotation -->
            <text x="20" y="310" fill='currentColor' font-size='13' font-family='monospace'>P(A or B) = P(A) + P(B) − P(A ∩ B)</text>
            <text x="20" y="330" fill='currentColor' opacity='0.6' font-size='12' font-family='monospace'>= (blue area) + (green area) − (purple area counted twice)</text>
        </svg>

        <div class="worked-example">
            <h4>Example 3: Drawing a Card (Red or Face Card)</h4>
            <p><strong>Standard deck: 52 cards</strong></p>
            <p><strong>Event A:</strong> Drawing a red card</p>
            <ul>
                <li>Red cards = 26 (13 hearts + 13 diamonds)</li>
                <li>\\(P(\\text{Red}) = \\frac{26}{52} = \\frac{1}{2}\\)</li>
            </ul>
            <p><strong>Event B:</strong> Drawing a face card (J, Q, K)</p>
            <ul>
                <li>Face cards = 12 (3 per suit × 4 suits)</li>
                <li>\\(P(\\text{Face}) = \\frac{12}{52} = \\frac{3}{13}\\)</li>
            </ul>
            <p><strong>Overlap:</strong> Red face cards</p>
            <ul>
                <li>Red face cards = 6 (3 per suit × 2 red suits)</li>
                <li>\\(P(\\text{Red and Face}) = \\frac{6}{52} = \\frac{3}{26}\\)</li>
            </ul>
            <p><strong>Using the formula:</strong></p>
            <p>\\(P(\\text{Red or Face}) = \\frac{26}{52} + \\frac{12}{52} - \\frac{6}{52} = \\frac{32}{52} = \\frac{8}{13}\\)</p>
            <p><strong>Why subtract?</strong> The 6 red face cards are counted in both "red cards" and "face cards." Subtracting removes the double count.</p>
        </div>

        <div class="concept-box">
            <h4>Example 4: Number Divisibility</h4>
            <p><strong>Question:</strong> A number is selected from 1 to 20. What's P(divisible by 2 or 3)?</p>
            <p><strong>Divisible by 2:</strong> {2, 4, 6, 8, 10, 12, 14, 16, 18, 20} — 10 numbers, \\(P(\\text{div by 2}) = \\frac{10}{20} = \\frac{1}{2}\\)</p>
            <p><strong>Divisible by 3:</strong> {3, 6, 9, 12, 15, 18} — 6 numbers, \\(P(\\text{div by 3}) = \\frac{6}{20} = \\frac{3}{10}\\)</p>
            <p><strong>Divisible by both 2 and 3 (i.e., by 6):</strong> {6, 12, 18} — 3 numbers, \\(P(\\text{div by 2 and 3}) = \\frac{3}{20}\\)</p>
            <p><strong>\\(P(\\text{div by 2 or 3}) = \\frac{10}{20} + \\frac{6}{20} - \\frac{3}{20} = \\frac{13}{20}\\)</strong></p>
            <p><strong>Check by listing:</strong> {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20} — exactly 13 numbers ✓</p>
        </div>

        <h4>When to Use Which Formula</h4>
        <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <tr class="formula-box">
                <td style="padding: 12px;"><strong>Situation</strong></td>
                <td style="padding: 12px;"><strong>Formula</strong></td>
            </tr>
            <tr >
                <td style="padding: 12px;">Mutually exclusive (no overlap)</td>
                <td style="padding: 12px;">P(A or B) = P(A) + P(B)</td>
            </tr>
            <tr >
                <td style="padding: 12px;">Non-mutually exclusive (has overlap)</td>
                <td style="padding: 12px;">P(A or B) = P(A) + P(B) − P(A ∩ B)</td>
            </tr>
            <tr >
                <td style="padding: 12px;">Unsure</td>
                <td style="padding: 12px;">Always safe: use P(A) + P(B) − P(A ∩ B)<br/>(works for both cases)</td>
            </tr>
        </table>

        <div class="success-box">
            <h4>Pro Tip</h4>
            <p>The formula P(A or B) = P(A) + P(B) − P(A ∩ B) works for <em>all</em> events, not just non-mutually exclusive ones. If A and B are mutually exclusive, P(A ∩ B) = 0, and you get P(A) + P(B). So you can always use the full formula!</p>
        </div>
        """
    },
    {
        "title": "The Complement Rule Revisited",
        "body": """
        <h3>Using Complements to Simplify "Or" Problems</h3>
        <p>Sometimes, finding P(A or B) directly is difficult. But finding P(neither A nor B) is easy. This is where complements shine.</p>

        <h4>The Relationship</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>\\(P(A \\text{ or } B) = 1 - P(\\text{neither } A \\text{ nor } B)\\)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Or equivalently: \\(P(A \\text{ or } B) = 1 - P(A' \\cap B')\\)</p>
        </div>

        <p><strong>Why?</strong> Either at least one of A or B happens, or neither happens. These are complementary events.</p>

        <div class="worked-example">
            <h4>Example 5: At Least One Success</h4>
            <p><strong>Scenario:</strong> You take two independent exams. Each has probability 0.7 of passing.</p>
            <p><strong>Question:</strong> What's the probability you pass at least one exam?</p>

            <p><strong>Direct approach:</strong> (Hard) Calculate P(pass first) + P(pass second) − P(pass both)</p>
            <ul>
                <li>\\(P(\\text{pass both}) = 0.7 \\times 0.7 = 0.49\\)</li>
                <li>\\(P(\\text{pass only first}) = 0.7 \\times 0.3 = 0.21\\)</li>
                <li>\\(P(\\text{pass only second}) = 0.3 \\times 0.7 = 0.21\\)</li>
                <li>\\(P(\\text{at least one}) = 0.49 + 0.21 + 0.21 = 0.91\\)</li>
            </ul>

            <p><strong>Complement approach:</strong> (Easier)</p>
            <ul>
                <li>\\(P(\\text{fail both}) = 0.3 \\times 0.3 = 0.09\\)</li>
                <li>\\(P(\\text{at least one pass}) = 1 - 0.09 = 0.91\\) ✓</li>
            </ul>
        </div>

        <h4>When to Use Complements</h4>
        <p>Use the complement when:</p>
        <ul>
            <li>"At least one" appears in the problem</li>
            <li>The complement is simpler (fewer cases to consider)</li>
            <li>Direct counting is tedious</li>
        </ul>

        <div class="concept-box">
            <h4>Example 6: Quality Control</h4>
            <p><strong>Question:</strong> A factory produces parts. Each part has a 2% defect rate. A batch of 50 parts is produced. What's the probability that at least one is defective?</p>

            <p><strong>Complement approach:</strong> Much easier than listing all ways to have 1, 2, 3, ..., or 50 defects!</p>
            <ul>
                <li>P(one part is good) = 0.98</li>
                <li>P(all 50 are good) = 0.98^50 ≈ 0.364</li>
                <li>P(at least one is defective) = 1 − 0.364 ≈ 0.636 or 63.6%</li>
            </ul>
            <p><strong>Interpretation:</strong> Even though each part has only a 2% defect rate, across 50 parts, it's more likely than not that at least one is defective.</p>
        </div>

        <p><strong>Lesson:</strong> Always consider whether the complement is simpler. Sometimes a quick complement calculation beats struggling with a complex direct approach.</p>
        """
    }
]
