"""
Decimals (to 3 places) - Lesson Content

Topics covered:
- Understanding decimals
- Tenths, hundredths, thousandths
- Decimal-fraction conversion
- Comparing decimals
- Adding and subtracting decimals
"""

SECTIONS = [
    {
        "title": "Understanding Decimals",
        "body": """
        <h3>What is a Decimal?</h3>
        <p>A decimal is another way to write a fraction using a special notation with a decimal point. It's just a different way to represent parts of a whole.</p>

        <div class='example-box'>
            <p>1/10 = 0.1 (one-tenth)<br>
            3/10 = 0.3 (three-tenths)<br>
            7/10 = 0.7 (seven-tenths)</p>
            <p>The decimal point separates the whole number part from the fraction part.</p>
        </div>

        <h3>The Connection Between Decimals and Fractions</h3>
        <p>Decimals are just fractions written in a modern way:</p>
        <div class='example-box'>
            <p><strong>Fraction:</strong> 3/10 = <strong>Decimal:</strong> 0.3</p>
            <p><strong>Fraction:</strong> 25/100 = <strong>Decimal:</strong> 0.25</p>
            <p><strong>Fraction:</strong> 456/1000 = <strong>Decimal:</strong> 0.456</p>
        </div>

        <h3>Why Decimals Are Useful</h3>
        <ul>
            <li><strong>Money:</strong> $2.50 is easier than 2 50/100 dollars</li>
            <li><strong>Measurement:</strong> 2.5 metres is clearer than 2 5/10 metres</li>
            <li><strong>Science:</strong> Temperature, speed, percentages all use decimals</li>
            <li><strong>Easy arithmetic:</strong> Adding 2.5 + 3.7 is simpler than adding fractions</li>
        </ul>
        """
    },
    {
        "title": "Place Value in Decimals",
        "body": """
        <h3>Decimal Place Values</h3>
        <p>Just like whole numbers have place value, so do decimals. The position of each digit tells us its value.</p>

        <div class='example-box'>
            <p>In the number <strong>3.456</strong>:</p>
            <p><strong>3</strong> is in the <strong>ones</strong> place = 3<br>
            <strong>4</strong> is in the <strong>tenths</strong> place = 4/10 = 0.4<br>
            <strong>5</strong> is in the <strong>hundredths</strong> place = 5/100 = 0.05<br>
            <strong>6</strong> is in the <strong>thousandths</strong> place = 6/1000 = 0.006</p>
        </div>

        <h3>Understanding Each Place</h3>
        <p>Each place to the right of the decimal point is 10 times smaller than the one before:</p>
        <div class='example-box'>
            <p><strong>Tenths:</strong> 1/10 = 0.1 (divide the whole into 10 parts)<br>
            <strong>Hundredths:</strong> 1/100 = 0.01 (divide the whole into 100 parts)<br>
            <strong>Thousandths:</strong> 1/1000 = 0.001 (divide the whole into 1000 parts)</p>
        </div>

        <h3>Reading Decimals Correctly</h3>
        <div class='example-box'>
            <p><strong>0.5</strong> is read as "five tenths" or "zero point five"<br>
            <strong>0.25</strong> is read as "twenty-five hundredths" or "zero point two five"<br>
            <strong>0.456</strong> is read as "four hundred fifty-six thousandths" or "zero point four five six"<br>
            <strong>2.75</strong> is read as "two and seventy-five hundredths" or "two point seven five"</p>
        </div>
        """
    },
    {
        "title": "Converting Between Decimals and Fractions",
        "body": """
        <h3>From Decimal to Fraction</h3>
        <p>The number of decimal places tells us the denominator:</p>
        <div class='example-box'>
            <p><strong>0.3</strong> → 3/10 (one decimal place → denominator 10)<br>
            <strong>0.25</strong> → 25/100 (two decimal places → denominator 100)<br>
            <strong>0.456</strong> → 456/1000 (three decimal places → denominator 1000)</p>
        </div>

        <h3>From Fraction to Decimal</h3>
        <p>Divide the numerator by the denominator:</p>
        <div class='example-box'>
            <p><strong>1/4:</strong> 1 ÷ 4 = 0.25<br>
            <strong>3/5:</strong> 3 ÷ 5 = 0.6<br>
            <strong>7/8:</strong> 7 ÷ 8 = 0.875</p>
        </div>

        <h3>Common Decimal-Fraction Pairs to Memorize</h3>
        <div class='example-box'>
            <p>1/2 = 0.5<br>
            1/4 = 0.25<br>
            3/4 = 0.75<br>
            1/5 = 0.2<br>
            2/5 = 0.4<br>
            3/5 = 0.6<br>
            4/5 = 0.8<br>
            1/10 = 0.1</p>
        </div>
        """
    },
    {
        "title": "Comparing and Ordering Decimals",
        "body": """
        <h3>Comparing Decimals: Strategy</h3>
        <p>Compare decimals digit by digit from left to right, just like comparing whole numbers.</p>

        <div class='example-box'>
            <p><strong>Compare 0.5 and 0.3:</strong><br>
            Look at the tenths place: 5 > 3<br>
            So 0.5 > 0.3</p>
        </div>

        <h3>Comparing with Different Lengths</h3>
        <p>It's helpful to write decimals with the same number of decimal places:</p>
        <div class='example-box'>
            <p><strong>Compare 0.5 and 0.45:</strong><br>
            Write as: 0.50 and 0.45<br>
            Compare the tenths: 5 = 5 (same)<br>
            Compare the hundredths: 0 < 5<br>
            So 0.45 < 0.50 (or 0.45 < 0.5)</p>
        </div>

        <h3>Important: Don't Count Decimal Places!</h3>
        <p>A common mistake: thinking 0.1 < 0.09 because 1 < 09. This is wrong!</p>
        <div class='example-box'>
            <p>0.1 = 0.10 (one-tenth = ten-hundredths)<br>
            0.09 = 0.09 (nine-hundredths)<br>
            So 0.1 > 0.09 because 10/100 > 9/100</p>
        </div>

        <h3>Ordering Decimals</h3>
        <p>Use the same strategy as comparing—work left to right:</p>
        <div class='example-box'>
            <p><strong>Order from smallest to largest:</strong> 0.45, 0.54, 0.4, 0.5<br>
            Rewrite with same decimal places: 0.45, 0.54, 0.40, 0.50<br>
            Compare tenths: 0.40, 0.45, 0.50, 0.54<br>
            <strong>Answer: 0.4, 0.45, 0.5, 0.54</strong></p>
        </div>
        """
    },
    {
        "title": "Adding and Subtracting Decimals",
        "body": """
        <h3>The Key Principle: Line Up the Decimal Points!</h3>
        <p>This is the most important rule. When adding or subtracting decimals, the decimal points must be directly above each other.</p>

        <div class='example-box'>
            <p><strong>Example: 2.5 + 1.3</strong></p>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;2.5<br>
            + 1.3<br>
            -----<br>
            &nbsp;&nbsp;3.8<br>
            </p>
            <p>Tenths + tenths: 5 + 3 = 8 tenths = 8<br>
            Ones + ones: 2 + 1 = 3</p>
        </div>

        <h3>Adding Decimals with Different Lengths</h3>
        <p>Add zeros if needed to make the decimal places equal:</p>
        <div class='example-box'>
            <p><strong>Example: 3.2 + 1.45</strong></p>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;3.20<br>
            + 1.45<br>
            ------<br>
            &nbsp;&nbsp;4.65<br>
            </p>
            <p>Hundredths: 0 + 5 = 5<br>
            Tenths: 2 + 4 = 6<br>
            Ones: 3 + 1 = 4</p>
        </div>

        <h3>Subtracting Decimals</h3>
        <p>Same rule: line up decimal points and subtract column by column:</p>
        <div class='example-box'>
            <p><strong>Example: 5.74 - 2.31</strong></p>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;5.74<br>
            - 2.31<br>
            ------<br>
            &nbsp;&nbsp;3.43<br>
            </p>
        </div>

        <h3>Subtracting with Borrowing (Regrouping)</h3>
        <p>Sometimes you need to borrow, just like with whole numbers:</p>
        <div class='example-box'>
            <p><strong>Example: 3.2 - 1.5</strong></p>
            <p>Can't do 2 - 5, so borrow from the 3<br>
            3.2 becomes 2.12 (borrow 1 from ones place)<br>
            2.12 - 1.5 = 1.62</p>
            <p style="text-align: center; font-family: monospace;">
            &nbsp;&nbsp;3.20<br>
            - 1.50<br>
            ------<br>
            &nbsp;&nbsp;1.70<br>
            </p>
        </div>

        <h3>Real-World Practice: Money</h3>
        <p>Money is a perfect example of decimals:</p>
        <div class='example-box'>
            <p>You have $5.75. You spend $2.30. How much is left?<br>
            $5.75 - $2.30 = $3.45</p>
        </div>
        """
    }
]
