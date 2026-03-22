"""
Fractions (Equivalent, Unlike Denominators) - Lesson Content

Topics covered:
- What fractions represent
- Equivalent fractions
- Comparing fractions
- Simplifying fractions
- Adding/subtracting fractions with unlike denominators using LCM
"""

SECTIONS = [
    {
        "title": "Understanding Fractions",
        "body": """
        <h3>What is a Fraction?</h3>
        <p>A fraction represents <strong>a part of a whole</strong>. It tells us how many equal pieces we have out of the total.</p>

        <div class='example-box'>
            <p>A pizza is cut into 8 equal slices. You eat 3 slices.</p>
            <p>We write this as: <strong>3/8</strong> (read as "three-eighths")</p>
            <ul>
                <li>The <strong>numerator (3)</strong> is how many pieces you have</li>
                <li>The <strong>denominator (8)</strong> is how many equal pieces the whole is divided into</li>
            </ul>
        </div>

        <h3>Key Insight: The Denominator Tells the Size of Each Piece</h3>
        <p>A larger denominator means smaller pieces. Compare these:</p>
        <div class='example-box'>
            <p>1/2 (one-half, big piece)<br>
            1/4 (one-quarter, smaller piece)<br>
            1/8 (one-eighth, even smaller piece)</p>
            <p>Even though the numerator is 1 in all cases, the pieces get smaller as the denominator gets larger.</p>
        </div>

        <h3>Types of Fractions</h3>
        <div class='example-box'>
            <p><strong>Proper fraction:</strong> numerator &lt; denominator. Example: 3/5 (less than 1)</p>
            <p><strong>Improper fraction:</strong> numerator ≥ denominator. Example: 7/5 (equal to or more than 1)</p>
            <p><strong>Mixed number:</strong> whole number + fraction. Example: 1 2/5 (same as 7/5, but shown differently)</p>
        </div>
        """
    },
    {
        "title": "Equivalent Fractions",
        "body": """
        <h3>What Are Equivalent Fractions?</h3>
        <p>Equivalent fractions are <strong>different fractions that represent the same amount</strong>.</p>

        <div class='example-box'>
            <p>Picture: A chocolate bar divided into 2 pieces. You eat 1 piece = 1/2</p>
            <p>Picture: The same chocolate bar divided into 4 pieces. You eat 2 pieces = 2/4</p>
            <p><strong>1/2 = 2/4</strong> — You ate the same amount, just in different-sized pieces!</p>
        </div>

        <h3>How to Create Equivalent Fractions</h3>
        <p>Multiply both the numerator AND denominator by the same number:</p>
        <div class='example-box'>
            <p><strong>Start with:</strong> 1/2<br>
            <strong>Multiply top and bottom by 2:</strong> (1 × 2)/(2 × 2) = 2/4<br>
            <strong>Multiply top and bottom by 3:</strong> (1 × 3)/(2 × 3) = 3/6<br>
            <strong>Multiply top and bottom by 5:</strong> (1 × 5)/(2 × 5) = 5/10</p>
            <p>All of these are equivalent: 1/2 = 2/4 = 3/6 = 5/10</p>
        </div>

        <h3>Why This Works</h3>
        <p>You're not changing the fraction's value—you're just dividing the pieces differently. If you divide each piece into 2 parts, you need twice as many parts to have the same amount!</p>

        <h3>Simplifying Fractions (Reducing)</h3>
        <p>Sometimes we want to express a fraction using the smallest numbers possible. We do this by dividing both numerator and denominator by the same number.</p>
        <div class='example-box'>
            <p><strong>Simplify:</strong> 6/8<br>
            <strong>Both are divisible by 2:</strong> (6 ÷ 2)/(8 ÷ 2) = 3/4<br>
            <strong>3/4 is the simplified form</strong> — we can't simplify further</p>
        </div>
        """
    },
    {
        "title": "Comparing Fractions with Unlike Denominators",
        "body": """
        <h3>The Challenge</h3>
        <p>When fractions have different denominators, comparing them isn't as obvious as comparing numerators.</p>

        <div class='example-box'>
            <p>Which is bigger: 2/3 or 3/4?<br>
            You can't just compare 2 and 3 because the denominators are different!</p>
        </div>

        <h3>Strategy 1: Convert to Equivalent Fractions</h3>
        <p>Convert both fractions to have the same denominator, then compare:</p>
        <div class='example-box'>
            <p>Compare: 2/3 and 3/4</p>
            <p><strong>Find a common denominator:</strong> The denominators are 3 and 4. We can use 12 (3×4).</p>
            <p>2/3 = (2×4)/(3×4) = 8/12<br>
            3/4 = (3×3)/(4×3) = 9/12</p>
            <p>Now we compare: 8/12 vs 9/12<br>
            <strong>3/4 is bigger because 9/12 > 8/12</strong></p>
        </div>

        <h3>Strategy 2: Use a Number Line</h3>
        <p>Mark both fractions on a number line and see which is further to the right.</p>
        <div class='example-box'>
            <p>0 -------- 1/4 ------- 1/2 ------- 3/4 ------- 1</p>
            <p>0 ----------- 1/3 ----------- 2/3 ----------- 1</p>
            <p>Seeing them visually makes the comparison clearer!</p>
        </div>
        """
    },
    {
        "title": "Adding and Subtracting Fractions with Unlike Denominators",
        "body": """
        <h3>The Challenge</h3>
        <p>You can't add 1/3 + 1/4 directly because you'd be adding thirds and quarters—different-sized pieces!</p>

        <h3>The Solution: Find a Common Denominator</h3>
        <p>Convert both fractions to have the same denominator, then add or subtract:</p>
        <div class='example-box'>
            <p><strong>Problem:</strong> 1/3 + 1/4<br>
            <strong>Step 1: Find common denominator</strong> — Use 12 (a common multiple of 3 and 4)<br>
            <strong>Step 2: Convert:</strong> 1/3 = 4/12 and 1/4 = 3/12<br>
            <strong>Step 3: Add:</strong> 4/12 + 3/12 = 7/12<br>
            <strong>Answer: 7/12</strong></p>
        </div>

        <h3>Using LCM (Least Common Multiple)</h3>
        <p>The smallest common denominator is the LCM (Least Common Multiple) of the denominators.</p>
        <div class='example-box'>
            <p><strong>Find the LCM of 4 and 6:</strong><br>
            Multiples of 4: 4, 8, 12, 16, 20...<br>
            Multiples of 6: 6, 12, 18, 24...<br>
            <strong>LCM = 12</strong> (smallest number in both lists)</p>
        </div>

        <h3>Step-by-Step Example: 2/3 - 1/4</h3>
        <div class='example-box'>
            <p><strong>Step 1: Find LCM of 3 and 4</strong><br>
            Multiples of 3: 3, 6, 9, 12...<br>
            Multiples of 4: 4, 8, 12...<br>
            LCM = 12</p>
            <p><strong>Step 2: Convert to equivalent fractions with denominator 12</strong><br>
            2/3 = (2×4)/(3×4) = 8/12<br>
            1/4 = (1×3)/(4×3) = 3/12</p>
            <p><strong>Step 3: Subtract</strong><br>
            8/12 - 3/12 = 5/12</p>
            <p><strong>Answer: 5/12</strong></p>
        </div>

        <h3>Always Simplify Your Answer</h3>
        <p>After adding or subtracting, check if your answer can be simplified:</p>
        <div class='example-box'>
            <p>If your answer is 6/8, simplify to 3/4<br>
            If your answer is 4/12, simplify to 1/3</p>
        </div>
        """
    },
    {
        "title": "Real-World Fraction Problems",
        "body": """
        <h3>Fractions in Cooking</h3>
        <div class='example-box'>
            <p>A recipe calls for 1/2 cup flour and 1/3 cup sugar. How much total flour and sugar?<br>
            1/2 + 1/3 = 3/6 + 2/6 = 5/6 cup</p>
        </div>

        <h3>Fractions in Sharing</h3>
        <div class='example-box'>
            <p>You have 3/4 of a cake. Your friend eats 1/6 of the original cake. How much is left?<br>
            3/4 - 1/6 = 9/12 - 2/12 = 7/12 of the cake</p>
        </div>

        <h3>Fractions in Measurement</h3>
        <div class='example-box'>
            <p>A board is 3/4 meter long. Another board is 2/3 meter long. How long are they together?<br>
            3/4 + 2/3 = 9/12 + 8/12 = 17/12 = 1 5/12 meters</p>
        </div>

        <h3>Why Understanding Fractions Matters</h3>
        <ul>
            <li>Cooking and baking (measuring ingredients)</li>
            <li>Construction (measurements like 3/8 inch)</li>
            <li>Time (1/4 hour = 15 minutes)</li>
            <li>Money (1/2 dollar = 50 cents)</li>
            <li>Science (percentages are fractions out of 100)</li>
        </ul>
        """
    }
]
