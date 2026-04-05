TITLE = "Conditional Probability & Independence"

SECTIONS = [
    {
        "title": "Understanding Conditional Probability",
        "body": """
        <h3>Probability Changes When We Have New Information</h3>
        <p>Imagine you draw a card and see it's red, but you don't see which suit. Now I ask: "What's the probability it's a heart?" Your answer should change because you have information—the card is already red, which eliminates all 26 black cards.</p>

        <p>This is <strong>conditional probability</strong>: the probability of an event given that something else has already happened.</p>

        <h4>The Conditional Probability Formula</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="font-size: 1.1em; margin: 0"><strong>P(A|B) = P(A ∩ B) / P(B)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Read: "Probability of A given B"</p>
        </div>

        <p><strong>Breaking it down:</strong></p>
        <ul>
            <li><strong>P(A|B)</strong> = probability of A happening, given that B has happened</li>
            <li><strong>P(A ∩ B)</strong> = probability of both A and B happening</li>
            <li><strong>P(B)</strong> = probability of B happening</li>
        </ul>

        <p><strong>Intuition:</strong> We restrict our sample space to only outcomes where B occurred, then ask what fraction of those also have A.</p>

        <div class="worked-example">
            <h4>Example 1: Drawing a Red Card That's a Heart</h4>
            <p><strong>Question:</strong> Given that a card is red, what's the probability it's a heart?</p>
            <p><strong>Given information:</strong> The card is red (26 possibilities: 13 hearts + 13 diamonds)</p>
            <p><strong>Favorable outcomes:</strong> Red cards that are hearts = 13</p>
            <p><strong>P(Heart | Red) = 13/26 = 1/2</strong></p>
            <p><strong>Using the formula:</strong></p>
            <ul>
                <li>P(Heart AND Red) = 13/52 (13 hearts out of 52 cards)</li>
                <li>P(Red) = 26/52 (26 red cards)</li>
                <li>P(Heart | Red) = (13/52) / (26/52) = 13/26 = 1/2</li>
            </ul>
        </div>

        <h4>Why the Formula Works</h4>
        <p>Think of it as restricting your universe. When B occurs, our sample space shrinks to only outcomes where B is true. We now find what fraction of <em>those</em> outcomes include A.</p>

        <div class="concept-box">
            <h4>Example 2: Drawing Two Cards Without Replacement</h4>
            <p><strong>Question:</strong> If the first card is a heart, what's the probability the second is also a heart?</p>
            <p><strong>Original deck:</strong> 52 cards, 13 hearts</p>
            <p><strong>After first card (a heart):</strong> 51 cards remain, 12 hearts</p>
            <p><strong>P(2nd Heart | 1st Heart) = 12/51</strong></p>
            <p><strong>Why?</strong> Given that a heart was drawn, we don't go back to 13/52. We're working with 51 cards, of which 12 are hearts.</p>
        </div>

        <div class="warning-box">
            <h4>Critical Point</h4>
            <p>Conditional probability uses the new, restricted sample space. Always update the denominator based on what you know!</p>
        </div>
        """
    },
    {
        "title": "Independence: When New Information Doesn't Matter",
        "body": """
        <h3>Independent Events vs. Dependent Events</h3>
        <p>Sometimes learning that event B occurred tells us nothing about whether A will happen. These are <strong>independent events</strong>. Other times, B completely changes the likelihood of A. These are <strong>dependent events</strong>.</p>

        <h4>The Key Test for Independence</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>Events A and B are independent if and only if:</strong></p>
            <p style="font-size: 1.1em; margin: 10px 0 0 0"><strong>P(A|B) = P(A)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Knowing B occurred doesn't change the probability of A</p>
        </div>

        <p><strong>Equivalently:</strong> A and B are independent if P(A ∩ B) = P(A) × P(B)</p>

        <p><strong>Why?</strong> If P(A|B) = P(A), then:</p>
        <ul>
            <li>P(A ∩ B) / P(B) = P(A)</li>
            <li>P(A ∩ B) = P(A) × P(B) ✓</li>
        </ul>

        <div class="worked-example">
            <h4>Example 3: Rolling a Die vs. Flipping a Coin</h4>
            <p><strong>Question:</strong> Are "rolling a 4" and "flipping heads" independent?</p>
            <p><strong>P(4) = 1/6</strong></p>
            <p><strong>P(4 | Heads) = 1/6</strong> (coin flip doesn't affect die roll)</p>
            <p><strong>Conclusion:</strong> Since P(4) = P(4 | Heads), these are independent events.</p>
            <p><strong>Also check:</strong> P(4 AND Heads) = 1/6 × 1/2 = 1/12, and P(4) × P(Heads) = 1/6 × 1/2 = 1/12 ✓</p>
        </div>

        <div class="concept-box">
            <h4>Example 4: Drawing from a Deck With and Without Replacement</h4>
            <p><strong>Without Replacement (Dependent):</strong></p>
            <p>P(2nd Heart | 1st Heart) = 12/51 ≠ 13/52 = P(2nd Heart)</p>
            <p>Knowing the first card was a heart changes the probability for the second.</p>

            <p><strong>With Replacement (Independent):</strong></p>
            <p>P(2nd Heart | 1st Heart) = 13/52 = P(2nd Heart)</p>
            <p>Knowing the first card was a heart doesn't change the probability for the second (card returns).</p>
        </div>

        <h4>Real-World Context</h4>
        <p>Independent events are rare in complex situations. But they're common when:</p>
        <ul>
            <li>Events are in different experiments (coin flip and die roll)</li>
            <li>Events are with replacement</li>
            <li>Events truly don't affect each other (weather today vs. your exam score)</li>
        </ul>

        <p>Dependent events occur when:</p>
        <ul>
            <li>Drawing without replacement</li>
            <li>Sequential causes and effects</li>
            <li>Shared underlying factors</li>
        </ul>
        """
    },
    {
        "title": "The Multiplication Rule for Independent Events",
        "body": """
        <h3>Simplifying Probabilities When Independence Holds</h3>
        <p>When events are independent, calculating joint probabilities becomes much simpler.</p>

        <h4>The Multiplication Rule (Independent Events)</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="font-size: 1.1em; margin: 0"><strong>P(A and B) = P(A) × P(B)</strong></p>
            <p style="font-size: 0.9em; margin: 10px 0 0 0">Only works when A and B are independent!</p>
        </div>

        <p><strong>Why this works:</strong> If knowing B doesn't change P(A), then P(A|B) = P(A), so:</p>
        <p style="text-align: center">P(A and B) = P(A|B) × P(B) = P(A) × P(B)</p>

        <div class="worked-example">
            <h4>Example 5: Two Fair Coins</h4>
            <p><strong>Question:</strong> What's the probability of getting heads on both coins?</p>
            <p><strong>P(Heads on coin 1) = 1/2</strong></p>
            <p><strong>P(Heads on coin 2) = 1/2</strong></p>
            <p><strong>These are independent (one coin doesn't affect the other)</strong></p>
            <p><strong>P(Both Heads) = 1/2 × 1/2 = 1/4</strong></p>
        </div>

        <div class="worked-example">
            <h4>Example 6: Rolling Two Dice</h4>
            <p><strong>Question:</strong> What's the probability of rolling a 3 on the first die and a 5 on the second?</p>
            <p><strong>P(3 on first) = 1/6</strong></p>
            <p><strong>P(5 on second) = 1/6</strong></p>
            <p><strong>P(3 and 5) = 1/6 × 1/6 = 1/36</strong></p>
        </div>

        <h4>Extending to Multiple Independent Events</h4>
        <p>The rule extends: if A, B, and C are mutually independent:</p>

        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>P(A and B and C) = P(A) × P(B) × P(C)</strong></p>
        </div>

        <div class="concept-box">
            <h4>Example 7: Three Coin Flips</h4>
            <p><strong>Question:</strong> What's the probability of getting heads on all three flips?</p>
            <p><strong>P(HHH) = 1/2 × 1/2 × 1/2 = 1/8</strong></p>
            <p><strong>Note:</strong> Total outcomes = 2³ = 8 (HHH, HHT, HTH, HTT, THH, THT, TTH, TTT). Only 1 is all heads. ✓</p>
        </div>

        <div class="warning-box">
            <h4>Critical Mistake to Avoid</h4>
            <p><strong>Don't use this formula for dependent events!</strong></p>
            <p>Example: Drawing cards without replacement.</p>
            <p>Wrong: P(both hearts) = 13/52 × 13/52 = 169/2704 ≈ 0.062</p>
            <p>Correct: P(both hearts) = 13/52 × 12/51 = 156/2652 ≈ 0.0588</p>
            <p>The first formula ignores that the second draw has fewer cards!</p>
        </div>
        """
    }
]
