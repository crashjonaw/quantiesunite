TITLE = "LSTM Cell Architecture: Gates and Memory"

SECTIONS = [
    {
        "title": "LSTM Overview: States and Gates",
        "body": """<div class="concept-box">
<h3>Two Key State Variables</h3>
<p>An LSTM (Long Short-Term Memory) cell maintains two state vectors:</p>
<ul>
<li><strong>Cell state c<sub>t</sub></strong>: Memory buffer that changes slowly via addition</li>
<li><strong>Hidden state h<sub>t</sub></strong>: Output passed to next step and to prediction layers</li>
</ul>
<h3>Three Control Gates</h3>
<p>The cell is controlled by three gates that determine information flow:</p>
<ul>
<li><strong>Forget gate f<sub>t</sub></strong>: Decides what to remove from memory</li>
<li><strong>Input gate i<sub>t</sub></strong>: Decides what new information to add</li>
<li><strong>Output gate o<sub>t</sub></strong>: Decides what to expose to the next layer</li>
</ul>
<p>Each gate is a neural network layer that produces values between 0 and 1, allowing the LSTM to learn which information to keep, discard, or output.</p>
</div>"""
    },
    {
        "title": "The Forget and Input Gates",
        "body": """<div class="concept-box">
<h3>The Forget Gate: Controlling Memory Retention</h3>
<p>The forget gate determines how much of the previous cell state to retain:</p>
<p><strong>f<sub>t</sub> = σ(W<sub>f</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>f</sub>)</strong></p>
<p>where σ is the sigmoid function (output in [0, 1]).</p>
<p><strong>Interpretation:</strong></p>
<ul>
<li>f<sub>t</sub> ≈ 0 means "forget" — the cell state is reset</li>
<li>f<sub>t</sub> ≈ 1 means "remember" — the cell state passes through unchanged</li>
</ul>
<p>The gate output is applied multiplicatively: <strong>forget = f<sub>t</sub> ⊙ c<sub>t-1</sub></strong></p>
</div>
<div class="concept-box">
<h3>The Input Gate: Adding New Information</h3>
<p>The input gate controls what new information enters the cell state:</p>
<p><strong>i<sub>t</sub> = σ(W<sub>i</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>i</sub>)</strong></p>
<p>Separately, we compute a <strong>candidate value</strong> (proposed new memory):</p>
<p><strong>c̃<sub>t</sub> = tanh(W<sub>c</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>c</sub>)</strong></p>
<p>The input gate scales this candidate before adding to cell state:</p>
<p><strong>input = i<sub>t</sub> ⊙ c̃<sub>t</sub></strong></p>
</div>"""
    },
    {
        "title": "Cell State Update and Output Gate",
        "body": """<div class="concept-box">
<h3>Cell State: The Core of LSTM</h3>
<p>The cell state is updated by combining forget and input contributions via <strong>addition</strong>:</p>
<p><strong>c<sub>t</sub> = f<sub>t</sub> ⊙ c<sub>t-1</sub> + i<sub>t</sub> ⊙ c̃<sub>t</sub></strong></p>
<p>This additive path is why LSTM solves the vanishing gradient problem. Gradients flow backward through addition without exponential decay.</p>
<h3>The Output Gate: Exposing Memory</h3>
<p>The output gate determines what portion of the cell state to expose:</p>
<p><strong>o<sub>t</sub> = σ(W<sub>o</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>o</sub>)</strong></p>
<p>The hidden state is computed by scaling a tanh-normalized cell state:</p>
<p><strong>h<sub>t</sub> = o<sub>t</sub> ⊙ tanh(c<sub>t</sub>)</strong></p>
<p>The hidden state h<sub>t</sub> is passed to the next time step and to output layers for predictions.</p>
</div>"""
    },
    {
        "title": "Complete Equations and Intuition",
        "body": """<div class="concept-box">
<h3>All LSTM Equations</h3>
<p>An LSTM cell at time t computes:</p>
<ul style="font-family: monospace;">
<li>f<sub>t</sub> = σ(W<sub>f</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>f</sub>)</li>
<li>i<sub>t</sub> = σ(W<sub>i</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>i</sub>)</li>
<li>c̃<sub>t</sub> = tanh(W<sub>c</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>c</sub>)</li>
<li>o<sub>t</sub> = σ(W<sub>o</sub> [h<sub>t-1</sub>, x<sub>t</sub>] + b<sub>o</sub>)</li>
<li>c<sub>t</sub> = f<sub>t</sub> ⊙ c<sub>t-1</sub> + i<sub>t</sub> ⊙ c̃<sub>t</sub></li>
<li>h<sub>t</sub> = o<sub>t</sub> ⊙ tanh(c<sub>t</sub>)</li>
</ul>
<p>All weight matrices and biases are learned parameters. Hidden and cell states are initialized to zero.</p>
</div>
<div class="worked-example">
<h3>Thinking of LSTM as a Data Structure</h3>
<ul>
<li><strong>c<sub>t</sub> (cell state)</strong>: The "memory bank" that can be selectively modified</li>
<li><strong>Forget gate</strong>: "Should I delete this memory?"</li>
<li><strong>Input gate</strong>: "Should I write this new value to memory?"</li>
<li><strong>Output gate</strong>: "Should I expose this memory to the network?"</li>
</ul>
<p>Different gates learn different temporal dependencies. Early in training, gates act neutrally; over time, they specialize to capture relevant patterns in the data.</p>
</div>"""
    }
]
