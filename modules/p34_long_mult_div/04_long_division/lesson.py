TITLE = "Long Division: Dividing by Two Digits"
SECTIONS = [
    {
        "title": "From One Digit to Two Digits: What Changes?",
        "body": """
        <h3>The Same Steps, Applied to Larger Divisors</h3>
        <p>Long division by a two-digit divisor uses the same strategy as dividing by one digit, but we need to be more careful about estimation and placing digits.</p>

        <div class='concept-box'>
            <p><strong>Key steps remain the same:</strong></p>
            <ol>
                <li>Look at enough digits so the divisor fits in</li>
                <li>Divide and write the quotient digit</li>
                <li>Multiply the quotient digit by the divisor</li>
                <li>Subtract to find the remainder</li>
                <li>Bring down the next digit</li>
                <li>Repeat until all digits are used</li>
            </ol>
        </div>

        <h3>Why Two-Digit Division is Harder</h3>
        <p>It's harder to guess how many times the divisor goes into a number. For example:</p>
        <ul>
            <li>How many times does 12 go into 45? You might guess 3, 4, or 5. You have to test it!</li>
            <li>With single digits, it's easier: does 4 go into 9? You know roughly how many times.</li>
        </ul>

        <p><strong>Strategy:</strong> Make an educated guess, multiply to check, and adjust if needed.</p>
        """
    },
    {
        "title": "Step-by-Step: 456 ÷ 12",
        "body": """
        <h3>Worked Example: 456 ÷ 12</h3>

        <p><strong>Step 1: Set up the problem</strong></p>
        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;<br>
              12 ) 456
            </p>
        </div>

        <p><strong>Step 2: Does 12 fit into 4? No. Into 45? Yes!</strong></p>
        <div class='worked-example'>
            <p>We look at the first two digits: 45. Now, how many times does 12 go into 45?</p>
            <p>12 × 3 = 36 ✓ (fits)</p>
            <p>12 × 4 = 48 ✗ (too big)</p>
            <p>So 12 goes into 45 three times. Write 3 above the 5.</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
              12 ) 456
            </p>
        </div>

        <p><strong>Step 3: Multiply 3 × 12 and subtract</strong></p>
        <div class='worked-example'>
            <p>3 × 12 = 36. Subtract: 45 - 36 = 9.</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
              12 ) 456<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-36<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9
            </p>
        </div>

        <p><strong>Step 4: Bring down the next digit (6)</strong></p>
        <div class='worked-example'>
            <p>The 9 remainder becomes 96 when we bring down the 6.</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
              12 ) 456<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-36<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;96
            </p>
        </div>

        <p><strong>Step 5: Divide again: How many times does 12 go into 96?</strong></p>
        <div class='worked-example'>
            <p>12 × 8 = 96 ✓ (exactly!)</p>
            <p>Write 8 above the 6.</p>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38<br>
              12 ) 456<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-36<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;96<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-96<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0
            </p>
        </div>

        <p style='font-weight: bold;'>456 ÷ 12 = 38</p>
        <p><em>Check: 38 × 12 = 456 ✓</em></p>
        """
    },
    {
        "title": "With Remainders: 457 ÷ 12 and 345 ÷ 15",
        "body": """
        <h3>Example 1: When There's a Remainder (457 ÷ 12)</h3>

        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38 R1<br>
              12 ) 457<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-36<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;97<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-96<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1
            </p>
            <p><strong>457 ÷ 12 = 38 R1</strong></p>
            <p><em>Check: (38 × 12) + 1 = 456 + 1 = 457 ✓</em></p>
        </div>

        <h3>Example 2: 345 ÷ 15</h3>

        <div class='worked-example'>
            <p style='text-align: center; font-family: monospace; font-size: 1.1em;'>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23<br>
              15 ) 345<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-30<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45<br>
              &nbsp;&nbsp;&nbsp;&nbsp;-45<br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0
            </p>
            <p>Step 1: Does 15 fit into 3? No. Into 34? Yes! 15 × 2 = 30. Write 2.</p>
            <p>Step 2: 34 - 30 = 4. Bring down 5 to make 45.</p>
            <p>Step 3: 15 × 3 = 45. Write 3. No remainder.</p>
            <p><strong>345 ÷ 15 = 23</strong></p>
        </div>
        """
    },
    {
        "title": "Tips for Solving Two-Digit Division",
        "body": """
        <h3>Making Good Guesses</h3>
        <div class='worked-example'>
            <p><strong>Estimation Tip:</strong> To guess how many times 12 goes into 96:</p>
            <p>Round 12 to 10, then 96 ÷ 10 ≈ 10. So try 8, 9, or 10.</p>
            <p>Test: 12 × 8 = 96. That works!</p>
        </div>

        <h3>What If Your Guess is Wrong?</h3>
        <div class='worked-example'>
            <p><strong>Example:</strong> How many times does 12 go into 45?</p>
            <p>Guess 5: 12 × 5 = 60 (too big)</p>
            <p>Try 4: 12 × 4 = 48 (too big)</p>
            <p>Try 3: 12 × 3 = 36 (just right!)</p>
        </div>

        <h3>Common Mistakes</h3>
        <div class='warning-box'>
            <p><strong>Mistake 1:</strong> Forgetting to bring down a digit. This causes the problem to become unsolvable.</p>
            <p><strong>Mistake 2:</strong> Placing the quotient digit in the wrong position. Be careful about alignment!</p>
            <p><strong>Mistake 3:</strong> Multiplying or subtracting incorrectly. Double-check your arithmetic!</p>
        </div>

        <h3>Always Verify</h3>
        <div class='success-box'>
            <p><strong>Formula:</strong> (quotient × divisor) + remainder = dividend</p>
            <p>Before you finish, plug your answer back in to check!</p>
        </div>
        """
    }
]
