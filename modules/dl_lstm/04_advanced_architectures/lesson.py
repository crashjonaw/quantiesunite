TITLE = "Advanced Architectures: Bidirectional and Stacked LSTMs/GRUs"

SECTIONS = [
    {
        "title": "Bidirectional RNNs and BiLSTM",
        "body": """<div class="concept-box">
<h3>The Limitation of Single-Direction Processing</h3>
<p>Standard RNNs (and LSTMs) process sequences left to right, using only past context. However, future context is often equally important.</p>
<p><strong>Example: Part-of-speech tagging</strong></p>
<p style="font-style: italic;">"The bank approved the loan"</p>
<p>When labeling "bank", knowing that "loan" comes next suggests "bank" is a financial institution, not a riverbank.</p>
<h3>Bidirectional Architecture</h3>
<p>A <strong>bidirectional RNN</strong> runs two independent networks:</p>
<ol>
<li><strong>Forward RNN</strong>: Process left → right, producing h<sub>t</sub><sup>(f)</sup></li>
<li><strong>Backward RNN</strong>: Process right ← left, producing h<sub>t</sub><sup>(b)</sup></li>
</ol>
<p>Final representation concatenates both:</p>
<p><strong>h<sub>t</sub> = [h<sub>t</sub><sup>(f)</sup> ; h<sub>t</sub><sup>(b)</sup>]</strong></p>
<h3>BiLSTM Advantages and Trade-offs</h3>
<div class="success-box">
<p><strong>Advantages:</strong> Access to past and future context, better representations, superior performance on tagging/parsing/translation</p>
</div>
<div class="warning-box">
<p><strong>Disadvantages:</strong> Requires full sequence in memory (no streaming), 2x parameters, backward pass latency</p>
</div>
</div>"""
    },
    {
        "title": "Stacked LSTMs: Building Depth",
        "body": """<div class="concept-box">
<h3>Why Stack Layers?</h3>
<p>A single LSTM layer may be limited in expressiveness. <strong>Stacking</strong> multiple LSTM layers increases representational capacity:</p>
<p><strong>Layer 1:</strong> h<sub>t</sub><sup>(1)</sup> = LSTM<sub>1</sub>(x<sub>t</sub>, h<sub>t-1</sub><sup>(1)</sup>)</p>
<p><strong>Layer 2:</strong> h<sub>t</sub><sup>(2)</sup> = LSTM<sub>2</sub>(h<sub>t</sub><sup>(1)</sup>, h<sub>t-1</sub><sup>(2)</sup>)</p>
<p><strong>Layer 3:</strong> h<sub>t</sub><sup>(3)</sup> = LSTM<sub>3</sub>(h<sub>t</sub><sup>(2)</sup>, h<sub>t-1</sub><sup>(3)</sup>)</p>
<p><strong>Output:</strong> y<sub>t</sub> = W<sub>out</sub> h<sub>t</sub><sup>(L)</sup> + b<sub>out</sub></p>
<h3>Hierarchical Feature Learning</h3>
<ul>
<li><strong>Layer 1</strong> learns low-level patterns (phoneme transitions, word order)</li>
<li><strong>Layer 2</strong> learns higher-level patterns (syntax, phrase structure)</li>
<li><strong>Layer 3+</strong> learn abstract patterns (semantics, discourse)</li>
</ul>
</div>
<div class="worked-example">
<h3>Design Choices</h3>
<ul>
<li><strong>Number of layers:</strong> Typically 2-4 for most tasks; 8+ for very complex problems</li>
<li><strong>Hidden size:</strong> Can vary; often constant across layers</li>
<li><strong>Residual connections:</strong> Add h<sub>t</sub><sup>(i-1)</sup> to h<sub>t</sub><sup>(i)</sup> to ease gradient flow (recommended for deep stacks)</li>
<li><strong>Dropout:</strong> Applied between layers to prevent overfitting</li>
</ul>
</div>"""
    },
    {
        "title": "Combining BiLSTM and Stacking",
        "body": """<div class="concept-box">
<h3>Maximum Expressiveness: Stacked BiLSTM</h3>
<p>For the most powerful architecture, stack bidirectional LSTMs:</p>
<pre style=" padding: 12px; border-radius: 4px; font-size: 12px;">
Input x_t
  ↓
[BiLSTM Layer 1] → [Dropout] → h_t^(1)
  ↓
[BiLSTM Layer 2] → [Dropout] → h_t^(2)
  ↓
[BiLSTM Layer 3] → [Dropout] → h_t^(3)
  ↓
Output layer → predictions
</pre>
<p>Each layer is bidirectional, producing concatenated forward/backward states.</p>
<h3>Example: 2-Layer BiLSTM</h3>
<p><strong>Configuration:</strong> Hidden size 128 per direction</p>
<ul>
<li><strong>Layer 1 output:</strong> 256 features (128 fwd + 128 bwd)</li>
<li><strong>Layer 2 input:</strong> 256 features</li>
<li><strong>Layer 2 output:</strong> 256 features</li>
<li><strong>Total parameters:</strong> ≈ 2 × (3 LSTM gates × 256 × 256 weights)</li>
</ul>
</div>"""
    },
    {
        "title": "Variants and Practical Design",
        "body": """<div class="concept-box">
<h3>LSTM Variants</h3>
<p><strong>Peephole LSTM:</strong> Gates can peek at cell state for finer control (adds parameters)</p>
<p><strong>Coupled Input-Forget Gate:</strong> Merge gates to reduce parameters (i<sub>t</sub> + f<sub>t</sub> = 1)</p>
<p><strong>Recurrent Dropout:</strong> Apply dropout to hidden-to-hidden connections to prevent overfitting</p>
</div>
<div class="worked-example">
<h3>Best Practices for Stacked RNNs</h3>
<ol>
<li><strong>Start simple:</strong> Single layer LSTM/GRU often suffices</li>
<li><strong>Add layers if needed:</strong> Increase depth if validation error plateaus</li>
<li><strong>Regularization is crucial:</strong> Use dropout and weight decay</li>
<li><strong>Bidirectional only for offline tasks:</strong> Not suitable for real-time prediction</li>
<li><strong>Monitor gradient flow:</strong> Use layer normalization or residual connections in deep stacks</li>
<li><strong>Understand trade-offs:</strong> Bidirectional doubles parameters; stacking scales quadratically</li>
</ol>
</div>"""
    }
]
