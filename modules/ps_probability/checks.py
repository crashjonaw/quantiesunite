CHECKS = [
    {
        "id": "check_axioms_basic",
        "section": "ps_prob_axioms",
        "type": "multiple_choice",
        "question": "Which of the following is NOT one of Kolmogorov's axioms?",
        "options": [
            "P(A) >= 0 for all events A",
            "P(Omega) = 1",
            "For disjoint events, P(A ∪ B) = P(A) + P(B)",
            "P(A ∪ B) = P(A) + P(B) for ANY events A and B"
        ],
        "correct": 3,
        "explanation": "Axiom 3 (additivity) only applies to disjoint events. For arbitrary events, we use the inclusion-exclusion principle."
    },
    {
        "id": "check_complement_rule",
        "section": "ps_prob_axioms",
        "type": "fill_blank",
        "question": "If P(A) = 0.3, then P(A^c) = ______",
        "answer": "0.7",
        "explanation": "By the Complement Rule: P(A^c) = 1 - P(A) = 1 - 0.3 = 0.7"
    },
    {
        "id": "check_sample_space",
        "section": "ps_prob_sample_space",
        "type": "multiple_choice",
        "question": "When flipping a coin twice, how many outcomes are in the sample space?",
        "options": [
            "2",
            "4",
            "6",
            "8"
        ],
        "correct": 1,
        "explanation": "Ω = {HH, HT, TH, TT}, so |Ω| = 4"
    },
    {
        "id": "check_conditional_definition",
        "section": "ps_prob_conditional",
        "type": "fill_blank",
        "question": "If P(A ∩ B) = 0.12 and P(B) = 0.4, then P(A|B) = ______",
        "answer": "0.3",
        "explanation": "P(A|B) = P(A ∩ B) / P(B) = 0.12 / 0.4 = 0.3"
    },
    {
        "id": "check_bayes_simple",
        "section": "ps_prob_conditional",
        "type": "multiple_choice",
        "question": "Bayes' rule states P(A|B) = __________",
        "options": [
            "P(B|A) / P(A)",
            "P(B|A) * P(A) / P(B)",
            "P(A) * P(B) / P(A|B)",
            "P(A) + P(B) - P(A ∩ B)"
        ],
        "correct": 1,
        "explanation": "Bayes' rule: P(A|B) = P(B|A) * P(A) / P(B)"
    },
    {
        "id": "check_independence_def",
        "section": "ps_prob_independence",
        "type": "multiple_choice",
        "question": "Events A and B are independent if and only if:",
        "options": [
            "P(A ∩ B) = 0",
            "P(A|B) = P(A)",
            "P(A) = P(B)",
            "A ∩ B = ∅"
        ],
        "correct": 1,
        "explanation": "Independence means: P(A|B) = P(A), equivalently P(A ∩ B) = P(A) * P(B)"
    },
    {
        "id": "check_combination_counting",
        "section": "ps_prob_combinatorics",
        "type": "fill_blank",
        "question": "C(6, 2) = \\(\\binom{6}{2}\\) = ______",
        "answer": "15",
        "explanation": "C(6,2) = 6! / (2! * 4!) = (6 * 5) / (2 * 1) = 15"
    },
    {
        "id": "check_permutation_counting",
        "section": "ps_prob_combinatorics",
        "type": "fill_blank",
        "question": "P(5, 3) = ______",
        "answer": "60",
        "explanation": "P(5,3) = 5! / (5-3)! = 5! / 2! = 120 / 2 = 60"
    }
]
