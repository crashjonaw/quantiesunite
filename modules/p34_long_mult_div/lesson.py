"""
Long Multiplication & Division - Lesson Content

Topics covered:
- Standard algorithm for long multiplication
- Breaking numbers into parts
- Long division step by step
- Checking your work
"""

SECTIONS = [
    {
        "title": "Understanding Long Multiplication",
        "body": """
        <h3>Why Do We Need Long Multiplication?</h3>
        <p>We can multiply small numbers in our heads, but what about 23 × 45? That's too big to calculate quickly. Long multiplication breaks the problem into smaller, easier parts.</p>

        <h3>The Key Idea: Breaking Numbers Apart</h3>
        <p>When we multiply 23 × 45, we're really doing this:</p>
        <div class='example-box'>
            <p>23 = 20 + 3<br>
            45 = 40 + 5</p>
            <p>So 23 × 45 = (20 + 3) × (40 + 5)</p>
            <p>= (20 × 40) + (20 × 5) + (3 × 40) + (3 × 5)<br>
            = 800 + 100 + 120 + 15<br>
            = <strong>1,035</strong></p>
        </div>

        <h3>The Long Multiplication Algorithm</h3>
        <p>The algorithm (step-by-step process) arranges this nicely so we don't have to think about all the parts at once:</p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;23<br>
            ×&nbsp;&nbsp;45<br>
            ------<br>
            &nbsp;&nbsp;115&nbsp;&nbsp;(this is 23 × 5)<br>
            &nbsp;920&nbsp;&nbsp;&nbsp;(this is 23 × 40)<br>
            ------<br>
            1,035<br>
            </p>
        </div>

        <h3>Why This Works</h3>
        <p>We multiply the top number by each digit of the bottom number (from right to left), then add all the results together. The position of each partial product matters—we shift left each time because we're multiplying by larger place values.</p>
        """
    },
    {
        "title": "Step-by-Step Long Multiplication",
        "body": """
        <h3>Let's Solve: 34 × 27</h3>
        <p><strong>Step 1: Set up the problem</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;34<br>
            ×&nbsp;&nbsp;27<br>
            ------<br>
            </p>
        </div>

        <p><strong>Step 2: Multiply by the ones digit (7)</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;34<br>
            ×&nbsp;&nbsp;27<br>
            ------<br>
            &nbsp;&nbsp;238&nbsp;&nbsp;(34 × 7 = 238)<br>
            </p>
            <p>How? 7 × 4 = 28, write 8, carry 2. Then 7 × 3 = 21, plus the 2 = 23.</p>
        </div>

        <p><strong>Step 3: Multiply by the tens digit (2), and shift left one place</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;34<br>
            ×&nbsp;&nbsp;27<br>
            ------<br>
            &nbsp;&nbsp;238&nbsp;&nbsp;(34 × 7)<br>
            &nbsp;680&nbsp;&nbsp;&nbsp;(34 × 2 = 68, shifted left one place)<br>
            </p>
            <p>The 2 represents 20, so we multiply 34 × 20 = 680.</p>
        </div>

        <p><strong>Step 4: Add the partial products</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;34<br>
            ×&nbsp;&nbsp;27<br>
            ------<br>
            &nbsp;&nbsp;238<br>
            &nbsp;680<br>
            ------<br>
            &nbsp;918<br>
            </p>
            <p><strong>34 × 27 = 918</strong></p>
        </div>

        <h3>Another Example: 56 × 43</h3>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;56<br>
            ×&nbsp;&nbsp;43<br>
            ------<br>
            &nbsp;&nbsp;168&nbsp;&nbsp;(56 × 3)<br>
            2240&nbsp;&nbsp;&nbsp;(56 × 4, shifted left)<br>
            ------<br>
            2,408<br>
            </p>
        </div>

        <h3>Common Mistakes to Avoid</h3>
        <ul>
            <li><strong>Forgetting to shift:</strong> Make sure you shift left when multiplying by the tens digit</li>
            <li><strong>Forgetting to carry:</strong> When a multiplication result is 10 or more, carry the tens place</li>
            <li><strong>Misalignment in addition:</strong> Line up partial products correctly before adding</li>
        </ul>
        """
    },
    {
        "title": "Understanding Long Division",
        "body": """
        <h3>What is Division?</h3>
        <p>Division is sharing or grouping. If we have 24 cookies and 4 children, how many does each get? That's 24 ÷ 4 = 6.</p>

        <h3>Long Division: Breaking Down a Big Problem</h3>
        <p>Long division is used when we can't divide in our heads. For example, 456 ÷ 12 is too hard to do mentally, so we use the algorithm.</p>

        <h3>The Key Idea Behind Long Division</h3>
        <p>We divide from left to right, digit by digit. We look at how many times the divisor "fits into" each part of the dividend.</p>

        <div class='example-box'>
            <p><strong>Division vocabulary:</strong></p>
            <p>In the problem 456 ÷ 12 = 38:</p>
            <ul>
                <li><strong>456</strong> is the <strong>dividend</strong> (what we're dividing)</li>
                <li><strong>12</strong> is the <strong>divisor</strong> (what we're dividing by)</li>
                <li><strong>38</strong> is the <strong>quotient</strong> (the answer)</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Step-by-Step Long Division",
        "body": """
        <h3>Let's Solve: 456 ÷ 12</h3>

        <p><strong>Step 1: Set up the problem</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
             12 ) 456<br>
            </p>
        </div>

        <p><strong>Step 2: Look at the leftmost digits until you have a number ≥ divisor</strong></p>
        <div class='example-box'>
            <p>Is 4 ≥ 12? No.<br>
            Is 45 ≥ 12? Yes!</p>
        </div>

        <p><strong>Step 3: Divide and write the quotient above</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
            &nbsp;12 ) 456<br>
            </p>
            <p>12 goes into 45 how many times? 12 × 3 = 36, and 12 × 4 = 48 (too much). So 3 times.</p>
        </div>

        <p><strong>Step 4: Multiply and subtract</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
            &nbsp;12 ) 456<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-36<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9<br>
            </p>
            <p>12 × 3 = 36. Subtract 36 from 45 to get 9.</p>
        </div>

        <p><strong>Step 5: Bring down the next digit</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br>
            &nbsp;12 ) 456<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-36<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;96<br>
            </p>
            <p>Bring down the 6 to make 96.</p>
        </div>

        <p><strong>Step 6: Repeat: Divide, multiply, subtract</strong></p>
        <div class='example-box'>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38<br>
            &nbsp;12 ) 456<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-36<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;96<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-96<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>
            </p>
            <p>12 goes into 96 exactly 8 times (12 × 8 = 96).<br>
            <strong>So 456 ÷ 12 = 38</strong></p>
        </div>

        <h3>When There's a Remainder</h3>
        <p>Not all divisions divide evenly. Sometimes there's a remainder.</p>
        <div class='example-box'>
            <p><strong>Example: 457 ÷ 12</strong></p>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;38 R1<br>
            &nbsp;12 ) 457<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-36<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;97<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-96<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>
            </p>
            <p><strong>457 ÷ 12 = 38 R1</strong> (38 remainder 1)</p>
            <p>This means 12 × 38 = 456, and 457 - 456 = 1 is left over.</p>
        </div>

        <h3>Checking Division with Multiplication</h3>
        <p>To check: (quotient × divisor) + remainder = dividend</p>
        <div class='example-box'>
            <p>Check: 457 ÷ 12 = 38 R1<br>
            (38 × 12) + 1 = 456 + 1 = 457 ✓</p>
        </div>
        """
    },
    {
        "title": "Strategies for Successful Multiplication & Division",
        "body": """
        <h3>For Multiplication: Check Your Work</h3>
        <p>Always verify your answer using one of these methods:</p>
        <ul>
            <li><strong>Use commutative property:</strong> If you calculated 23 × 45, try 45 × 23 to see if you get the same answer</li>
            <li><strong>Estimate first:</strong> 23 × 45 is about 20 × 50 = 1,000, so your answer should be close to that</li>
            <li><strong>Use a different method:</strong> Solve it a different way and see if you get the same result</li>
        </ul>

        <h3>For Division: Use Multiplication to Check</h3>
        <p>Always verify: (quotient × divisor) + remainder = dividend</p>

        <h3>Common Mistakes</h3>
        <div class='example-box'>
            <p><strong>In multiplication:</strong> Forgetting to shift, not carrying correctly</p>
            <p><strong>In division:</strong> Not bringing down digits, forgetting remainders, misplacing quotient digits</p>
        </div>

        <h3>Real-World Applications</h3>
        <ul>
            <li><strong>Multiplication:</strong> Calculating cost (12 items at 23 dollars each)</li>
            <li><strong>Division:</strong> Sharing fairly (345 cookies shared among 15 children)</li>
            <li><strong>Both:</strong> Building and construction, cooking recipes, money management</li>
        </ul>
        """
    }
]
