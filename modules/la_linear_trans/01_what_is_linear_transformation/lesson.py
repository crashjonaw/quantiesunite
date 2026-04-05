TITLE = "What is a Linear Transformation?"

SECTIONS = [
    {
        "title": "Definition and Properties of Linear Transformations",
        "body": """
        <div class='concept-box'>
        <p><strong>Linear Transformation:</strong> A function $T: V \\to W$ between vector spaces is a linear transformation (or linear map) if:</p>
        <ol>
        <li><strong>Additivity:</strong> $T(\\mathbf{u} + \\mathbf{v}) = T(\\mathbf{u}) + T(\\mathbf{v})$ for all $\\mathbf{u}, \\mathbf{v} \\in V$</li>
        <li><strong>Homogeneity:</strong> $T(c\\mathbf{v}) = cT(\\mathbf{v})$ for all $c \\in F$ and $\\mathbf{v} \\in V$</li>
        </ol>

        <p>These conditions are equivalent to: $T(c\\mathbf{u} + d\\mathbf{v}) = cT(\\mathbf{u}) + dT(\\mathbf{v})$ for all $\\mathbf{u}, \\mathbf{v} \\in V$ and $c, d \\in F$ (preserves linear combinations).</p>
        </div>

        <h3>Examples of Linear Transformations</h3>
        <ul>
        <li><strong>Matrix multiplication:</strong> $T(\\mathbf{x}) = A\\mathbf{x}$ (from $\\mathbb{R}^n$ to $\\mathbb{R}^m$)</li>
        <li><strong>Projection:</strong> $T(\\mathbf{x}) = \\text{proj}_W(\\mathbf{x})$ (orthogonal projection onto a subspace $W$)</li>
        <li><strong>Differentiation:</strong> $T(p) = p'$ (from $P_n(\\mathbb{R})$ to $P_{n-1}(\\mathbb{R})$)</li>
        <li><strong>Integration:</strong> $T(f) = \\int f(x)\\,dx$ (from $C(\\mathbb{R})$ to $\\mathbb{R}$)</li>
        <li><strong>Rotation:</strong> $T(\\mathbf{v}) = R_\\theta \\mathbf{v}$ (rotation in the plane by angle $\\theta$)</li>
        <li><strong>Reflection:</strong> $T(\\mathbf{v})$ = reflection of $\\mathbf{v}$ across a line/plane</li>
        </ul>
        """
    },
    {
        "title": "Key Properties",
        "body": """
        <div class='concept-box'>
        <ul>
        <li>$T(\\mathbf{0}) = \\mathbf{0}$ (zero vector maps to zero vector)</li>
        <li>$T(-\\mathbf{v}) = -T(\\mathbf{v})$</li>
        <li>Composition of linear transformations is linear: If $T: U \\to V$ and $S: V \\to W$ are linear, then $S \\circ T: U \\to W$ is linear</li>
        <li>Inverse of a bijective linear transformation is linear</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Verification Example",
        "body": """
        <div class='worked-example'>
        <p><strong>Example: Verify $T(x, y) = (2x - y, x + y)$ is linear</strong></p>
        <pre class='code-block'>Additivity: $T((x_1, y_1) + (x_2, y_2)) = T((x_1+x_2, y_1+y_2))$
   $= (2(x_1+x_2) - (y_1+y_2), (x_1+x_2) + (y_1+y_2))$
   $= (2x_1 - y_1 + 2x_2 - y_2, x_1 + y_1 + x_2 + y_2)$
   $= (2x_1 - y_1, x_1 + y_1) + (2x_2 - y_2, x_2 + y_2)$
   $= T(x_1, y_1) + T(x_2, y_2)$ ✓

Homogeneity: $T(c(x, y)) = T((cx, cy))$
   $= (2cx - cy, cx + cy)$
   $= c(2x - y, x + y)$
   $= cT(x, y)$ ✓

$T$ is linear.</pre>
        </div>
        """
    },
    {
        "title": "Non-linear Examples (Counterexamples)",
        "body": """
        <div class='warning-box'>
        <p><strong>Important:</strong> These are NOT linear transformations:</p>
        <ul>
        <li>$T(x, y) = (x^2, y)$ is not linear (not additive: $T(1,0) + T(1,0) = 2$ but $T(2,0) = 4$)</li>
        <li>$T(x) = x + 1$ is not linear ($T(0) = 1 \\neq 0$)</li>
        <li>$T(x, y) = (x + y, xy)$ is not linear (not homogeneous)</li>
        </ul>
        </div>
        """
    }
]
