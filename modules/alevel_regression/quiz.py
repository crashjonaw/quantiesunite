QUIZ = [
    {
        "question": "Explain why correlation does not imply causation with a concrete example",
        "answer": "Example: Ice cream sales and drowning deaths are correlated (both increase in summer), but ice cream doesn't cause drowning. A third variable (warm weather) causes both.",
        "explanation": "Correlation measures association, not causation. Alternative explanations: (1) Reverse causation: z causes x instead. (2) Confounding: a third variable Z causes both x and y. (3) Coincidence: spurious correlation. To establish causation, we need experimental design or careful causal reasoning."
    },
    {
        "question": "Data from 5 points: (1,2), (2,3), (3,5), (4,6), (5,8). Calculate the correlation coefficient r.",
        "answer": "r ≈ 0.99 (very strong positive correlation)",
        "explanation": "x̄ = 3, ȳ = 4.8. Computing using the formula: Σ(xy) = 1(2) + 2(3) + 3(5) + 4(6) + 5(8) = 2+6+15+24+40 = 87. Σx² = 55, Σy² = 129. n=5. r = [5(87) - 15(24)] / √{[5(55)-225][5(129)-576]} = [435-360] / √{[275-225][645-576]} = 75 / √(50×69) ≈ 0.996."
    },
    {
        "question": "The regression line is ŷ = 20 + 3x. A particular observation has x = 10 and y = 48. Calculate the residual.",
        "answer": "Residual = -2 (or e = y - ŷ = 48 - 50 = -2)",
        "explanation": "ŷ = 20 + 3(10) = 50. Residual = actual - predicted = 48 - 50 = -2. Negative residual means the actual value is below the regression line."
    },
    {
        "question": "Explain the difference between r² and r, and why r² is often preferred for interpretation",
        "answer": "r is correlation coefficient (-1 to 1); r² is coefficient of determination (0 to 1). r² = proportion of variance explained. r² is preferred because it's percentage-based and easier to interpret quantitatively (e.g., 0.64 = 64% of variance explained).",
        "explanation": "Example: r = 0.8 means strong correlation. r² = 0.64 means 64% of variation in y is explained by x. The latter is more intuitive for practical decision-making."
    },
    {
        "question": "A scatter plot shows a curved (non-linear) pattern. How would you address this in regression?",
        "answer": "Options: (1) Transform variables (log, square root) to linearize. (2) Fit a polynomial or non-linear curve. (3) Use multiple regression with additional predictors. (4) Acknowledge that linear regression is inappropriate and report limitations.",
        "explanation": "Example 1: If y = ax^b (power law), use log-log transformation. Example 2: If data shows parabolic shape, fit a quadratic: ŷ = a + bx + cx². Always check residual plots to ensure assumptions are satisfied after transformation."
    }
]
