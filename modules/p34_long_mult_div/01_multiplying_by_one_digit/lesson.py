TITLE = "Multiplying by One Digit"
SECTIONS = [
    {
        "title": "Why We Need Multiplication Strategies",
        "body": """
        <h3>Times Tables Are Not Enough</h3>
        <p>You know that \\(3 \\times 4 = 12\\) from times tables. But what about \\(23 \\times 4\\)? We can't memorize every multiplication fact.</p>

        <div class='concept-box'>
            <p><strong>Big Idea:</strong> We can break larger numbers apart using place value and multiply each part separately. Then add the results together.</p>
        </div>

        <h3>The Key Idea: Breaking Numbers Apart</h3>
        <p>When we multiply 23 × 4, we're really doing this:</p>
        <div class='worked-example'>
            <p>\\(23 = 20 + 3\\)</p>
            <p>So \\(23 \\times 4 = (20 + 3) \\times 4\\)</p>
            <p style='font-weight: bold;'>\\(= (20 \\times 4) + (3 \\times 4)\\)</p>
            <p>\\(= 80 + 12\\)</p>
            <p>= <strong>92</strong></p>
        </div>

        <p><strong>This is the distributive property:</strong> We "distribute" the 4 across both parts of 23.</p>
        """
    },
    {
        "title": "The Column Method for One-Digit Multiplication",
        "body": """
        <h3>Let's Solve: 23 × 4</h3>

        <p><strong>Step 1: Set up vertically</strong></p>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.2em;'>
              &nbsp;&nbsp;23<br>
              ×&nbsp;&nbsp;4<br>
              ----
            </p>
        </div>

        <p><strong>Step 2: Multiply the ones digit (\\(3 \\times 4\\))</strong></p>
        <div class='worked-example'>
            <p>\\(3 \\times 4 = 12\\)</p>
            <p>Write down the 2, and carry the 1 (ten).</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.2em;'>
              <sup>1</sup>23<br>
              ×&nbsp;&nbsp;&nbsp;4<br>
              ----<br>
              &nbsp;&nbsp;&nbsp;2 &nbsp;&nbsp;(with 1 carried)
            </p>
        </div>

        <p><strong>Step 3: Multiply the tens digit (\\(2 \\times 4\\)) and add the carried 1</strong></p>
        <div class='worked-example'>
            <p>\\(2 \\times 4 = 8\\), plus the carried 1 = 9</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.2em;'>
              <sup>1</sup>23<br>
              ×&nbsp;&nbsp;&nbsp;4<br>
              ----<br>
              &nbsp;&nbsp;92
            </p>
        </div>

        <p style='font-weight: bold;'>So \\(23 \\times 4 = 92\\)</p>
        """
    },
    {
        "title": "More Examples: Practice the Method",
        "body": """
        <h3>Example 1: 34 × 7</h3>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>2</sup>34<br>
              ×&nbsp;&nbsp;&nbsp;7<br>
              ----<br>
              &nbsp;238
            </p>
            <p>Step 1: \\(7 \\times 4 = 28\\). Write 8, carry 2.</p>
            <p>Step 2: \\(7 \\times 3 = 21\\), plus carried 2 = 23. Write 23.</p>
            <p><strong>Answer: 238</strong></p>
        </div>

        <h3>Example 2: 45 × 6</h3>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>3</sup>45<br>
              ×&nbsp;&nbsp;&nbsp;6<br>
              ----<br>
              &nbsp;270
            </p>
            <p>Step 1: \\(6 \\times 5 = 30\\). Write 0, carry 3.</p>
            <p>Step 2: \\(6 \\times 4 = 24\\), plus carried 3 = 27. Write 27.</p>
            <p><strong>Answer: 270</strong></p>
        </div>

        <h3>What If There's a Bigger Number? (3 digits)</h3>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>1</sup>&nbsp;<sup>2</sup>124<br>
              ×&nbsp;&nbsp;&nbsp;&nbsp;5<br>
              ----<br>
              &nbsp;&nbsp;620
            </p>
            <p>Step 1: \\(5 \\times 4 = 20\\). Write 0, carry 2.</p>
            <p>Step 2: \\(5 \\times 2 = 10\\), plus carried 2 = 12. Write 2, carry 1.</p>
            <p>Step 3: \\(5 \\times 1 = 5\\), plus carried 1 = 6. Write 6.</p>
            <p><strong>Answer: 620</strong></p>
        </div>
        """
    },
    {
        "title": "Common Mistakes & How to Avoid Them",
        "body": """
        <h3>Mistake 1: Forgetting to Carry</h3>
        <div class='warning-box'>
            <p><strong>Wrong:</strong> \\(24 \\times 7 = 148\\) ✗</p>
            <p><strong>Right:</strong> \\(24 \\times 7 = 168\\) ✓</p>
            <p>When \\(7 \\times 4 = 28\\), you MUST carry the 2 to the next column.</p>
        </div>

        <h3>Mistake 2: Writing Too Many Digits</h3>
        <div class='warning-box'>
            <p><strong>Common error:</strong> Writing 28 instead of 8 (with carry 2)</p>
            <p>Remember: Only write the ONES digit in that position. Carry the tens to the next column.</p>
        </div>

        <h3>Mistake 3: Forgetting to Include the Carried Digit</h3>
        <div class='warning-box'>
            <p><strong>Wrong:</strong> \\(23 \\times 4\\) → \\(3 \\times 4 = 12\\), \\(2 \\times 4 = 8\\), answer is 812 ✗</p>
            <p><strong>Right:</strong> \\(23 \\times 4\\) → \\(3 \\times 4 = 12\\) (write 2, carry 1), \\(2 \\times 4 = 8\\) plus 1 = 9, answer is 92 ✓</p>
        </div>

        <h3>Checking Your Answer</h3>
        <div class='success-box'>
            <p>Use <strong>estimation:</strong> \\(23 \\times 4\\) is roughly \\(20 \\times 4 = 80\\), so 92 seems reasonable.</p>
            <p>Or use <strong>inverse:</strong> \\(92 \\div 4\\) should equal 23.</p>
        </div>
        """
    }
]
