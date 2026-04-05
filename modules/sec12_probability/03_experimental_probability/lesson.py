TITLE = "Experimental Probability: Testing Reality"

SECTIONS = [
    {
        "title": "From Theory to Reality: Experimental vs Theoretical",
        "body": """<h3>Two Different Kinds of Probability</h3>

<div class="concept-box">
<p><strong>Theoretical Probability:</strong> What we calculate based on the structure of the experiment (assuming fair equipment)</p>
<p><strong>Experimental Probability:</strong> What we actually observe when we perform the experiment</p>
</div>

<h3>The Experimental Probability Formula</h3>
<p><strong>P(event) = Number of times the event occurred / Total number of trials</strong></p>
<p>Also called <strong>relative frequency</strong> or <strong>observed probability</strong>.</p>

<div class="worked-example">
<h4>Flipping a Coin: Theory vs Reality</h4>
<p><strong>Theoretical Probability:</strong></p>
<ul>
<li>\\(P(\\text{Heads}) = \\frac{1}{2} = 0.5\\) or 50%</li>
<li>\\(P(\\text{Tails}) = \\frac{1}{2} = 0.5\\) or 50%</li>
</ul>

<p><strong>Experiment: Flip a fair coin 100 times</strong></p>
<p><strong>Results (actual outcomes):</strong></p>
<ul>
<li>Heads: 52 times</li>
<li>Tails: 48 times</li>
</ul>

<p><strong>Experimental Probability:</strong></p>
<ul>
<li>\\(P(\\text{Heads}) = \\frac{52}{100} = 0.52\\) or 52%</li>
<li>\\(P(\\text{Tails}) = \\frac{48}{100} = 0.48\\) or 48%</li>
</ul>

<p><strong>What do we notice?</strong> The experimental results (52%, 48%) are close to the theoretical predictions (50%, 50%), but not exactly the same. Small differences happen due to chance!</p>
</div>

<div class="worked-example">
<h4>Rolling a Die: Comparing Theory and Practice</h4>
<p><strong>Theoretical Probability:</strong> Each number 1-6 should appear 1/6 ≈ 16.7% of the time</p>

<p><strong>Experiment: Roll a die 60 times</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 10px 0">
<tr >
<td style="padding: 8px;"><strong>Number</strong></td>
<td style="padding: 8px;"><strong>Times Rolled</strong></td>
<td style="padding: 8px;"><strong>Experimental P</strong></td>
<td style="padding: 8px;"><strong>Theoretical P</strong></td>
</tr>
<tr >
<td style="padding: 8px;">1</td>
<td style="padding: 8px;">12</td>
<td style="padding: 8px;">12/60 = 0.20</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
<tr >
<td style="padding: 8px;">2</td>
<td style="padding: 8px;">10</td>
<td style="padding: 8px;">10/60 ≈ 0.167</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
<tr >
<td style="padding: 8px;">3</td>
<td style="padding: 8px;">11</td>
<td style="padding: 8px;">11/60 ≈ 0.183</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
<tr >
<td style="padding: 8px;">4</td>
<td style="padding: 8px;">9</td>
<td style="padding: 8px;">9/60 = 0.15</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
<tr >
<td style="padding: 8px;">5</td>
<td style="padding: 8px;">10</td>
<td style="padding: 8px;">10/60 ≈ 0.167</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
<tr >
<td style="padding: 8px;">6</td>
<td style="padding: 8px;">8</td>
<td style="padding: 8px;">8/60 ≈ 0.133</td>
<td style="padding: 8px;">1/6 ≈ 0.167</td>
</tr>
</table>

<p><strong>Observation:</strong> The experimental probabilities vary slightly from 1/6, but they're all in the same ballpark. The die appears to be fair!</p>
</div>"""
    },
    {
        "title": "The Law of Large Numbers: A Powerful Pattern",
        "body": """<h3>What Happens With More and More Trials?</h3>
<p><strong>The Law of Large Numbers:</strong> As we perform more and more trials, the experimental probability gets closer and closer to the theoretical probability.</p>

<div class="concept-box">
<p>With few trials, randomness can give wild results.</p>
<p>With many trials, the results settle down to what we theoretically predict.</p>
</div>

<div class="worked-example">
<h4>Coin Flipping: How Trials Change the Pattern</h4>

<p><strong>After 10 flips:</strong></p>
<ul>
<li>Got 7 heads</li>
<li>Experimental P(heads) = 7/10 = 0.7 (far from theoretical 0.5)</li>
</ul>

<p><strong>After 100 flips:</strong></p>
<ul>
<li>Got 52 heads</li>
<li>Experimental P(heads) = 52/100 = 0.52 (closer to theoretical 0.5)</li>
</ul>

<p><strong>After 1000 flips:</strong></p>
<ul>
<li>Got 503 heads</li>
<li>Experimental P(heads) = 503/1000 = 0.503 (very close to theoretical 0.5)</li>
</ul>

<p><strong>After 10,000 flips:</strong></p>
<ul>
<li>Got 5018 heads</li>
<li>Experimental P(heads) = 5018/10000 = 0.5018 (extremely close to theoretical 0.5)</li>
</ul>

<p><strong>The pattern is clear:</strong> More trials → Experimental probability approaches theoretical probability!</p>
</div>

<svg width="100%" height="200" viewBox="0 0 620 200" style="border-radius: 4px; margin: 15px 0">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='14' font-weight='bold'>Experimental P(Heads) Approaching Theoretical P = 0.5</text>

  <line x1="50" y1="50" x2="550" y2="50" stroke='#30363d' stroke-width="1"/>
  <line x1="50" y1="150" x2="550" y2="150" stroke='#30363d' stroke-width="1"/>
  <line x1="50" y1="50" x2="50" y2="150" stroke='#30363d' stroke-width="2"/>
  <line x1="550" y1="50" x2="550" y2="150" stroke='#30363d' stroke-width="2"/>

  <line x1="50" y1="100" x2="550" y2="100" stroke='#d29922' stroke-width="2" stroke-dasharray="5,5"/>

  <circle cx="120" cy="65" r="5" fill='#da3633'/>
  <text x="120" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>10</text>

  <circle cx="210" cy="92" r="5" fill='#da3633'/>
  <text x="210" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>100</text>

  <circle cx="300" cy="99" r="5" fill='#da3633'/>
  <text x="300" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>1000</text>

  <circle cx="390" cy="100" r="5" fill='#da3633'/>
  <text x="390" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>10K</text>

  <circle cx="480" cy="101" r="5" fill='#da3633'/>
  <text x="480" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>100K</text>

  <text x="570" y="107" fill='#d29922' font-size='11'>Theory</text>
  <text x="30" y="95" fill='#e6edf3' font-size='11'>P = 1.0</text>
  <text x="30" y="155" fill='#e6edf3' font-size='11'>P = 0</text>
  <text x="300" y="30" fill='#8b949e' font-size='11'>Number of Trials →</text>
</svg>

<div class="success-box">
<h4>Why Does This Happen?</h4>
<p>With few trials, random luck can push the results one way. A coin might land heads 7 times out of 10 just by chance!</p>
<p>But with many trials, the luck "averages out." In 1000 flips, the occasional unlucky streak doesn't change the overall pattern much.</p>
</div>"""
    },
    {
        "title": "Comparing Theoretical and Experimental Probability",
        "body": """<h3>When Should You Use Which?</h3>

<div class="concept-box">
<p><strong>Theoretical Probability:</strong> Use when equipment is fair and you can count outcomes mathematically</p>
<p><strong>Experimental Probability:</strong> Use when equipment might be biased, or to verify theoretical predictions</p>
</div>

<div class="worked-example">
<h4>Is This Die Fair?</h4>
<p><strong>Scenario:</strong> You have an old die that might be weighted.</p>

<p><strong>What to do:</strong></p>
<ol>
<li>Calculate theoretical P(each number) = 1/6 ≈ 0.167</li>
<li>Roll the die many times (at least 100 times, ideally 1000+)</li>
<li>Calculate experimental P for each number</li>
<li>Compare: Are they close? If yes, the die is probably fair. If no, it's probably biased.</li>
</ol>

<p><strong>Example results from rolling 600 times:</strong></p>
<ul>
<li>Number 1: 95 times → Experimental P = 95/600 ≈ 0.158 (close to 0.167) ✓</li>
<li>Number 2: 102 times → Experimental P = 102/600 = 0.17 (close to 0.167) ✓</li>
<li>Number 3: 98 times → Experimental P ≈ 0.163 (close to 0.167) ✓</li>
<li>Number 4: 101 times → Experimental P ≈ 0.168 (close to 0.167) ✓</li>
<li>Number 5: 99 times → Experimental P ≈ 0.165 (close to 0.167) ✓</li>
<li>Number 6: 105 times → Experimental P = 105/600 = 0.175 (close to 0.167) ✓</li>
</ul>

<p><strong>Conclusion:</strong> All experimental probabilities are very close to the theoretical 1/6. The die appears to be fair!</p>
</div>

<div class="worked-example">
<h4>A Suspicious Spinner</h4>
<p><strong>Scenario:</strong> A spinner has 4 sections that look equal, but you suspect it might be weighted.</p>

<p><strong>Theoretical prediction:</strong> Each section should appear 1/4 = 0.25 of the time</p>

<p><strong>Experiment: Spin 400 times</strong></p>
<ul>
<li>Red: 95 times → Experimental P = 95/400 ≈ 0.238 (close to 0.25) ✓</li>
<li>Blue: 98 times → Experimental P ≈ 0.245 (close to 0.25) ✓</li>
<li>Green: 102 times → Experimental P ≈ 0.255 (close to 0.25) ✓</li>
<li>Yellow: 105 times → Experimental P ≈ 0.263 (close to 0.25, slightly high)</li>
</ul>

<p><strong>Conclusion:</strong> The spinner looks fair. Small variations are just random chance with 400 trials.</p>
</div>

<div class="warning-box">
<h4>Important: How Many Trials Do You Need?</h4>
<p>The more trials, the more confident you can be.</p>
<ul>
<li><strong>10-50 trials:</strong> Expect large random variations</li>
<li><strong>100-500 trials:</strong> Good for checking if something is roughly fair</li>
<li><strong>1000+ trials:</strong> Experimental probability closely matches theory</li>
</ul>
</div>"""
    },
    {
        "title": "Practice: Experimental Probability and Large Numbers",
        "body": """<h3>Check Your Understanding</h3>

<div class="worked-example">
<h4>Problem 1: Calculating Experimental Probability</h4>
<p><strong>Question:</strong> In 200 coin flips, heads appeared 108 times. What is the experimental P(heads)?</p>
<p><strong>Answer:</strong> \\(P(\\text{heads}) = \\frac{108}{200} = 0.54\\) or 54%</p>
<p><strong>Explanation:</strong> Experimental P = (times it happened) / (total trials). Note: This is close to, but not exactly, the theoretical 0.5.</p>
</div>

<div class="worked-example">
<h4>Problem 2: Understanding the Law of Large Numbers</h4>
<p><strong>Question:</strong> After 50 die rolls, you get 15 sixes. After 500 die rolls, you get 82 sixes. Which is closer to the theoretical prediction?</p>
<p><strong>Answer:</strong> The 500-roll experiment (82/500 = 0.164 vs theoretical 1/6 ≈ 0.167)</p>
<p><strong>Explanation:</strong> 15/50 = 0.3, which is far from 1/6. The 500-roll experiment has more trials, so it's more likely to be closer to the theoretical probability due to the Law of Large Numbers.</p>
</div>

<div class="worked-example">
<h4>Problem 3: Testing for Fairness</h4>
<p><strong>Question:</strong> A spinner has 3 equal-looking sections (A, B, C). Theoretical P for each = 1/3 ≈ 0.333. After 300 spins: A = 95, B = 102, C = 103. Is the spinner likely fair?</p>
<p><strong>Answer:</strong> Yes, the spinner is likely fair.</p>
<p><strong>Explanation:</strong> Experimental probabilities: A = 95/300 ≈ 0.317, B = 102/300 = 0.34, C = 103/300 ≈ 0.343. These are all very close to 1/3 ≈ 0.333. The small variations are normal random chance.</p>
</div>

<div class="worked-example">
<h4>Problem 4: Comparing Theoretical and Experimental</h4>
<p><strong>Question:</strong> A bag has 6 red and 4 blue balls. Theoretical P(red) = 6/10 = 0.6. After 1000 draws (with replacement): red = 598 times. What is the experimental probability?</p>
<p><strong>Answer:</strong> \\(P(\\text{red}) = \\frac{598}{1000} = 0.598\\) or 59.8%</p>
<p><strong>Explanation:</strong> This is extremely close to the theoretical 0.6. With 1000 trials, the experimental probability matches the theory very well!</p>
</div>"""
    }
]
