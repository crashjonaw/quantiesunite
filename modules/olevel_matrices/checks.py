CHECKS = [
    {
        "q": "Add matrices: A = [[1, 2], [3, 4]] and B = [[2, 0], [1, 5]]",
        "a": "A + B = [[3, 2], [4, 9]]",
        "hint": "Add corresponding elements: (1+2, 2+0), (3+1, 4+5)"
    },
    {
        "q": "Multiply: [[2, 3], [1, 4]] × [[1, 0], [2, 1]]",
        "a": "[[8, 3], [9, 4]]",
        "hint": "(2,3)·(1,2) = 2+6=8; (2,3)·(0,1) = 0+3=3; (1,4)·(1,2) = 1+8=9; (1,4)·(0,1) = 0+4=4"
    },
    {
        "q": "Find det(A) for A = [[4, 2], [1, 3]]",
        "a": "det(A) = 12 - 2 = 10",
        "hint": "det = ad - bc = 4(3) - 2(1)"
    },
    {
        "q": "Find A⁻¹ for A = [[2, 1], [3, 2]]",
        "a": "A⁻¹ = [[2, -1], [-3, 2]]. Or with det=1: A⁻¹ = [[2, -1], [-3, 2]]",
        "hint": "det = 2(2) - 1(3) = 1. Swap 2 and 2, negate 1 and 3."
    },
    {
        "q": "Solve using matrices: 2x + y = 5, x - y = 1",
        "a": "x = 2, y = 1",
        "hint": "Write as AX = B, find A⁻¹, then X = A⁻¹B"
    }
]
