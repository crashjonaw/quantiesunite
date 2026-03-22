QUIZ = [
    {
        "question": "Normalize the vector v = (3, 4, 0)",
        "answer": "v̂ = (3/5, 4/5, 0)",
        "explanation": "|v| = √(9 + 16 + 0) = √25 = 5. So v̂ = v/|v| = (3/5, 4/5, 0). Verify: |v̂| = √(9/25 + 16/25 + 0) = √1 = 1."
    },
    {
        "question": "Find the vector projection of u = (3, 4, 0) onto v = (1, 0, 0)",
        "answer": "proj_v(u) = (3, 0, 0)",
        "explanation": "u·v = 3, |v|² = 1. proj_v(u) = (u·v/|v|²)v = 3(1, 0, 0) = (3, 0, 0)."
    },
    {
        "question": "Determine if the lines r = (1, 2, 3) + s(1, 1, 0) and r = (2, 1, 3) + t(2, 2, 0) are parallel.",
        "answer": "Yes, they are parallel.",
        "explanation": "The direction vectors are (1, 1, 0) and (2, 2, 0). Since (2, 2, 0) = 2(1, 1, 0), the direction vectors are scalar multiples, so the lines are parallel."
    },
    {
        "question": "Find the equation of the plane with normal vector n = (2, 3, -1) passing through P(1, -1, 2)",
        "answer": "2x + 3y - z = -3 or 2(x - 1) + 3(y + 1) - 1(z - 2) = 0",
        "explanation": "The plane equation is n·(r - a) = 0. So 2(x - 1) + 3(y + 1) - 1(z - 2) = 0, which simplifies to 2x + 3y - z = -3."
    },
    {
        "question": "Show that the vectors u = (1, 2, 3), v = (2, -1, 0), and w = (3, 1, 3) are coplanar.",
        "answer": "The scalar triple product u·(v × w) = 0, so the vectors are coplanar.",
        "explanation": "v × w = (-1·3 - 0·1, 0·3 - 2·3, 2·1 - (-1)·3) = (-3, -6, 5). u·(v × w) = 1(-3) + 2(-6) + 3(5) = -3 - 12 + 15 = 0. Since the scalar triple product is zero, the vectors are coplanar (lie in the same plane)."
    }
]
