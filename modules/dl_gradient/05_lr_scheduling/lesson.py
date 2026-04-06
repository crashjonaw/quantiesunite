TITLE = "Learning Rate Scheduling"

SECTIONS = [
    {
        "id": "fixed_lr_limitations",
        "title": "Limitations of Fixed Learning Rate",
        "body": """
        <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Problem:</strong> A single learning rate often isn't optimal throughout training.</p>
            <ul >
                <li><strong>Early training:</strong> Large steps needed to escape plateau near initialization</li>
                <li><strong>Late training:</strong> Small steps needed to fine-tune and avoid overshooting minima</li>
                <li><strong>Oscillations:</strong> Fixed \(\alpha\) can cause bouncing in steep regions</li>
            </ul>
            <p><strong>Solution:</strong> Schedule (reduce) the learning rate over time.</p>
        </div>
        """
    },
    {
        "id": "step_decay",
        "title": "Step Decay Scheduling",
        "body": """
        <div class="worked-example" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Step decay:</strong> Reduce learning rate by a fixed factor every N epochs.</p>
            <p>$$\\alpha_t = \\alpha_0 \\cdot \\gamma^{\\lfloor t / S \\rfloor}$$</p>
            <p>where \(\gamma \approx 0.5\) or \(0.1\) (multiplicative factor), \(S\) = epochs between reductions.</p>
            <p><strong>Example:</strong></p>
            <ul >
                <li>Epochs 0-9: \(\alpha = 0.1\)</li>
                <li>Epochs 10-19: \(\alpha = 0.01\) (divide by 10)</li>
                <li>Epochs 20-29: \(\alpha = 0.001\) (divide by 10 again)</li>
            </ul>
            <p><strong>Typical choice:</strong> Reduce by 10× every 10-30 epochs. Simple and effective.</p>
        </div>
        """
    },
    {
        "id": "exponential_decay",
        "title": "Exponential and Linear Decay",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Exponential decay:</strong> Smooth, continuous reduction.</p>
            <p>$$\\alpha_t = \\alpha_0 e^{-\\lambda t}$$</p>
            <p>where \(\lambda\) controls decay rate, \(t\) is epoch or iteration count.</p>
            <p><strong>Linear decay:</strong> Reduce linearly from \(\alpha_0\) to ~0.</p>
            <p>$$\\alpha_t = \\alpha_0 \\left(1 - \\frac{t}{T}\\right)$$</p>
            <p>where T is total number of iterations.</p>
            <p><strong>Use case:</strong> Exponential when you have many epochs. Linear when total iterations are known (e.g., fixed budget).</p>
        </div>
        """
    },
    {
        "id": "warmup_cosine",
        "title": "Learning Rate Warmup and Cosine Annealing",
        "body": """
        <div class="success-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Warmup:</strong> Start with \(\alpha = 0\), linearly increase to \(\alpha_0\) over first few epochs/iterations.</p>
            <p><strong>Why:</strong> Prevents instability at initialization. Common in transformers and large-batch training.</p>
            <p><strong>Cosine annealing:</strong> Learning rate follows cosine curve from \(\alpha_0\) to ~0.</p>
            <p>$$\\alpha_t = \\frac{\\alpha_0}{2} \\left(1 + \\cos\\left(\\frac{\\pi t}{T}\\right)\\right)$$</p>
            <p><strong>Benefit:</strong> Smooth decay. Often leads to better final loss than abrupt step decay.</p>
            <p><strong>Modern approach:</strong> Combine warmup + cosine annealing for robust convergence. Popular in computer vision and NLP.</p>
        </div>
        """
    }
]
