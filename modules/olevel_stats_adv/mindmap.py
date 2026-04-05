MINDMAP = {
    "concepts": [
        {
            "title": "Cumulative Frequency",
            "points": [
                "Running total of frequencies up to each class boundary",
                "Plot upper class boundary against cumulative frequency",
                "Use S-shaped (ogive) curve to estimate median, quartiles, percentiles",
                "Median = value at \\(\\frac{n}{2}\\) on the cumulative frequency axis",
            ],
        },
        {
            "title": "Box-and-Whisker Plots",
            "points": [
                "Five-number summary: min, Q1, median, Q3, max",
                "Interquartile range: \\(\\text{IQR} = Q_3 - Q_1\\)",
                "Outliers typically defined as values beyond \\(Q_1 - 1.5 \\times \\text{IQR}\\) or \\(Q_3 + 1.5 \\times \\text{IQR}\\)",
                "Useful for comparing distributions side by side",
            ],
        },
        {
            "title": "Standard Deviation",
            "points": [
                "Measures spread of data around the mean",
                "Population SD: \\(\\sigma = \\sqrt{\\frac{\\sum (x_i - \\bar{x})^2}{n}}\\)",
                "Alternative form: \\(\\sigma = \\sqrt{\\frac{\\sum x_i^2}{n} - \\bar{x}^2}\\)",
                "Larger SD means data is more spread out",
            ],
        },
        {
            "title": "Grouped Data Calculations",
            "points": [
                "Use mid-values of class intervals for mean and SD",
                "Estimated mean: \\(\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}\\)",
                "Histogram: frequency density = \\(\\frac{\\text{frequency}}{\\text{class width}}\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Mean (grouped)", "expr": "\\(\\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i}\\)"},
        {"label": "Variance", "expr": "\\(\\sigma^2 = \\frac{\\sum f_i x_i^2}{\\sum f_i} - \\bar{x}^2\\)"},
        {"label": "Standard Deviation", "expr": "\\(\\sigma = \\sqrt{\\frac{\\sum f_i (x_i - \\bar{x})^2}{\\sum f_i}}\\)"},
        {"label": "Interquartile Range", "expr": "\\(\\text{IQR} = Q_3 - Q_1\\)"},
        {"label": "Percentile position", "expr": "\\(P_k = \\frac{k}{100} \\times n\\)"},
    ],
    "tips": [
        "Always use upper class boundaries when plotting cumulative frequency curves.",
        "The mean-SD form \\(\\sqrt{\\frac{\\sum x^2}{n} - \\bar{x}^2}\\) is usually faster for calculation.",
        "When comparing data sets, compare both a measure of central tendency (mean/median) and spread (IQR/SD).",
        "Check if the question asks for population or sample SD — O-Level typically uses population SD (divide by n).",
    ],
}
