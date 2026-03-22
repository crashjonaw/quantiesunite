CHECKS = [
    {
        "q": "Given data: 3, 7, 8, 12, 15, 18, 22. Find Q₁, Q₂, Q₃.",
        "a": "Q₁ = 7.5, Q₂ = 12, Q₃ = 18.5",
        "hint": "With 7 values: Q₁ position = 8/4 = 2, Q₂ position = 8/2 = 4, Q₃ position = 12/4 = 3. Wait: (7+8)/2=7.5 for Q₁, 12 is the middle, (18+22)/2 for upper... Actually, recalculate: position for Q₁ = (7+1)/4 = 2, for Q₃ = 3(7+1)/4 = 6."
    },
    {
        "q": "Calculate the variance and standard deviation of: 4, 6, 8, 10, 12",
        "a": "Mean = 8; Variance = 8; SD ≈ 2.83",
        "hint": "Find mean first. Then calculate (x−mean)² for each value, average them (variance), and take the square root."
    },
    {
        "q": "A dataset has IQR = 12. What is the outlier threshold range?",
        "a": "Outliers are outside [Q₁ − 18, Q₃ + 18]. More precisely: any value outside [Q₁−1.5(IQR), Q₃+1.5(IQR)]",
        "hint": "Use 1.5 × IQR as the threshold distance from quartiles."
    },
    {
        "q": "Test scores are normally distributed with mean 75 and SD 10. What percentage of students score between 65 and 85?",
        "a": "68%",
        "hint": "65 to 85 is within μ ± σ. Use the empirical rule."
    },
    {
        "q": "Two classes have: Class A (mean 80, SD 5) and Class B (mean 80, SD 12). Which is more consistent?",
        "a": "Class A (lower SD means more consistent)",
        "hint": "Lower standard deviation indicates less variability and more consistency."
    }
]
