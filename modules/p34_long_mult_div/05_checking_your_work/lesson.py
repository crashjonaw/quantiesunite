TITLE = "Checking Your Work: Verification Strategies"
SECTIONS = [
    {
        "title": "Why Checking Matters",
        "body": """
        <h3>Mistakes Happen to Everyone</h3>
        <p>Even when you follow all the steps correctly, it's easy to make small arithmetic errors: forgetting to carry, misaligning digits, or miscalculating. That's why checking is crucial.</p>

        <div class='concept-box'>
            <p><strong>Good mathematicians always check their work.</strong> Checking helps you catch errors before you submit your answer.</p>
        </div>

        <h3>Methods for Checking</h3>
        <p>There are several ways to verify your multiplication and division answers. Different methods work for different situations.</p>
        """
    },
    {
        "title": "Checking Multiplication: Three Methods",
        "body": """
        <h3>Method 1: Use the Inverse (Division)</h3>
        <p>Multiplication and division are inverses. If \\(23 \\times 47 = 1,081\\), then \\(1,081 \\div 23\\) should equal 47.</p>

        <div class='worked-example'>
            <p><strong>Example:</strong> Check 34 × 27 = 918</p>
            <p>Divide: 918 ÷ 34 = 27 ✓</p>
            <p>If this is true, your multiplication is correct!</p>
        </div>

        <h3>Method 2: Use the Commutative Property</h3>
        <p>Multiplication is commutative: \\(a \\times b = b \\times a\\). So 23 × 47 should equal 47 × 23.</p>

        <div class='worked-example'>
            <p><strong>Example:</strong> Check 34 × 27 = 918</p>
            <p>Calculate 27 × 34 and see if you also get 918.</p>
            <p>This method catches alignment or place-value errors!</p>
        </div>

        <h3>Method 3: Estimation (Rough Rounding)</h3>
        <p>Round both numbers to simpler values and multiply mentally. Your answer should be roughly close.</p>

        <div class='worked-example'>
            <p><strong>Example:</strong> Check 34 × 27 = 918</p>
            <p>Round: 34 ≈ 30, 27 ≈ 30</p>
            <p>Mental math: 30 × 30 = 900</p>
            <p>Your answer of 918 is close to 900, so it seems reasonable! ✓</p>
        </div>

        <h3>Method 4: Check Partial Products</h3>
        <p>For long multiplication, verify that each partial product is correct before adding them.</p>

        <div class='worked-example'>
            <p><strong>Example:</strong> 34 × 27</p>
            <p>First partial: 34 × 7 = 238. Check: 30 × 7 = 210, 4 × 7 = 28, total 238 ✓</p>
            <p>Second partial: 34 × 2 = 68 (really 34 × 20 = 680 when shifted). Check: 30 × 2 = 60, 4 × 2 = 8, total 68 ✓</p>
            <p>Then verify: 238 + 680 = 918 ✓</p>
        </div>
        """
    },
    {
        "title": "Checking Division: The Verification Formula",
        "body": """
        <h3>The Universal Division Check</h3>
        <p>For ANY division problem, use this formula:</p>

        <div class='concept-box' style='text-align: center; font-size: 1.1em;'>
            <p><strong>(quotient × divisor) + remainder = dividend</strong></p>
        </div>

        <h3>Example 1: Division with No Remainder</h3>
        <div class='worked-example'>
            <p><strong>Problem:</strong> 456 ÷ 12 = 38</p>
            <p><strong>Check:</strong> (38 × 12) + 0 = 456 ✓</p>
            <p>If this equation is true, your division is correct!</p>
        </div>

        <h3>Example 2: Division with a Remainder</h3>
        <div class='worked-example'>
            <p><strong>Problem:</strong> 457 ÷ 12 = 38 R1</p>
            <p><strong>Check:</strong> (38 × 12) + 1 = 456 + 1 = 457 ✓</p>
            <p>The remainder must be included in the check!</p>
        </div>

        <h3>Example 3: Dividing by One Digit</h3>
        <div class='worked-example'>
            <p><strong>Problem:</strong> 87 ÷ 4 = 21 R3</p>
            <p><strong>Check:</strong> (21 × 4) + 3 = 84 + 3 = 87 ✓</p>
        </div>

        <h3>What If the Check Fails?</h3>
        <p>If (quotient × divisor) + remainder ≠ dividend, then something went wrong. Go back and redo the long division carefully!</p>
        """
    },
    {
        "title": "Real-World Applications: Why Accuracy Matters",
        "body": """
        <h3>Shopping and Money</h3>
        <div class='worked-example'>
            <p><strong>Scenario:</strong> You buy 12 items at 23 dollars each. What's the total cost?</p>
            <p>Calculation: 12 × 23 = 276 dollars</p>
            <p><strong>Why check?</strong> If you miscalculate and charge the customer 276 cents instead of 276 dollars, they might underpay or overpay!</p>
            <p><strong>Check:</strong> 276 ÷ 23 = 12 ✓</p>
        </div>

        <h3>Sharing Fairly</h3>
        <div class='worked-example'>
            <p><strong>Scenario:</strong> You have 345 cookies and want to share them equally among 15 children. How many does each get?</p>
            <p>Calculation: 345 ÷ 15 = 23</p>
            <p><strong>Why check?</strong> To make sure every child gets exactly the right amount with no leftover.</p>
            <p><strong>Check:</strong> (23 × 15) = 345 ✓ (No remainder—everyone gets exactly 23!)</p>
        </div>

        <h3>Construction and Measurement</h3>
        <div class='worked-example'>
            <p><strong>Scenario:</strong> A carpenter needs to cut 18 wooden pieces, each 34 cm long. How much total wood does he need?</p>
            <p>Calculation: 18 × 34 = 612 cm</p>
            <p><strong>Why check?</strong> If he buys too little wood, the project fails. Too much is wasted money.</p>
            <p><strong>Check:</strong> 612 ÷ 34 = 18 ✓</p>
        </div>

        <h3>Key Takeaway</h3>
        <div class='success-box'>
            <p><strong>In real life, accuracy matters.</strong> Whether it's calculating bill totals, sharing resources fairly, or planning projects, checking your work ensures nobody gets shortchanged and nothing goes wrong!</p>
        </div>
        """
    }
]
