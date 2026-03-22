QUIZ = [
    {
        "question": "A survey of 200 students' daily screen time (minutes) shows: median 240, Q₁ = 180, Q₃ = 300. Are there any outliers if one student reported 480 minutes?",
        "answer": "No outliers in this case. Outlier threshold: Q₃ + 1.5(IQR) = 300 + 1.5(120) = 480. The value 480 is exactly at the threshold, so borderline.",
        "explanation": "IQR = 300 − 180 = 120. Upper threshold = 300 + 1.5(120) = 300 + 180 = 480. Since 480 equals the threshold, it's not beyond it, so technically not an outlier (though it's on the boundary)."
    },
    {
        "question": "A dataset has mean 50 and standard deviation 8. Using z-scores, which is more unusual: a value of 70 or a value of 34?",
        "answer": "Both are equally unusual (z = ±2.5), but if forced to choose, both are comparably extreme.",
        "explanation": "z(70) = (70−50)/8 = 2.5. z(34) = (34−50)/8 = −2. The value 70 is 2.5 SDs above the mean, while 34 is 2 SDs below. So 70 is slightly more unusual."
    },
    {
        "question": "Test scores follow a normal distribution with mean 70 and standard deviation 12. Estimate the percentage of students scoring above 94.",
        "answer": "Approximately 0.15% (or about 2.5% if we count from 94 as 2σ above mean)",
        "explanation": "94 = 70 + 24 = 70 + 2(12), so it's 2 SDs above the mean. By empirical rule, 95% fall within 2σ, so 5% fall outside. By symmetry, 2.5% are above 2σ."
    },
    {
        "question": "Two factories produce widgets. Factory A: mean 100 units/day, SD 5. Factory B: mean 102 units/day, SD 8. Which factory is more reliable? Justify.",
        "answer": "Factory A is more reliable (lower SD = 5 vs 8). Though Factory B has slightly higher mean output, Factory A is more consistent.",
        "explanation": "Standard deviation measures variability. Factory A's lower SD means output is more predictable and stable, which is desirable for reliability."
    },
    {
        "question": "In a cumulative frequency graph with total frequency 120, at what cumulative frequency value would you read the median and Q₃?",
        "answer": "Median: 60; Q₃: 90",
        "explanation": "Median is at 50% of data: 120/2 = 60. Q₃ (upper quartile) is at 75% of data: 0.75 × 120 = 90."
    }
]
