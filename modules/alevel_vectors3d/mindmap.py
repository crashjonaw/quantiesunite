MINDMAP = {
    "concepts": [
        {
            "title": "3D Vectors Basics",
            "points": [
                "Position vector: \\(\\mathbf{r} = x\\mathbf{i} + y\\mathbf{j} + z\\mathbf{k}\\)",
                "Magnitude: \\(|\\mathbf{r}| = \\sqrt{x^2 + y^2 + z^2}\\)",
                "Unit vector: \\(\\hat{\\mathbf{r}} = \\frac{\\mathbf{r}}{|\\mathbf{r}|}\\)",
                "Direction ratios and direction cosines",
            ],
        },
        {
            "title": "Scalar (Dot) Product",
            "points": [
                "\\(\\mathbf{a} \\cdot \\mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3\\)",
                "\\(\\mathbf{a} \\cdot \\mathbf{b} = |\\mathbf{a}||\\mathbf{b}|\\cos\\theta\\)",
                "Perpendicular vectors: \\(\\mathbf{a} \\cdot \\mathbf{b} = 0\\)",
                "Projection of \\(\\mathbf{a}\\) on \\(\\mathbf{b}\\): \\(\\frac{\\mathbf{a} \\cdot \\mathbf{b}}{|\\mathbf{b}|}\\)",
            ],
        },
        {
            "title": "Cross Product",
            "points": [
                "\\(\\mathbf{a} \\times \\mathbf{b} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ a_1 & a_2 & a_3 \\\\ b_1 & b_2 & b_3 \\end{vmatrix}\\)",
                "Result is perpendicular to both \\(\\mathbf{a}\\) and \\(\\mathbf{b}\\)",
                "\\(|\\mathbf{a} \\times \\mathbf{b}| = |\\mathbf{a}||\\mathbf{b}|\\sin\\theta\\)",
                "Area of parallelogram = \\(|\\mathbf{a} \\times \\mathbf{b}|\\)",
            ],
        },
        {
            "title": "Lines in 3D",
            "points": [
                "Vector equation: \\(\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{d}\\)",
                "Parametric: \\(x = a_1 + \\lambda d_1\\), etc.",
                "Cartesian: \\(\\frac{x-a_1}{d_1} = \\frac{y-a_2}{d_2} = \\frac{z-a_3}{d_3}\\)",
                "Parallel lines: direction vectors are scalar multiples",
            ],
        },
        {
            "title": "Planes",
            "points": [
                "Scalar product form: \\(\\mathbf{r} \\cdot \\mathbf{n} = d\\)",
                "Cartesian: \\(ax + by + cz = d\\), where \\(\\mathbf{n} = (a, b, c)\\)",
                "Distance from point to plane: \\(\\frac{|\\mathbf{p} \\cdot \\mathbf{n} - d|}{|\\mathbf{n}|}\\)",
                "Angle between line and plane: \\(\\sin\\alpha = \\frac{|\\mathbf{d} \\cdot \\mathbf{n}|}{|\\mathbf{d}||\\mathbf{n}|}\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Dot product", "expr": "\\(\\mathbf{a} \\cdot \\mathbf{b} = |\\mathbf{a}||\\mathbf{b}|\\cos\\theta\\)"},
        {"label": "Cross product magnitude", "expr": "\\(|\\mathbf{a} \\times \\mathbf{b}| = |\\mathbf{a}||\\mathbf{b}|\\sin\\theta\\)"},
        {"label": "Line equation", "expr": "\\(\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{d}\\)"},
        {"label": "Plane equation", "expr": "\\(\\mathbf{r} \\cdot \\mathbf{n} = d\\)"},
        {"label": "Point-to-plane distance", "expr": "\\(\\frac{|ax_0 + by_0 + cz_0 - d|}{\\sqrt{a^2+b^2+c^2}}\\)"},
    ],
    "tips": [
        "Two lines in 3D that are not parallel may still not intersect — they could be skew lines.",
        "To find the line of intersection of two planes, use the cross product of their normals for the direction.",
        "The foot of perpendicular from a point to a line: substitute the line equation into the perpendicularity condition.",
    ],
}
