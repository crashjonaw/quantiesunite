TITLE = "Kernel and Image"

SECTIONS = [
    {
        "title": "Kernel (Null Space)",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> For a linear transformation T: V → W, the kernel is:</p>
        <pre class='code-block'>ker(T) = {v ∈ V : T(v) = 0}</pre>

        <p><strong>Key fact:</strong> The kernel is a subspace of V.</p>

        <p><strong>Intuition:</strong> The kernel consists of all input vectors that map to the zero vector. It represents the "information lost" by the transformation.</p>
        </div>
        """
    },
    {
        "title": "Image (Range)",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> The image of T is:</p>
        <pre class='code-block'>im(T) = {w ∈ W : w = T(v) for some v ∈ V}</pre>

        <p><strong>Key fact:</strong> The image is a subspace of W.</p>

        <p><strong>Intuition:</strong> The image is the set of all possible output values. It represents what the transformation can "reach".</p>
        </div>
        """
    },
    {
        "title": "Connection to Matrices",
        "body": """
        <div class='concept-box'>
        <p><strong>For matrix transformations T(x) = Ax where A is m × n:</strong></p>
        <ul>
        <li>ker(T) = null space of A = {x : Ax = 0}</li>
        <li>im(T) = column space of A = span of columns of A</li>
        <li>rank(T) = dim(im(T)) = rank(A)</li>
        <li>nullity(T) = dim(ker(T)) = nullity(A)</li>
        </ul>
        </div>

        <div class='success-box'>
        <p><strong>Rank-Nullity Theorem:</strong> For a linear transformation T: V → W where V is finite-dimensional:</p>
        <pre class='code-block'>rank(T) + nullity(T) = dim(V)</pre>

        <p>This is a fundamental theorem relating the dimensions of the kernel and image. It says there's a trade-off: a larger kernel means a smaller image.</p>
        </div>
        """
    },
    {
        "title": "Worked Example",
        "body": """
        <div class='worked-example'>
        <p><strong>Example: Find kernel and image of T(x, y) = (x + y, 2x + 2y)</strong></p>
        <pre class='code-block'>Matrix representation: A = [1  1]
                           [2  2]

Kernel: Solve Ax = 0
[1  1][x] = [0]
[2  2][y]   [0]

From row 1: x + y = 0 → x = -y. Free variable y = t.
General solution: x = t[-1, 1]ᵀ
ker(T) = span{[-1, 1]}, dim(ker(T)) = 1 (nullity = 1)

Image: Rank(A) = 1 (one independent column since row 2 = 2·row 1)
im(T) = span{column 1} = span{[1, 2]ᵀ}
dim(im(T)) = 1 (rank = 1)

Verify rank-nullity: rank + nullity = 1 + 1 = 2 = dim(ℝ²) ✓</pre>
        </div>

        <div class='concept-box'>
        <p><strong>Injectivity and surjectivity:</strong></p>
        <ul>
        <li><strong>Injective (one-to-one):</strong> T is injective ⟺ ker(T) = {0} ⟺ rank(T) = dim(V)</li>
        <li><strong>Surjective (onto):</strong> T is surjective ⟺ im(T) = W ⟺ rank(T) = dim(W)</li>
        <li><strong>Bijective (isomorphism):</strong> T is bijective ⟺ T is injective and surjective ⟺ rank(T) = dim(V) = dim(W)</li>
        </ul>
        </div>
        """
    }
]
