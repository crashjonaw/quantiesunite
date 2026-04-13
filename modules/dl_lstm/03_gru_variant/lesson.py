TITLE = "GRU: A Simpler Variant of LSTM"

SECTIONS = [
    {
        "title": "Motivation for GRU",
        "body": """<div class="concept-box">
<h3>LSTM's Computational Cost</h3>
<p>LSTM cells are effective but computationally expensive:</p>
<ul>
<li><strong>3 gates</strong>: Forget gate + Input gate + Output gate</li>
<li><strong>4 computations per step</strong>: 3 sigmoid + 1 tanh</li>
<li><strong>4 weight matrices</strong> (for typical architecture)</li>
</ul>
<h3>The GRU Solution</h3>
<p>In 2014, Cho et al. proposed the <strong>Gated Recurrent Unit (GRU)</strong> as a simplified alternative:</p>
<ul>
<li>Only <strong>2 gates</strong>: Reset and Update</li>
<li><strong>Merge</strong> cell state and hidden state into one vector</li>
<li><strong>Reduce</strong> parameters and computation while maintaining performance</li>
</ul>
<p>GRU achieves similar performance to LSTM with ~25% fewer parameters, making it attractive for resource-constrained applications.</p>
</div>"""
    },
    {
        "title": "GRU Equations: Reset, Update, and Candidate",
        "body": """<div class="concept-box">
<h3>Reset Gate: Selective Context</h3>
<p>The reset gate determines how much of the previous hidden state to use when computing a candidate:</p>
<p><strong>r<sub>t</sub> = \(\\sigma\)(W<sub>r</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>r</sub>)</strong></p>
<p>If r<sub>t</sub> ≈ 0, the cell "forgets" the previous context and focuses on new input.</p>
<h3>Update Gate: Mixing Old and New</h3>
<p>The update gate determines how much of the previous hidden state to retain versus replace:</p>
<p><strong>z<sub>t</sub> = \(\\sigma\)(W<sub>z</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>z</sub>)</strong></p>
<p>If z<sub>t</sub> ≈ 0, the hidden state remains mostly unchanged. If z<sub>t</sub> ≈ 1, it's fully replaced.</p>
<h3>Candidate Hidden State</h3>
<p>Notice the reset gate is applied <strong>before</strong> the weight multiplication:</p>
<p><strong>h̃<sub>t</sub> = tanh(W<sub>h</sub> [r<sub>t</sub> ⊙ h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>h</sub>)</strong></p>
<p>This allows the cell to "reset" its context when computing new information.</p>
</div>"""
    },
    {
        "title": "Final Hidden State and Gradient Flow",
        "body": """<div class="concept-box">
<h3>Linear Interpolation: Combining Old and New</h3>
<p>The final hidden state is a linear combination of previous and candidate states:</p>
<p><strong>h<sub>t</sub> = (1 - z<sub>t</sub>) ⊙ h<sub>t-1</sub> + z<sub>t</sub> ⊙ h̃<sub>t</sub></strong></p>
<p>This is a <strong>linear interpolation</strong>:</p>
<ul>
<li>If z<sub>t</sub> ≈ 0: Keep previous state (update gate "off")</li>
<li>If z<sub>t</sub> ≈ 1: Fully adopt candidate state (update gate "on")</li>
</ul>
<h3>Preserving Gradient Flow</h3>
<p>Like LSTM, GRU preserves gradient flow via its additive update mechanism. The gradient with respect to h<sub>t-1</sub> includes a direct path:</p>
<p><strong>∂h<sub>t</sub>/∂h<sub>t-1</sub> = (1 - z<sub>t</sub>) + (terms from h̃<sub>t</sub>)</strong></p>
<p>When the update gate is small, (1 - z<sub>t</sub>) ≈ 1, allowing gradients to propagate directly backward. This gives GRU similar vanishing gradient benefits as LSTM with fewer parameters.</p>
</div>"""
    },
    {
        "title": "GRU vs LSTM: Comparison and Practical Use",
        "body": """<div class="concept-box">
<h3>Feature Comparison</h3>
<table style="width: 100%; border-collapse: collapse;">
<tr style="border-bottom: 1px solid #444;">
<th style="padding: 8px; text-align: left;">Aspect</th><th style="padding: 8px; text-align: left;">LSTM</th><th style="padding: 8px; text-align: left;">GRU</th>
</tr>
<tr style="border-bottom: 1px solid #333;">
<td style="padding: 8px;">Number of gates</td><td style="padding: 8px;">3</td><td style="padding: 8px;">2</td>
</tr>
<tr style="border-bottom: 1px solid #333;">
<td style="padding: 8px;">Hidden vectors</td><td style="padding: 8px;">2 (h, c)</td><td style="padding: 8px;">1 (h)</td>
</tr>
<tr style="border-bottom: 1px solid #333;">
<td style="padding: 8px;">Parameters</td><td style="padding: 8px;">~4x input size</td><td style="padding: 8px;">~3x input size</td>
</tr>
<tr style="border-bottom: 1px solid #333;">
<td style="padding: 8px;">Computation</td><td style="padding: 8px;">More complex</td><td style="padding: 8px;">Simpler</td>
</tr>
</table>
</div>
<div class="worked-example">
<h3>When to Use Each</h3>
<p><strong>Use GRU when:</strong></p>
<ul>
<li>Computational efficiency is critical (mobile, embedded)</li>
<li>Dataset is moderate size</li>
<li>Training speed matters</li>
</ul>
<p><strong>Use LSTM when:</strong></p>
<ul>
<li>Abundant computational resources available</li>
<li>Problem requires very long-term dependencies</li>
<li>Interpretability of three gates is valuable</li>
</ul>
<p>In practice, both work well for most sequence tasks. GRU is increasingly popular due to lower overhead and faster training.</p>
</div>"""
    }
]
