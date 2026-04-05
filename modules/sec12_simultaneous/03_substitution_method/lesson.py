TITLE = "The Substitution Method"

SECTIONS = [
    {
        "title": "The Core Idea: Replace One Variable",
        "body": "<p>The substitution method works by solving one equation for one variable, then using that expression wherever that variable appears in the other equation.</p><div class='concept-box'><p><strong>Example:</strong></p><p>If we know \\(y = 2x + 1\\), we can replace y with '2x + 1' in the second equation. This turns two unknowns into one.</p></div><p>This method is especially useful when one variable is already isolated (like y = ...) or has a coefficient of 1 or -1.</p>"
    },
    {
        "title": "When One Variable is Already Isolated",
        "body": "<p><strong>Example 1:</strong> y is already isolated</p><pre class='code-block'>Equation 1: y = 2x + 1\nEquation 2: x + y = 4\n\ny is already solved in Equation 1, so substitute into Equation 2:\nx + (2x + 1) = 4\n3x + 1 = 4\n3x = 3\nx = 1\n\nSubstitute back into Equation 1:\ny = 2(1) + 1 = 3\n\nCheck in Equation 2: 1 + 3 = 4 ✓\nSolution: x = 1, y = 3</pre></p>"
    },
    {
        "title": "When You Need to Rearrange First",
        "body": "<p><strong>Example 2:</strong> Rearrange to isolate a variable</p><pre class='code-block'>Equation 1: 2x + y = 5\nEquation 2: x - y = 1\n\nSolve Equation 1 for y:\ny = 5 - 2x\n\nSubstitute into Equation 2:\nx - (5 - 2x) = 1\nx - 5 + 2x = 1\n3x - 5 = 1\n3x = 6\nx = 2\n\nSubstitute back:\ny = 5 - 2(2) = 5 - 4 = 1\n\nCheck in Equation 1: 2(2) + 1 = 5 ✓\nCheck in Equation 2: 2 - 1 = 1 ✓\nSolution: x = 2, y = 1</pre></p>"
    },
    {
        "title": "When to Choose Substitution Over Elimination",
        "body": "<p>Use substitution when:</p><ul><li>One equation is already solved for one variable (y = ...)</li><li>One variable has a coefficient of 1 or -1 (easy to isolate)</li><li>The coefficients don't have convenient factors for elimination</li></ul><p>Use elimination when:</p><ul><li>Both equations have the same variable with the same or opposite coefficients</li><li>You would need to rearrange significantly to use substitution</li><li>Multiplying to match coefficients is simpler than rearranging</li></ul>"
    }
]
