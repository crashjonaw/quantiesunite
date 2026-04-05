MINDMAP = {
    "concepts": [
        {"title": "Arrays", "points": [
            "np.array([1,2,3]) — homogeneous, fixed-size",
            "Shape: .shape, Reshape: .reshape(rows, cols)",
            "Creators: np.zeros(), np.ones(), np.arange(), np.linspace()",
        ]},
        {"title": "Vectorised Operations", "points": [
            "Element-wise: a + b, a * b, a ** 2 — no loops needed",
            "Broadcasting: smaller array stretched to match larger",
            "Universal functions: np.sin(), np.exp(), np.sqrt()",
        ]},
        {"title": "Indexing & Slicing", "points": [
            "1D: a[2], a[1:4]",
            "2D: a[row, col], a[:, 0] (all rows, column 0)",
            "Boolean indexing: a[a > 5] — filters by condition",
        ]},
        {"title": "Linear Algebra", "points": [
            "Matrix multiply: a @ b or np.dot(a, b)",
            "np.linalg.inv(), np.linalg.det(), np.linalg.eig()",
            "Solve Ax=b: np.linalg.solve(A, b)",
        ]},
    ],
    "formulas": [],
    "tips": [
        "NumPy arrays are much faster than Python lists for numerical operations",
        "Avoid loops — use vectorised operations and broadcasting instead",
        "a.copy() creates a true copy; slicing creates a view that shares memory",
    ],
}
