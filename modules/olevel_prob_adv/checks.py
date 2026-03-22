CHECKS = [
    {
        "q": "In a bag: 5 red, 3 blue, 2 green marbles. P(drawing red or green)?",
        "a": "7/10",
        "hint": "Red or green: (5 + 2) / (5 + 3 + 2) = 7/10. These are mutually exclusive."
    },
    {
        "q": "Draw two cards without replacement. P(both hearts)?",
        "a": "13/52 × 12/51 = 156/2652 = 1/17",
        "hint": "After drawing first heart, 12 hearts left out of 51 cards."
    },
    {
        "q": "P(getting heads | fair coin is flipped) = ? Is flipping heads independent of nothing?",
        "a": "P(H) = 1/2. Yes, it's independent of any other coin flip (assuming fair coin and independent trials).",
        "hint": "Coin flips are independent events. Each flip has the same probability."
    },
    {
        "q": "From a deck, P(red card OR face card) = ?",
        "a": "P(red or face) = 26/52 + 12/52 - 6/52 = 32/52 = 8/13",
        "hint": "Use addition rule with overlap: 6 red face cards are counted in both categories."
    },
    {
        "q": "A die is rolled. P(rolling > 4)?",
        "a": "2/6 = 1/3",
        "hint": "Values > 4 are {5, 6}."
    }
]
