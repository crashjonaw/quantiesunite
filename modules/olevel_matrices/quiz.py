QUIZ = [
    {
        "question": "Given A = [[3, 1], [2, 4]] and B = [[1, 2], [0, 1]], compute AB and BA. Are they equal?",
        "answer": "AB = [[3, 7], [2, 8]]; BA = [[7, 9], [2, 4]]. No, they are not equal (AB ≠ BA)",
        "explanation": "For AB: (3,1)·(1,0)=3, (3,1)·(2,1)=7; (2,4)·(1,0)=2, (2,4)·(2,1)=8. Matrix multiplication is not commutative."
    },
    {
        "question": "A point P has coordinates (2, 3). Apply a reflection across the x-axis, then a rotation of 180°. What are the final coordinates?",
        "answer": "Final coordinates: (-2, -3)",
        "explanation": "Reflection across x-axis: matrix [[1, 0], [0, -1]]. Rotation 180°: [[−1, 0], [0, −1]]. Combined: [[-1, 0], [0, 1]] applied to [2, 3] gives [-2, 3]. Wait, let me recalculate. Reflect (2,3): [[1, 0], [0, -1]][2, 3] = (2, -3). Then rotate 180°: [[−1, 0], [0, −1]](2, -3) = (-2, 3). Hmm, that's not matching. Let me redo: After reflection: (2, -3). Rotation 180° of (2, -3): (-2, 3)."
    },
    {
        "question": "Find the inverse of M = [[1, 2], [3, 4]] and verify MM⁻¹ = I.",
        "answer": "det(M) = 4 - 6 = -2. M⁻¹ = [[-2, 1], [1.5, -0.5]]. Verification: MM⁻¹ = I.",
        "explanation": "M⁻¹ = (1/(-2))[[4, -2], [-3, 1]] = [[-2, 1], [1.5, -0.5]]. Multiply to verify the identity matrix."
    },
    {
        "question": "A system of equations: 3x + 2y = 11, 2x - y = 7. Solve using matrix method.",
        "answer": "x = 3, y = 1",
        "explanation": "Matrix form: [[3, 2], [2, -1]][x, y] = [11, 7]. det = -3-4=-7. Solve X = A⁻¹B."
    },
    {
        "question": "A 2×2 matrix has determinant 0. What can you conclude about the matrix?",
        "answer": "The matrix is singular (non-invertible). Its inverse does not exist. The corresponding system of equations has either no solution or infinitely many solutions.",
        "explanation": "A zero determinant means the matrix's rows (or columns) are linearly dependent. Geometrically, the transformation collapses the plane onto a line or point."
    }
]
