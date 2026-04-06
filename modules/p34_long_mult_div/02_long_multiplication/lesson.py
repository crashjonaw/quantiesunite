TITLE = "Long Multiplication: Two-Digit by Two-Digit"
SECTIONS = [
    {
        "title": "Understanding the Distributive Property",
        "body": """
        <h3>Breaking Down the Problem Using Place Value</h3>
        <p>You now know how to multiply a multi-digit number by a single digit. But what about \\(23 \\times 47\\)? We can't do that mentally.</p>

        <p><strong>The trick:</strong> Treat the second number (47) as 40 + 7, and multiply by each part separately.</p>

        <div class='worked-example'>
            <p>\\(23 \\times 47 = 23 \\times (40 + 7)\\)</p>
            <p style='font-weight: bold;'>\\(= (23 \\times 40) + (23 \\times 7)\\)</p>
            <p>\\(= 920 + 161\\)</p>
            <p>= <strong>1,081</strong></p>
        </div>

        <h3>Why This Works: The Area Model</h3>
        <p>Imagine a rectangle that is 23 units wide and 47 units tall. We can split it into two smaller rectangles:</p>
        <ul>
            <li>One rectangle: \\(23 \\times 40 = 920\\)</li>
            <li>Another rectangle: \\(23 \\times 7 = 161\\)</li>
        </ul>
        <p>Total area = \\(920 + 161 = 1{,}081\\)</p>

        <div class='concept-box'>
            <p><strong>Long multiplication with two digits</strong> means we multiply by each digit separately, then add the partial products.</p>
        </div>
        """
    },
    {
        "title": "Step-by-Step: 34 × 27",
        "body": """
        <h3>Worked Example: 34 × 27</h3>

        <p><strong>Step 1: Set up the problem vertically</strong></p>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;34<br>
              ×&nbsp;&nbsp;27<br>
              ----
            </p>
        </div>

        <p><strong>Step 2: Multiply by the ones digit (7)</strong><br>
        This is 34 × 7, which you already know how to do!</p>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>2</sup>34<br>
              ×&nbsp;&nbsp;27<br>
              ----<br>
              &nbsp;238 &nbsp;&nbsp;← (34 × 7 = 238)
            </p>
        </div>

        <p><strong>Step 3: Multiply by the tens digit (2), but SHIFT LEFT one place</strong><br>
        We're really multiplying 34 × 20 (not just 34 × 2).</p>
        <div class='worked-example'>
            <p>\\(34 \\times 2 = 68\\), but we write it in the tens place, so it becomes 680.</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>2</sup>34<br>
              ×&nbsp;&nbsp;27<br>
              ----<br>
              &nbsp;238<br>
              &nbsp;68&nbsp;&nbsp;&nbsp;&nbsp;← shifted left (this is really 68 × 10 = 680)
            </p>
        </div>

        <p><strong>Step 4: Add the partial products</strong></p>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;34<br>
              ×&nbsp;&nbsp;27<br>
              ----<br>
              &nbsp;238<br>
              &nbsp;680<br>
              ----<br>
              &nbsp;918
            </p>
            <p><strong>34 × 27 = 918</strong></p>
        </div>
        """
    },
    {
        "title": "More Examples: 56 × 43 and 47 × 23",
        "body": """
        <h3>Example 1: 56 × 43</h3>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>2</sup>56<br>
              ×&nbsp;&nbsp;43<br>
              ----<br>
              &nbsp;168 &nbsp;&nbsp;← (56 × 3)<br>
              2240 &nbsp;&nbsp;← (56 × 4, shifted left to 56 × 40)<br>
              ----<br>
              2408
            </p>
            <p><strong>56 × 43 = 2,408</strong></p>
        </div>

        <h3>Example 2: 47 × 23</h3>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>2</sup>47<br>
              ×&nbsp;&nbsp;23<br>
              ----<br>
              &nbsp;141 &nbsp;&nbsp;← (47 × 3)<br>
              &nbsp;940 &nbsp;&nbsp;← (47 × 20)<br>
              ----<br>
              1081
            </p>
            <p><strong>47 × 23 = 1,081</strong></p>
        </div>

        <h3>When the Tens Digit is Larger</h3>
        <div class='worked-example'>
            <p><strong>Example: 25 × 87</strong></p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              <sup>3</sup>25<br>
              ×&nbsp;&nbsp;87<br>
              ----<br>
              &nbsp;175 &nbsp;&nbsp;← (25 × 7)<br>
              2000 &nbsp;&nbsp;← (25 × 8, shifted: really 25 × 80 = 2000)<br>
              ----<br>
              2175
            </p>
            <p><strong>25 × 87 = 2,175</strong></p>
        </div>
        """
    },
    {
        "title": "Avoiding Common Mistakes in Long Multiplication",
        "body": """
        <h3>Mistake 1: Forgetting to Shift</h3>
        <div class='warning-box'>
            <p><strong>Wrong:</strong> \\(34 \\times 27\\) → first partial: 238, second partial: 68, answer: \\(238 + 68 = 306\\) ✗</p>
            <p><strong>Right:</strong> \\(34 \\times 27\\) → first partial: 238, second partial: 680 (shifted), answer: \\(238 + 680 = 918\\) ✓</p>
            <p><strong>Why?</strong> When you multiply by the tens digit, you're multiplying by 20, 30, etc., not 2, 3, etc. The shift accounts for this.</p>
        </div>

        <h3>Mistake 2: Forgetting to Carry in Partial Products</h3>
        <div class='warning-box'>
            <p><strong>Wrong:</strong> \\(34 \\times 7 = 21\\) and 28, written as 2128 ✗</p>
            <p><strong>Right:</strong> \\(34 \\times 7\\) → \\(7 \\times 4 = 28\\) (write 8, carry 2), \\(7 \\times 3 = 21\\), plus 2 = 23, answer: 238 ✓</p>
        </div>

        <h3>Mistake 3: Misaligning Partial Products</h3>
        <div class='warning-box'>
            <p>Always line up the partial products correctly before adding. The second partial product should start one space to the left.</p>
        </div>

        <h3>Checking Your Work</h3>
        <div class='success-box'>
            <p><strong>Method 1 - Estimation:</strong> \\(34 \\times 27\\) is roughly \\(30 \\times 30 = 900\\), so 918 seems reasonable.</p>
            <p><strong>Method 2 - Commutative Property:</strong> Try \\(27 \\times 34\\) and see if you get the same answer.</p>
            <p><strong>Method 3 - Reverse:</strong> Divide your answer by one of the numbers: \\(918 \\div 34\\) should equal 27.</p>
        </div>
        """
    }
]
