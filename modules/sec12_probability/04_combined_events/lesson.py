TITLE = "Combined Events: When Two Things Happen Together"

SECTIONS = [
    {
        "title": "Two-Stage Experiments: Combining Outcomes",
        "body": """<h3>What Are Combined Events?</h3>
<p>Sometimes an experiment has multiple stages, and we want to find the probability of a combination of outcomes.</p>

<div class="concept-box">
<p><strong>Two-Stage Experiment:</strong> You perform two experiments one after the other (or two things happen at the same time)</p>
<p><strong>Combined Event:</strong> A specific outcome from both stages combined</p>
</div>

<div class="worked-example">
<h4>Example 1: Flip a Coin, Then Roll a Die</h4>
<p><strong>Stage 1:</strong> Flip a coin → {H, T}</p>
<p><strong>Stage 2:</strong> Roll a die → {1, 2, 3, 4, 5, 6}</p>

<p><strong>Sample Space (all combinations):</strong></p>
<p>{(H,1), (H,2), (H,3), (H,4), (H,5), (H,6), (T,1), (T,2), (T,3), (T,4), (T,5), (T,6)}</p>

<p><strong>Total possible outcomes:</strong> 2 × 6 = 12</p>

<p><strong>Some combined events:</strong></p>
<ul>
<li>P(H and 4) = 1/12</li>
<li>P(T and even number) = P(T and {2,4,6}) = 3/12 = 1/4</li>
<li>P(H and odd number) = P(H and {1,3,5}) = 3/12 = 1/4</li>
</ul>
</div>

<div class="worked-example">
<h4>Example 2: Spin a Spinner Twice</h4>
<p><strong>Spinner:</strong> 3 equal sections (Red, Blue, Green)</p>
<p><strong>Experiment:</strong> Spin twice</p>

<p><strong>Sample Space:</strong></p>
<p>{(R,R), (R,B), (R,G), (B,R), (B,B), (B,G), (G,R), (G,B), (G,G)}</p>

<p><strong>Total outcomes:</strong> 3 × 3 = 9</p>

<p><strong>Some probabilities:</strong></p>
<ul>
<li>P(both Red) = 1/9</li>
<li>P(first Red, second Blue) = 1/9</li>
<li>P(at least one Red) = {(R,R), (R,B), (R,G), (B,R), (G,R)} = 5/9</li>
</ul>
</div>

<div class="success-box">
<h4>Counting Rule for Combined Events</h4>
<p>If the first experiment has <strong>m</strong> outcomes and the second has <strong>n</strong> outcomes:</p>
<p><strong>Total combined outcomes = m × n</strong></p>
</div>"""
    },
    {
        "title": "Tree Diagrams: Visualizing All Possibilities",
        "body": """<h3>What is a Tree Diagram?</h3>
<p>A <strong>tree diagram</strong> is a visual way to show all possible outcomes of a two-stage experiment.</p>

<div class="worked-example">
<h4>Tree Diagram: Coin Then Die</h4>

<svg width="100%" height="240" viewBox="0 0 600 240" style="border-radius: 4px">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='14' font-weight='bold'>Tree Diagram: Flip Coin, Then Roll Die</text>

  <circle cx="100" cy="100" r="5" fill='#d29922'/>
  <text x="100" y="130" text-anchor='middle' fill='#e6edf3' font-size='11'>Start</text>

  <line x1="105" y1="95" x2="180" y2="60" stroke='#30363d' stroke-width="2"/>
  <text x="140" y="70" fill='#8b949e' font-size='11'>H (1/2)</text>

  <line x1="105" y1="105" x2="180" y2="140" stroke='#30363d' stroke-width="2"/>
  <text x="140" y="135" fill='#8b949e' font-size='11'>T (1/2)</text>

  <circle cx="185" cy="60" r="4" fill='#da3633'/>
  <circle cx="185" cy="140" r="4" fill='#da3633'/>

  <line x1="189" y1="56" x2="270" y2="30" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="60" x2="270" y2="50" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="64" x2="270" y2="70" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="68" x2="270" y2="90" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="72" x2="270" y2="110" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="76" x2="270" y2="130" stroke='#30363d' stroke-width="1"/>

  <text x="295" y="35" fill='#8b949e' font-size='9'>(H,1): 1/12</text>
  <text x="295" y="55" fill='#8b949e' font-size='9'>(H,2): 1/12</text>
  <text x="295" y="75" fill='#8b949e' font-size='9'>(H,3): 1/12</text>
  <text x="295" y="95" fill='#8b949e' font-size='9'>(H,4): 1/12</text>
  <text x="295" y="115" fill='#8b949e' font-size='9'>(H,5): 1/12</text>
  <text x="295" y="135" fill='#8b949e' font-size='9'>(H,6): 1/12</text>

  <line x1="189" y1="136" x2="270" y2="150" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="140" x2="270" y2="170" stroke='#30363d' stroke-width="1"/>
  <line x1="189" y1="144" x2="270" y2="190" stroke='#30363d' stroke-width="1"/>

  <text x="295" y="155" fill='#8b949e' font-size='9'>(T,1): 1/12</text>
  <text x="295" y="175" fill='#8b949e' font-size='9'>(T,2): 1/12</text>
  <text x="295" y="195" fill='#8b949e' font-size='9'>... (6 total)</text>
</svg>

<p><strong>How to read it:</strong></p>
<ol>
<li>Start from the left (the beginning)</li>
<li>Branches show the first outcome (Heads or Tails)</li>
<li>Each branch splits into more branches (1-6 for the die)</li>
<li>The path from start to the right shows one combined outcome</li>
</ol>

<p><strong>Counting outcomes:</strong> Each path from start to end is one outcome. Count the paths to find the sample space.</p>
</div>

<div class="worked-example">
<h4>Tree Diagram: Spinner Twice (Red, Blue, Green)</h4>

<svg width="100%" height="220" viewBox="0 0 500 220" style="border-radius: 4px">
  <text x="250" y="20" text-anchor='middle' fill='#e6edf3' font-size='14' font-weight='bold'>Spin Twice</text>

  <circle cx="80" cy="80" r="5" fill='#d29922'/>
  <line x1="85" y1="70" x2="150" y2="40" stroke='#30363d' stroke-width="2"/>
  <line x1="85" y1="80" x2="150" y2="80" stroke='#30363d' stroke-width="2"/>
  <line x1="85" y1="90" x2="150" y2="120" stroke='#30363d' stroke-width="2"/>

  <text x="115" y="55" fill='#8b949e' font-size='11'>R (1/3)</text>
  <text x="115" y="88" fill='#8b949e' font-size='11'>B (1/3)</text>
  <text x="115" y="118" fill='#8b949e' font-size='11'>G (1/3)</text>

  <circle cx="155" cy="40" r="4" fill='#da3633'/>
  <circle cx="155" cy="80" r="4" fill='#da3633'/>
  <circle cx="155" cy="120" r="4" fill='#da3633'/>

  <line x1="159" y1="37" x2="220" y2="20" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="43" x2="220" y2="45" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="49" x2="220" y2="70" stroke='#30363d' stroke-width="1"/>

  <line x1="159" y1="77" x2="220" y2="60" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="83" x2="220" y2="85" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="89" x2="220" y2="110" stroke='#30363d' stroke-width="1"/>

  <line x1="159" y1="117" x2="220" y2="140" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="123" x2="220" y2="165" stroke='#30363d' stroke-width="1"/>
  <line x1="159" y1="129" x2="220" y2="190" stroke='#30363d' stroke-width="1"/>

  <text x="240" y="25" fill='#8b949e' font-size='9'>(R,R): 1/9</text>
  <text x="240" y="50" fill='#8b949e' font-size='9'>(R,B): 1/9</text>
  <text x="240" y="75" fill='#8b949e' font-size='9'>(R,G): 1/9</text>
  <text x="240" y="90" fill='#8b949e' font-size='9'>(B,R): 1/9</text>
  <text x="240" y="115" fill='#8b949e' font-size='9'>(B,B): 1/9</text>
  <text x="240" y="140" fill='#8b949e' font-size='9'>(B,G): 1/9</text>
  <text x="240" y="170" fill='#8b949e' font-size='9'>(G,R): 1/9</text>
  <text x="240" y="195" fill='#8b949e' font-size='9'>(G,G): 1/9</text>
</svg>

<p><strong>Total outcomes:</strong> 3 × 3 = 9 (shown by 9 paths from start to end)</p>
</div>"""
    },
    {
        "title": "The Multiplication Rule: AND Events",
        "body": """<h3>When Outcomes Happen Together: Using AND</h3>

<div class="concept-box">
<p><strong>P(A and B) = P(A) × P(B)</strong></p>
<p>(when A and B are <strong>independent</strong> — one doesn't affect the other)</p>
</div>

<p><strong>Independent events:</strong> The result of the first doesn't change the probability of the second. Rolling two dice, flipping a coin then rolling a die, or spinning a spinner twice are all independent.</p>

<div class="worked-example">
<h4>Example 1: Rolling Two Dice</h4>
<p><strong>Question:</strong> What is P(both dice show a 3)?</p>

<p><strong>Method 1: Using the formula</strong></p>
<ul>
<li>\\(P(\\text{first die is 3}) = \\frac{1}{6}\\)</li>
<li>\\(P(\\text{second die is 3}) = \\frac{1}{6}\\)</li>
<li>\\(P(\\text{both are 3}) = \\frac{1}{6} \\times \\frac{1}{6} = \\frac{1}{36}\\)</li>
</ul>

<p><strong>Method 2: Counting</strong></p>
<ul>
<li>Sample space has 6 × 6 = 36 outcomes</li>
<li>Only one outcome is (3,3)</li>
<li>P = 1/36</li>
</ul>
</div>

<div class="worked-example">
<h4>Example 2: Coin and Die</h4>
<p><strong>Question:</strong> What is P(getting Heads AND rolling a 5)?</p>

<p><strong>Solution:</strong></p>
<ul>
<li>\\(P(\\text{Heads}) = \\frac{1}{2}\\)</li>
<li>\\(P(\\text{rolling a 5}) = \\frac{1}{6}\\)</li>
<li>\\(P(\\text{Heads AND 5}) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12}\\)</li>
</ul>
</div>

<div class="worked-example">
<h4>Example 3: Picking Colored Balls with AND</h4>
<p><strong>Scenario:</strong> A bag has 3 red and 7 blue balls. Pick a ball, put it back, pick again.</p>

<p><strong>Question:</strong> What is P(red, then blue)?</p>

<p><strong>Solution:</strong></p>
<ul>
<li>\\(P(\\text{first is red}) = \\frac{3}{10}\\)</li>
<li>\\(P(\\text{second is blue}) = \\frac{7}{10}\\) (we put the first back, so nothing changed)</li>
<li>\\(P(\\text{red, then blue}) = \\frac{3}{10} \\times \\frac{7}{10} = \\frac{21}{100} = 0.21\\)</li>
</ul>
</div>

<div class="success-box">
<h4>When Do You Use Multiplication?</h4>
<p>Use the multiplication rule when you have the word <strong>AND</strong>. You want both things to happen.</p>
<p>Examples: "both heads," "die shows 3 AND coin shows tails," "first ball is red AND second is blue"</p>
</div>"""
    },
    {
        "title": "The Addition Rule: OR Events",
        "body": """<h3>When Either Outcome Works: Using OR</h3>

<div class="concept-box">
<p><strong>P(A or B) = P(A) + P(B)</strong></p>
<p>(when A and B are <strong>mutually exclusive</strong> — they cannot both happen at once)</p>
</div>

<p><strong>Mutually exclusive:</strong> If one event happens, the other cannot. Getting a 2 or 5 on a die are mutually exclusive (you can't roll both at once).</p>

<div class="worked-example">
<h4>Example 1: Rolling a Die (OR)</h4>
<p><strong>Question:</strong> What is P(rolling a 2 OR rolling a 5)?</p>

<p><strong>Solution:</strong></p>
<ul>
<li>\\(P(\\text{rolling a 2}) = \\frac{1}{6}\\)</li>
<li>\\(P(\\text{rolling a 5}) = \\frac{1}{6}\\)</li>
<li>These cannot both happen at once (mutually exclusive)</li>
<li>\\(P(\\text{2 or 5}) = \\frac{1}{6} + \\frac{1}{6} = \\frac{2}{6} = \\frac{1}{3}\\)</li>
</ul>
</div>

<div class="worked-example">
<h4>Example 2: Rolling Odd Numbers</h4>
<p><strong>Question:</strong> What is P(rolling an odd number)?</p>

<p><strong>Solution:</strong></p>
<ul>
<li>Odd numbers: 1, 3, 5</li>
<li>\\(P(1) = \\frac{1}{6}\\), \\(P(3) = \\frac{1}{6}\\), \\(P(5) = \\frac{1}{6}\\)</li>
<li>These are mutually exclusive</li>
<li>\\(P(\\text{odd}) = \\frac{1}{6} + \\frac{1}{6} + \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2}\\)</li>
</ul>
</div>

<div class="worked-example">
<h4>Example 3: Spinner (OR)</h4>
<p><strong>Spinner has 4 equal sections:</strong> Red, Blue, Green, Yellow</p>

<p><strong>Question:</strong> What is P(Red OR Yellow)?</p>

<p><strong>Solution:</strong></p>
<ul>
<li>\\(P(\\text{Red}) = \\frac{1}{4}\\)</li>
<li>\\(P(\\text{Yellow}) = \\frac{1}{4}\\)</li>
<li>\\(P(\\text{Red OR Yellow}) = \\frac{1}{4} + \\frac{1}{4} = \\frac{2}{4} = \\frac{1}{2}\\)</li>
</ul>
</div>

<div class="success-box">
<h4>When Do You Use Addition?</h4>
<p>Use the addition rule when you have the word <strong>OR</strong>. Either outcome is acceptable.</p>
<p>Examples: "rolling a 2 or a 5," "spinning red or blue," "getting heads or tails"</p>
<p><strong>Important:</strong> The outcomes must be mutually exclusive (can't both happen).</p>
</div>"""
    },
    {
        "title": "Practice: Combined Events and Rules",
        "body": """<h3>Check Your Understanding</h3>

<div class="worked-example">
<h4>Problem 1: Multiplication Rule</h4>
<p><strong>Question:</strong> A coin is flipped and a die is rolled. What is P(Heads AND rolling a 6)?</p>
<p><strong>Answer:</strong> \\(P(\\text{Heads and 6}) = \\frac{1}{2} \\times \\frac{1}{6} = \\frac{1}{12}\\)</p>
<p><strong>Explanation:</strong> Use multiplication because we want both things to happen. These are independent events.</p>
</div>

<div class="worked-example">
<h4>Problem 2: Addition Rule</h4>
<p><strong>Question:</strong> What is P(rolling a 1 OR a 6)?</p>
<p><strong>Answer:</strong> \\(P(\\text{1 or 6}) = \\frac{1}{6} + \\frac{1}{6} = \\frac{2}{6} = \\frac{1}{3}\\)</p>
<p><strong>Explanation:</strong> Use addition because we want either outcome. These are mutually exclusive.</p>
</div>

<div class="worked-example">
<h4>Problem 3: Combining Rules</h4>
<p><strong>Question:</strong> Spin a spinner twice. The spinner has 2 red and 3 blue sections (total 5). What is P(first spin is red AND second spin is blue)?</p>
<p><strong>Answer:</strong> \\(P(\\text{red, then blue}) = \\frac{2}{5} \\times \\frac{3}{5} = \\frac{6}{25} = 0.24\\)</p>
<p><strong>Explanation:</strong> This is a two-stage experiment with independent stages. Use multiplication.</p>
</div>

<div class="worked-example">
<h4>Problem 4: Complex Combined Events</h4>
<p><strong>Question:</strong> A spinner has 3 equal sections: A, B, C. Spin twice. What is P(first is A or B, then second is C)?</p>
<p><strong>Answer:</strong> \\(P(\\text{A or B, then C}) = (\\frac{1}{3} + \\frac{1}{3}) \\times \\frac{1}{3} = \\frac{2}{3} \\times \\frac{1}{3} = \\frac{2}{9}\\)</p>
<p><strong>Explanation:</strong> P(A or B) = 2/3 (using addition). Then multiply by P(C) because both parts must happen (multiplication).</p>
</div>"""
    }
]
