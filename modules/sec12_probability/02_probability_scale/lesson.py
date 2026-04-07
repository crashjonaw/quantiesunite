TITLE = "The Probability Scale"

SECTIONS = [
    {
        "title": "From 0 to 1: The Probability Number Line",
        "body": """<h3>Understanding the Scale</h3>
<p>All probabilities are numbers between <strong>0 and 1</strong> (or between <strong>0% and 100%</strong>).</p>

<div class="concept-box">
<p><strong>Probability 0 (0%):</strong> Impossible — will NEVER happen</p>
<p><strong>Probability 0.5 (50%):</strong> Even chance — equally likely to happen or not</p>
<p><strong>Probability 1 (100%):</strong> Certain — MUST happen</p>
</div>

<svg width="100%" viewBox="0 0 620 120" style="max-width:640px;">
  <line x1="50" y1="55" x2="570" y2="55" stroke="currentColor" stroke-width="2.5" opacity="0.3"/>
  <circle cx="50" cy="55" r="7" fill="#da3633"/>
  <circle cx="570" cy="55" r="7" fill="#3fb950"/>
  <circle cx="310" cy="55" r="7" fill="#d29922"/>

  <text x="50" y="85" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="sans-serif">0 (Impossible)</text>
  <text x="310" y="85" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="sans-serif">0.5 (Even Chance)</text>
  <text x="570" y="85" text-anchor="middle" fill="currentColor" font-size="13" font-weight="bold" font-family="sans-serif">1 (Certain)</text>

  <text x="180" y="35" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="12" font-family="sans-serif">Unlikely</text>
  <text x="440" y="35" text-anchor="middle" fill="currentColor" opacity="0.6" font-size="12" font-family="sans-serif">Likely</text>
</svg>

<div class="worked-example">
<h4>Probability Examples on the Scale</h4>
<ul>
<li><strong>P(rolling a 7 on a standard die):</strong> 0 (impossible — a die only goes 1-6)</li>
<li><strong>P(rolling a 1 on a fair die):</strong> \(\frac{1}{6} \approx 0.167\) (unlikely, but possible)</li>
<li><strong>P(rolling an even number):</strong> \(\frac{1}{2} = 0.5\) (even chance)</li>
<li><strong>P(rolling 1, 2, 3, 4, 5, or 6):</strong> 1 (certain — must happen)</li>
<li><strong>P(coin landing on heads or tails):</strong> 1 (certain)</li>
</ul>
</div>"""
    },
    {
        "title": "The Complement Rule: If NOT, Then...",
        "body": """<h3>What is a Complement?</h3>
<p>The <strong>complement</strong> of an event is everything that is NOT that event.</p>

<div class="concept-box">
<p>If P(event happens) = p</p>
<p>Then P(event does NOT happen) = 1 − p</p>
<p>Or in other words: <strong>P(A) + P(not A) = 1</strong></p>
</div>

<div class="worked-example">
<h4>Example 1: Rolling a Die</h4>
<p><strong>Event A:</strong> Rolling a 4</p>
<p><strong>P(rolling a 4):</strong> \\(\\frac{1}{6}\\)</p>
<p><strong>Complement (NOT rolling a 4):</strong> Rolling {1, 2, 3, 5, 6}</p>
<p><strong>P(NOT rolling a 4):</strong> \\(1 - \\frac{1}{6} = \\frac{5}{6}\\)</p>
<p><strong>Check:</strong> \\(\\frac{1}{6} + \\frac{5}{6} = \\frac{6}{6} = 1\\) ✓</p>
</div>

<div class="worked-example">
<h4>Example 2: Drawing Colored Balls</h4>
<p><strong>A bag contains:</strong> 3 red, 7 other-colored balls (total 10)</p>
<p><strong>P(red):</strong> \\(\\frac{3}{10} = 0.3\\)</p>
<p><strong>P(NOT red):</strong> \\(1 - 0.3 = 0.7 = \\frac{7}{10}\\)</p>
<p><strong>This makes sense:</strong> If 3 are red, then 7 are not red. \(\frac{7}{10} = 0.7\)</p>
</div>

<div class="worked-example">
<h4>Example 3: Coin Flip</h4>
<p><strong>Event A:</strong> Getting heads</p>
<p><strong>P(heads):</strong> \\(\\frac{1}{2} = 0.5\\)</p>
<p><strong>P(NOT heads, i.e., tails):</strong> \\(1 - \\frac{1}{2} = \\frac{1}{2} = 0.5\\)</p>
<p><strong>Both outcomes are equally likely!</strong></p>
</div>

<div class="success-box">
<h4>Why is the Complement Rule Useful?</h4>
<p>Sometimes it's easier to calculate the probability of the complement than the event itself. For example:</p>
<p><strong>Question:</strong> What's P(at least one heads in 4 coin flips)?</p>
<p><strong>Easier approach:</strong> Calculate P(no heads at all), then use the complement!</p>
</div>"""
    },
    {
        "title": "Real-World Probability: Understanding Risk",
        "body": """<h3>Probability in Everyday Life</h3>
<p>Probability helps us understand risk and make decisions.</p>

<div class="worked-example">
<h4>Weather Forecasting</h4>
<p><strong>News report:</strong> "30% chance of rain tomorrow"</p>
<p><strong>What this means:</strong></p>
<ul>
<li>\(P(\text{rain}) = 0.3\) or \(30\%\)</li>
<li>\(P(\text{no rain}) = 1 - 0.3 = 0.7\) or \(70\%\)</li>
</ul>
<p><strong>Conclusion:</strong> It's more likely NOT to rain. You probably don't need an umbrella, but keep one just in case!</p>
</div>

<div class="worked-example">
<h4>Lottery Odds</h4>
<p><strong>A lottery might have:</strong> 1 in 1,000,000 chance of winning the jackpot</p>
<p><strong>P(winning):</strong> \\(\\frac{1}{1,000,000} = 0.000001\\) (extremely tiny!)</p>
<p><strong>P(not winning):</strong> \\(1 - 0.000001 = 0.999999\\) (extremely high)</p>
<p><strong>Conclusion:</strong> You're almost certainly not going to win. Don't depend on it!</p>
</div>

<div class="worked-example">
<h4>Medical Testing</h4>
<p><strong>A medical test is 95% accurate.</strong></p>
<ul>
<li>If you have the disease, it correctly identifies it 95% of the time (5% false negatives)</li>
<li>If you don't have the disease, it correctly says no 95% of the time (5% false positives)</li>
</ul>
<p><strong>P(positive test | you have disease):</strong> 0.95</p>
<p><strong>P(negative test | you don't have disease):</strong> 0.95</p>
</div>

<div class="warning-box">
<h4>Important: Probability ≠ Guarantee</h4>
<p>Just because something has a high probability doesn't mean it will happen. And just because it has a low probability doesn't mean it can't happen!</p>
<ul>
<li>Even if \(P = 0.99\) (99% likely), the 1% can still occur</li>
<li>Even if \(P = 0.01\) (1% likely), it might still happen</li>
<li>Probability describes the long-run frequency over many trials</li>
</ul>
</div>"""
    },
    {
        "title": "Practice: The Probability Scale and Complements",
        "body": """<h3>Check Your Understanding</h3>

<div class="worked-example">
<h4>Problem 1: Reading the Scale</h4>
<p><strong>Question:</strong> If P(event) = 0.15, is this event likely or unlikely?</p>
<p><strong>Answer:</strong> Unlikely (close to 0)</p>
<p><strong>Explanation:</strong> 0.15 is closer to 0 than to 1, so the event is unlikely.</p>
</div>

<div class="worked-example">
<h4>Problem 2: Using the Complement Rule</h4>
<p><strong>Question:</strong> A student passes a test with probability 0.8. What is the probability they fail?</p>
<p><strong>Answer:</strong> \(P(\text{fail}) = 1 - 0.8 = 0.2\) or \(20\%\)</p>
<p><strong>Explanation:</strong> The complement of passing is failing. Use P(not A) = 1 − P(A).</p>
</div>

<div class="worked-example">
<h4>Problem 3: Real-World Application</h4>
<p><strong>Question:</strong> The probability your flight is on time is 0.92. What is the probability it's delayed?</p>
<p><strong>Answer:</strong> \(P(\text{delayed}) = 1 - 0.92 = 0.08\) or \(8\%\)</p>
<p><strong>Explanation:</strong> Delayed is the complement of on-time. Calculate using 1 − P(on time).</p>
</div>

<div class="worked-example">
<h4>Problem 4: Interpreting Probability</h4>
<p><strong>Question:</strong> A weather report says there's a 25% chance of snow. Would you be surprised if it snowed? Why or why not?</p>
<p><strong>Answer:</strong> It would be somewhat surprising but not impossible. 25% means it's unlikely but possible. It's more likely NOT to snow (75%), but there's still a 1 in 4 chance of snow.</p>
</div>"""
    }
]
