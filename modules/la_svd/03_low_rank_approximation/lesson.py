TITLE = "Low-Rank Approximation"

SECTIONS = [
    {
        "title": "Truncating the SVD for Compression",
        "body": """
        <p><strong>Key observation:</strong> Since $\\sigma_1 \\geq \\sigma_2 \\geq \\cdots \\geq \\sigma_r$, the first singular values dominate. Keeping only the largest $k$ values gives a rank-$k$ approximation:</p>
        <p>$$A_k = \\sum_{j=1}^{k} \\sigma_j \\mathbf{u}_j \\mathbf{v}_j^T$$</p>

        <p>This is much simpler: instead of storing the full $m \\times n$ matrix, we store:</p>
        <ul>
        <li>$k$ singular values: $k$ numbers</li>
        <li>First $k$ columns of $U$: $km$ numbers</li>
        <li>First $k$ columns of $V$: $kn$ numbers</li>
        <li><strong>Total:</strong> $k(m + n + 1)$ numbers instead of $mn$</li>
        </ul>

        <p><strong>Eckart-Young Theorem:</strong> Among all rank-$k$ matrices, $A_k$ (truncated SVD) minimizes the distance to $A$:</p>
        <p>$$\\min_{\\text{rank}(B) \\leq k} \\|A - B\\| = \\|A - A_k\\| = \\sigma_{k+1}$$</p>

        <p>This proves SVD gives the optimal low-rank approximation in any spectral norm (and Frobenius norm).</p>

        <div class='concept-box'>
        <p><strong>Approximation error:</strong></p>
        <p>$$\\|A - A_k\\|_F = \\sqrt{\\sigma_{k+1}^2 + \\sigma_{k+2}^2 + \\cdots + \\sigma_r^2}$$</p>
        <p>The error depends only on the discarded singular values.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Compression savings</strong></p>
        <pre class='code-block'>Full matrix $A$ ($m \\times n$): $mn$ numbers
Rank-$k$ approximation $A_k$: $k(m + n + 1)$ numbers

For $m = n = 1000$ (1M numbers):
$k=1$:   $1(1000 + 1000 + 1) = 2{,}001$ numbers (0.2% storage)
$k=10$:  $10(1000 + 1000 + 1) = 20{,}010$ numbers (2% storage)
$k=50$:  $50(1000 + 1000 + 1) = 100{,}050$ numbers (10% storage)
$k=100$: $100(1000 + 1000 + 1) = 200{,}100$ numbers (20% storage)

For $m = 4000$, $n = 3000$ (12M numbers, typical image):
$k=100$: $100(4000 + 3000 + 1) = 700{,}100$ numbers (5.8% storage)</pre>
        </div>
        """
    },
    {
        "title": "Applications of Low-Rank Approximation",
        "body": """
        <p><strong>Image compression:</strong> Store only the first $k$ singular values and vectors, which saves dramatic amounts of space while preserving most visual information.</p>

        <p><strong>Noise reduction:</strong> In noisy data, true signal dominates large singular values while noise spreads across all. Truncating small singular values removes noise:</p>
        <ul>
        <li>Noisy signal = true signal + noise</li>
        <li>True structure appears in dominant singular values</li>
        <li>Truncate small singular values (mostly noise)</li>
        <li>Reconstruct from low-rank approximation = denoised signal</li>
        </ul>

        <p><strong>Dimensionality reduction:</strong> Project high-dimensional data onto first $k$ principal directions defined by $V$, reducing dimensionality from $n$ to $k$ while retaining most variance.</p>

        <p><strong>Matrix completion:</strong> Given a matrix with missing entries, SVD can infer them using the assumption that the data has low-rank structure.</p>

        <div class='worked-example'>
        <p><strong>Example: Image compression conceptually</strong></p>
        <pre class='code-block'>High-resolution image: $4000 \\times 3000$ pixels = 12 million numbers

SVD reveals:
$\\sigma_1 = 1000$, $\\sigma_2 = 800$, $\\sigma_3 = 600$, ..., $\\sigma_{100} = 50$

Cumulative explained variance:
$\\sum_{i=1}^{100} \\sigma_i^2 \\;/\\; \\sum_{\\text{all}} \\sigma_i^2 \\approx 95\\%$

Compressed representation:
100 singular values + 4000 components of $U$ + 3000 components of $V$
$= 100 + 4000 + 3000 = 7{,}100$ numbers

Compression ratio: $12{,}000{,}000 / 7{,}100 \\approx 1{,}700\\times$
With only 5% information loss!</pre>
        </div>

        <p><strong>Data quality metric:</strong> The decay of singular values indicates data structure. Steep decay ($\\sigma_1 \\gg \\sigma_2 \\gg \\cdots$) means low-rank approximation works well. Slow decay means data is high-rank and compression is less effective.</p>

        <div class='success-box'>
        <p><strong>Why truncated SVD works:</strong> For real-world data (images, text, sensor readings), the true underlying structure is typically much lower-rank than apparent. The large singular values capture structure; small ones are noise or redundancy. Truncation removes the noise/redundancy while preserving essential information.</p>
        </div>
        """
    }
]
