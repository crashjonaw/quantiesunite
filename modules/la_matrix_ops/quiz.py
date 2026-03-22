QUIZ = [
    {
        "question": "Compute [[2, 1], [0, 3]] × [[1, 2], [4, 0]].",
        "answer": "[[6, 4], [12, 0]]",
        "explanation": "First row: [2·1+1·4, 2·2+1·0]=[6,4]. Second row: [0·1+3·4, 0·2+3·0]=[12,0]."
    },
    {
        "question": "If (AB)^T = B^T A^T, verify this property with A=[[1,2]], B=[[3],[4]].",
        "answer": "AB = [[11]], (AB)^T = [[11]]. B^T A^T = [[3,4]]·[[1],[2]] = [[11]]. Both equal [[11]]. ✓",
        "explanation": "The property (AB)^T = B^T A^T is a fundamental identity (note order reversal)."
    },
    {
        "question": "True or False: Matrix multiplication is commutative (AB = BA for all invertible matrices A, B).",
        "answer": "False",
        "explanation": "Even for invertible matrices, generally AB ≠ BA. They commute only in special cases (e.g., if one is a scalar multiple of the identity)."
    },
    {
        "question": "Find the inverse of A = [[2, 0], [0, 3]] using Gauss-Jordan.",
        "answer": "A^(-1) = [[1/2, 0], [0, 1/3]]",
        "explanation": "[A|I] = [[2,0|1,0],[0,3|0,1]]. Scale R1 by 1/2, R2 by 1/3 to get [I|A^(-1)]."
    },
    {
        "question": "For a 3×3 matrix, (A^(-1))^(-1) equals what?",
        "answer": "A",
        "explanation": "Applying inverse twice returns the original matrix: (A^(-1))^(-1) = A."
    }
]
