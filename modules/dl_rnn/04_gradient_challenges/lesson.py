TITLE = "Vanishing and Exploding Gradients"

SECTIONS = [
    {
        "id": "vg_problem_intro",
        "title": "The Core Problem: Gradient Decay Through Time",
        "body": """
        <p >During BPTT, gradients are multiplied by \\(\\frac{\\partial h_t}{\\partial h_{t-1}}\\) at each step backwards in time:</p>
        <div class="concept-box">
            <p class="concept-box">
            $$\\frac{\\partial h_t}{\\partial h_{t-1}} = \\text{diag}(\\sigma'(\\ldots)) W_{hh}^T$$
            </p>
            <p >Chain rule: multiply this term for each step back in time.</p>
        </div>
        <p >If eigenvalues \\(< 1\\), gradient vanishes exponentially. If \\(> 1\\), it explodes.</p>
        """
    },
    {
        "id": "vg_vanishing",
        "title": "Vanishing Gradients: Long-Range Dependencies Forgotten",
        "body": """
        <div class="warning-box">
            <p class="concept-box">
            <strong>Problem:</strong> Gradient \\(\\propto (0.9)^T\\) over 100 steps \\(\\approx 2.7 \\times 10^{-5}\\) — nearly zero!
            </p>
        </div>
        <p ><strong>Effect:</strong> Early weights barely updated. Network cannot learn dependencies spanning many steps.</p>
        <p >Example: In a 100-word sentence, word 1 may not influence prediction of word 100.</p>
        """
    },
    {
        "id": "eg_exploding",
        "title": "Exploding Gradients: Training Instability",
        "body": """
        <div class="warning-box">
            <p class="concept-box">
            <strong>Problem:</strong> Gradient \\(\\propto (1.1)^T\\) over 100 steps \\(\\approx 13,780\\) — massive!
            </p>
        </div>
        <p ><strong>Effect:</strong> Large weight updates → NaN values → training collapse.</p>
        <p >Loss spikes unpredictably. Network oscillates wildly.</p>
        """
    },
    {
        "id": "vg_solutions",
        "title": "Solutions: GRU, LSTM, and Gradient Clipping",
        "body": """
        <p ><strong>1. Gated Architectures (LSTM, GRU):</strong></p>
        <ul >
            <li>Gates control information flow, multiplicative factor ≈ 1</li>
            <li>Enables learning of long-range dependencies</li>
        </ul>
        <p ><strong>2. Gradient Clipping:</strong></p>
        <div class="success-box">
            <p class="concept-box">
            $$\\nabla W \\leftarrow \\begin{cases} \\nabla W & \\text{if} \\|\\nabla W\\| \\leq \\theta \\\\ \\theta \\frac{\\nabla W}{\\|\\nabla W\\|} & \\text{otherwise} \\end{cases}$$
            </p>
            <p >Prevents explosions without killing learning signal.</p>
        </div>
        <p ><strong>3. Better Initialization:</strong> Orthogonal init for \\(W_{hh}\\) helps.</p>
        """
    }
]
