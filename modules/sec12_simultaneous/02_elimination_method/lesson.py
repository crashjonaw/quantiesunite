TITLE = "The Elimination Method"

SECTIONS = [
    {
        "title": "The Core Idea: Make Coefficients Match",
        "body": "<p>The elimination method works by making one variable 'disappear'. To do this, we need the coefficients of one variable to be equal or opposite in the two equations.</p><div class='concept-box'><p>If we have \\(2x + y = 7\\) and \\(x - y = 2\\), notice the y coefficients are +1 and -1 (opposites). If we add them:</p><p>\\((2x + y) + (x - y) = 7 + 2\\)<br>\\(3x = 9\\)<br>\\(x = 3\\)</p><p>The y variable has been eliminated!</p></div>"
    },
    {
        "title": "When Coefficients Already Match (Easy Case)",
        "body": "<p><strong>Example 1:</strong> Eliminate y directly</p><pre class='code-block'>Equation 1: 2x + y = 7\nEquation 2: x - y = 2\n\nNotice y coefficients: +1 and -1 (opposites)\nAdd the equations:\n(2x + y) + (x - y) = 7 + 2\n3x = 9\nx = 3\n\nSubstitute x = 3 into Equation 2:\n3 - y = 2\ny = 1\n\nCheck in Equation 1: 2(3) + 1 = 7 ✓\nSolution: x = 3, y = 1</pre></p>"
    },
    {
        "title": "When You Need to Multiply First",
        "body": "<p><strong>Example 2:</strong> Make coefficients equal by multiplying</p><pre class='code-block'>Equation 1: 3x + 2y = 11\nEquation 2: 2x + y = 7\n\nThe y coefficients are 2 and 1. Multiply Equation 2 by 2:\nEq 2 × 2: 4x + 2y = 14\n\nNow both have 2y. Subtract to eliminate y:\n(3x + 2y) - (4x + 2y) = 11 - 14\n3x - 4x = -3\n-x = -3\nx = 3\n\nSubstitute x = 3 into Equation 2:\n2(3) + y = 7\ny = 1\n\nCheck in Equation 1: 3(3) + 2(1) = 11 ✓\nSolution: x = 3, y = 1</pre></p>"
    },
    {
        "title": "Step-by-Step Process",
        "body": "<ol><li>Write both equations clearly.</li><li>Choose which variable to eliminate (often the one with simplest coefficients).</li><li>Multiply one or both equations to make coefficients equal or opposite.</li><li>Add (if opposite) or subtract (if equal and same sign) to eliminate that variable.</li><li>Solve the single-variable equation.</li><li>Substitute back into an original equation to find the other variable.</li><li>Check in both original equations.</li></ol><p><strong>Key principle:</strong> When we add or subtract equations, we use the fact that if A = B and C = D, then A + C = B + D. This keeps the system balanced.</p>"
    }
]
