QUIZ = [
    {
        "question": "A bag contains 4 red, 5 blue, 3 yellow balls. Draw two balls without replacement. Find P(both same color).",
        "answer": "P(both red) + P(both blue) + P(both yellow) = (4×3)/(12×11) + (5×4)/(12×11) + (3×2)/(12×11) = (12+20+6)/132 = 38/132 = 19/66",
        "explanation": "For each color, multiply the probability of first draw by the conditional probability of second. P(both red) = (4/12)×(3/11), etc."
    },
    {
        "question": "A student passes a test with probability 0.7 if they study, and 0.3 if they don't. They study 80% of the time. What is the probability they pass?",
        "answer": "P(pass) = 0.8 × 0.7 + 0.2 × 0.3 = 0.56 + 0.06 = 0.62",
        "explanation": "Use tree diagram: Path 1 (study and pass): 0.8 × 0.7 = 0.56. Path 2 (don't study and pass): 0.2 × 0.3 = 0.06. Total: 0.62."
    },
    {
        "question": "Given the student passed (from Question 2), find P(studied | passed) using Bayes' theorem.",
        "answer": "P(studied|passed) = P(passed|studied) × P(studied) / P(passed) = (0.7 × 0.8) / 0.62 = 0.56 / 0.62 ≈ 0.9032",
        "explanation": "Use Bayes: P(A|B) = P(B|A)×P(A) / P(B). Here, A=studied, B=passed."
    },
    {
        "question": "In a deck of cards, are the events 'drawing a spade' and 'drawing a 7' mutually exclusive or independent? Justify.",
        "answer": "Neither mutually exclusive nor independent. P(spade) = 13/52, P(7) = 4/52, P(spade and 7) = 1/52. Not exclusive because they can both occur (the 7 of spades). Not independent because P(spade)×P(7) = (1/4)×(1/13) = 1/52 ≠ P(both)=1/52. Wait, these ARE equal, so they are independent.",
        "explanation": "P(spade) = 13/52 = 1/4. P(7) = 4/52 = 1/13. P(spade)×P(7) = (1/4)×(1/13) = 1/52. P(spade and 7) = 1/52. Since these products match, the events are independent."
    },
    {
        "question": "Two cards are drawn with replacement. Find P(first is red AND second is a face card).",
        "answer": "P(first red) × P(second face) = (26/52) × (12/52) = (1/2) × (3/13) = 3/26",
        "explanation": "With replacement, probabilities don't change. P(red) = 26/52 = 1/2. P(face card) = 12/52 = 3/13. Multiply for independent events."
    }
]
