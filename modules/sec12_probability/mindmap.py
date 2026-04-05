MINDMAP = {
    "concepts": [
        {
            "title": "What is Probability?",
            "points": [
                "Probability measures how likely an event is to occur",
                "Range: \\(0 \\leq P \\leq 1\\)",
                "\\(P = 0\\): impossible; \\(P = 1\\): certain",
            ],
        },
        {
            "title": "Calculating Probability",
            "points": [
                "\\(P(\\text{event}) = \\frac{\\text{Number of favourable outcomes}}{\\text{Total number of outcomes}}\\)",
                "All outcomes must be equally likely",
                "Example: rolling a 3 on a fair die → \\(P = \\frac{1}{6}\\)",
            ],
        },
        {
            "title": "Complementary Events",
            "points": [
                "\\(P(\\text{not } A) = 1 - P(A)\\)",
                "Example: \\(P(\\text{not 3}) = 1 - \\frac{1}{6} = \\frac{5}{6}\\)",
            ],
        },
        {
            "title": "Sample Space & Listing Outcomes",
            "points": [
                "List all possible outcomes systematically",
                "Use a table or tree diagram for combined events",
                "Example: tossing 2 coins → {HH, HT, TH, TT}, 4 outcomes",
            ],
        },
        {
            "title": "Experimental Probability",
            "points": [
                "Based on actual experiments/observations",
                "\\(P \\approx \\frac{\\text{frequency of event}}{\\text{total trials}}\\)",
                "More trials → experimental probability gets closer to theoretical",
            ],
        },
    ],
    "formulas": [
        {"label": "Probability", "expr": "\\(P(A) = \\frac{n(A)}{n(S)}\\)"},
        {"label": "Complement", "expr": "\\(P(A') = 1 - P(A)\\)"},
        {"label": "Expected frequency", "expr": "\\(\\text{Expected} = P(A) \\times \\text{number of trials}\\)"},
    ],
    "tips": [
        "Probability is always between 0 and 1 — if you get a value outside this range, check your work.",
        "Express probability as a fraction, decimal, or percentage as required.",
        "Use systematic listing to avoid missing or double-counting outcomes.",
    ],
}
