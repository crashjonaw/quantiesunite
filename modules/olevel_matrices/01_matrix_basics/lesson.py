TITLE = "What is a Matrix? Introduction and Notation"

SECTIONS = [
    {
        "title": "Understanding Matrices from First Principles",
        "body": """
        <div class="concept-box">
            <h3>What is a Matrix?</h3>
            <p>Imagine you have data organized in a table. For example, test scores for 3 students across 4 subjects:</p>
            <table style="border-collapse: collapse; margin: 20px auto">
                <tr >
                    <th style="padding: 8px; text-align: left;">Student</th>
                    <th style="padding: 8px;">Math</th>
                    <th style="padding: 8px;">English</th>
                    <th style="padding: 8px;">Science</th>
                    <th style="padding: 8px;">History</th>
                </tr>
                <tr >
                    <td style="padding: 8px; font-weight: bold;">Alice</td>
                    <td style="padding: 8px; text-align: center;">85</td>
                    <td style="padding: 8px; text-align: center;">92</td>
                    <td style="padding: 8px; text-align: center;">88</td>
                    <td style="padding: 8px; text-align: center;">79</td>
                </tr>
                <tr >
                    <td style="padding: 8px; font-weight: bold;">Bob</td>
                    <td style="padding: 8px; text-align: center;">78</td>
                    <td style="padding: 8px; text-align: center;">85</td>
                    <td style="padding: 8px; text-align: center;">91</td>
                    <td style="padding: 8px; text-align: center;">87</td>
                </tr>
                <tr>
                    <td style="padding: 8px; font-weight: bold;">Carol</td>
                    <td style="padding: 8px; text-align: center;">92</td>
                    <td style="padding: 8px; text-align: center;">87</td>
                    <td style="padding: 8px; text-align: center;">85</td>
                    <td style="padding: 8px; text-align: center;">90</td>
                </tr>
            </table>

            <p>A <strong>matrix</strong> is exactly this: a rectangular arrangement of numbers in rows and columns. In matrix form, we'd write the scores (without labels) as:</p>

            <p>$$\\mathbf{M} = \\begin{pmatrix} 85 & 92 & 88 & 79 \\\\ 78 & 85 & 91 & 87 \\\\ 92 & 87 & 85 & 90 \\end{pmatrix}$$</p>

            <p><strong>Why do we use matrices?</strong> Matrices allow us to:</p>
            <ul style="margin-left: 20px;">
                <li>Organize large amounts of data compactly</li>
                <li>Perform calculations on all data simultaneously</li>
                <li>Represent geometric transformations (rotations, reflections)</li>
                <li>Solve systems of equations efficiently</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Matrix Dimensions and Notation",
        "body": """
        <div class="concept-box">
            <h3>Counting Rows and Columns</h3>
            <p>The <strong>dimensions</strong> of a matrix tell you its size. A matrix with <strong>m</strong> rows and <strong>n</strong> columns is called an <strong>m × n</strong> matrix (read "m by n").</p>

            <p>$$\\mathbf{A} = \\begin{pmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \\end{pmatrix} \\quad \\text{3 × 3 matrix}$$</p>

            <p><strong>Element notation:</strong> The element in row \\(i\\) and column \\(j\\) is written as \\(a_{ij}\\).</p>

            <svg viewBox="-35 -5 430 200" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Grid -->
                <rect x="50" y="30" width="270" height="120" fill='none' stroke='currentColor' opacity='0.3' stroke-width="2" rx='4'/>

                <!-- Column lines -->
                <line x1="140" y1="30" x2="140" y2="150" stroke='currentColor' opacity='0.3' stroke-width="1"/>
                <line x1="230" y1="30" x2="230" y2="150" stroke='currentColor' opacity='0.3' stroke-width="1"/>

                <!-- Row lines -->
                <line x1="50" y1="70" x2="320" y2="70" stroke='currentColor' opacity='0.3' stroke-width="1"/>
                <line x1="50" y1="110" x2="320" y2="110" stroke='currentColor' opacity='0.3' stroke-width="1"/>

                <!-- Row 1 values -->
                <text x="95" y="56" font-size='14' fill='currentColor' text-anchor='middle' font-weight='bold'>a₁₁</text>
                <text x="185" y="56" font-size='14' fill='currentColor' text-anchor='middle' font-weight='bold'>a₁₂</text>
                <text x="275" y="56" font-size='14' fill='currentColor' text-anchor='middle' font-weight='bold'>a₁₃</text>

                <!-- Row 2 values -->
                <text x="95" y="96" font-size='14' fill='currentColor' text-anchor='middle'>a₂₁</text>
                <text x="185" y="96" font-size='14' fill='currentColor' text-anchor='middle'>a₂₂</text>
                <text x="275" y="96" font-size='14' fill='currentColor' text-anchor='middle'>a₂₃</text>

                <!-- Row 3 values -->
                <text x="95" y="136" font-size='14' fill='currentColor' text-anchor='middle'>a₃₁</text>
                <text x="185" y="136" font-size='14' fill='currentColor' text-anchor='middle'>a₃₂</text>
                <text x="275" y="136" font-size='14' fill='currentColor' text-anchor='middle'>a₃₃</text>

                <!-- Row labels -->
                <text x="20" y="56" font-size='12' fill='currentColor' opacity='0.6' text-anchor='end'>Row 1</text>
                <text x="20" y="96" font-size='12' fill='currentColor' opacity='0.6' text-anchor='end'>Row 2</text>
                <text x="20" y="136" font-size='12' fill='currentColor' opacity='0.6' text-anchor='end'>Row 3</text>

                <!-- Column labels -->
                <text x="95" y="175" font-size='12' fill='currentColor' opacity='0.6' text-anchor='middle'>Col 1</text>
                <text x="185" y="175" font-size='12' fill='currentColor' opacity='0.6' text-anchor='middle'>Col 2</text>
                <text x="275" y="175" font-size='12' fill='currentColor' opacity='0.6' text-anchor='middle'>Col 3</text>
            </svg>

            <p><strong>Key point:</strong> When we write \\(a_{ij}\\), the first number is the row, the second is the column. So \\(a_{23}\\) means "row 2, column 3".</p>
        </div>
        """
    },
    {
        "title": "Types of Matrices",
        "body": """
        <div class="concept-box">
            <h3>Special Matrix Types</h3>
            <p>Just as we have special numbers (like 0 and 1), we have special matrices:</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Square Matrix</h4>
            <p>A matrix where the number of rows equals the number of columns (m = n).</p>
            <p>$$\\begin{pmatrix} 3 & 7 \\\\ 1 & 5 \\end{pmatrix} \\quad \\text{2 × 2 square matrix}$$</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Identity Matrix (I)</h4>
            <p>A square matrix with 1s on the main diagonal and 0s everywhere else. Think of it as the "matrix version of 1"—multiplying by I doesn't change anything.</p>
            <p>$$\\mathbf{I} = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} \\quad \\text{2 × 2 identity matrix}$$</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Zero Matrix</h4>
            <p>All elements are 0. This is the "matrix version of 0".</p>
            <p>$$\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} \\quad \\text{2 × 3 zero matrix}$$</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Row Matrix (Row Vector)</h4>
            <p>A matrix with just one row. Useful for storing a list of values.</p>
            <p>$$\\begin{pmatrix} 5 & -2 & 8 & 3 \\end{pmatrix} \\quad \\text{1 × 4 row matrix}$$</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Column Matrix (Column Vector)</h4>
            <p>A matrix with just one column. Often used to represent unknowns in equations.</p>
            <p>$$\\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix} \\quad \\text{3 × 1 column matrix}$$</p>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Identifying Dimensions</h4>
            <p><strong>Question:</strong> What are the dimensions of this matrix, and what is \\(a_{21}\\)?</p>
            <p>$$\\mathbf{M} = \\begin{pmatrix} 10 & -3 & 5 \\\\ 2 & 7 & 1 \\\\ 6 & 0 & -4 \\end{pmatrix}$$</p>
            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px;">
                <li>Count rows: 3</li>
                <li>Count columns: 3</li>
                <li>Dimensions: <strong>3 × 3</strong></li>
                <li>\\(a_{21}\\) is in row 2, column 1, which is <strong>2</strong></li>
            </ul>
        </div>
        """
    }
]
