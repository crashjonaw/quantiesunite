TITLE = "Applications: Real-World Uses of LSTMs and GRUs"

SECTIONS = [
    {
        "title": "NLP Applications: Text Processing and Understanding",
        "body": """<div class="concept-box">
<h3>Machine Translation</h3>
<p><strong>Encoder-Decoder Architecture:</strong></p>
<ul>
<li>Encoder LSTM reads source language sequence ("The cat sat")</li>
<li>Decoder LSTM generates target language output ("El gato se sentó") one word at a time</li>
<li>Attention mechanism allows decoder to focus on relevant encoder positions</li>
</ul>
<h3>Sentiment Analysis</h3>
<p>Input: "This movie was absolutely fantastic!"</p>
<p>BiLSTM processes entire text bidirectionally to capture context. The final hidden state is fed to a classifier:</p>
<p><strong>logits = W<sub>out</sub> [h<sub>T</sub><sup>(f)</sup> ; h<sub>1</sub><sup>(b)</sup>] + b</strong></p>
<p>BiLSTM captures emphasis ("absolutely") and sentiment words ("fantastic").</p>
<h3>Named Entity Recognition (NER)</h3>
<p><strong>BiLSTM-CRF architecture:</strong></p>
<ul>
<li>BiLSTM produces contextualized representations</li>
<li>CRF layer enforces valid tag sequences</li>
<li>Each word gets a tag based on bidirectional context</li>
</ul>
<h3>Text Classification</h3>
<p>Document → BiLSTM → embeddings → pooling (max/mean) → classifier</p>
<p>Applications: Spam detection, topic classification, chatbot intent detection</p>
</div>"""
    },
    {
        "title": "Time Series, Speech, and Video Applications",
        "body": """<div class="concept-box">
<h3>Speech Recognition</h3>
<p><strong>Architecture:</strong> Audio spectrogram → LSTM/GRU → phoneme probabilities</p>
<ul>
<li>Input: Log-mel filterbank features (10ms frames)</li>
<li>Output: Probability distribution over phonemes</li>
<li>Modern systems use CTC loss + language model rescoring</li>
</ul>
<p>Key challenge: Sequences are long (minutes of audio), requiring stable gradient flow.</p>
<h3>Time Series Forecasting</h3>
<p><strong>Many-to-one architecture:</strong> Past observations → LSTM → final hidden state → prediction</p>
<p><strong>Example - Stock Prediction:</strong></p>
<ul>
<li>Input: 60 days of closing prices</li>
<li>LSTM learns patterns: trends, seasonality, autocorrelation</li>
<li>Output: Next day's predicted price</li>
</ul>
<p>Challenge: Non-stationary data requires careful normalization and regularization.</p>
<h3>Activity Recognition (Videos)</h3>
<p><strong>CNN + LSTM pipeline:</strong></p>
<ul>
<li>CNN extracts spatial features from each frame</li>
<li>LSTM captures temporal dependencies across frames</li>
<li>Classification layer predicts action</li>
</ul>
<p>Why LSTM matters: "Picking up cup" vs "putting down cup" are visually similar but temporally opposite.</p>
</div>"""
    },
    {
        "title": "Biomedical and Gesture Recognition",
        "body": """<div class="concept-box">
<h3>Sleep Stage Classification</h3>
<p><strong>Input:</strong> EEG signals (brain electrical activity)</p>
<p><strong>Output:</strong> Sleep stage (Wake, N1, N2, N3, REM)</p>
<p>Temporal context is critical: isolated 5-second windows are ambiguous. LSTM learns that "after 30 min of N2 stage, deep sleep (N3) is likely".</p>
<p>Stacked BiLSTM models achieve 90%+ accuracy.</p>
<h3>Heart Arrhythmia Detection</h3>
<p><strong>Input:</strong> ECG time series | <strong>Output:</strong> Normal or arrhythmia</p>
<p>Key insight: Arrhythmias have temporal signatures (irregular patterns, repeated beats, gradual acceleration). LSTM captures these better than statistical models.</p>
<h3>Handwriting and Gesture Recognition</h3>
<p><strong>Input:</strong> Sequence of pen coordinates/velocities</p>
<p><strong>Output:</strong> Character or gesture label</p>
<p>BiLSTM advantages:</p>
<ul>
<li>Captures stroke patterns naturally</li>
<li>Handles variable-length sequences</li>
<li>Bidirectional context helps: future movements inform past letter identity</li>
</ul>
<h3>Protein Structure Prediction</h3>
<p><strong>Input:</strong> Amino acid sequence | <strong>Output:</strong> Secondary structure</p>
<p>BiLSTM captures long-range interactions (residues far apart can interact in 3D) and contextual information. Modern systems combine BiLSTM with attention and transformers.</p>
</div>"""
    },
    {
        "title": "Design Patterns and Implementation",
        "body": """<div class="worked-example">
<h3>Four Common RNN Design Patterns</h3>
<p><strong>Pattern 1: Many-to-One (Classification)</strong></p>
<p>Sequence → LSTM → final hidden state → classifier → label</p>
<p style="font-size: 0.9em; color: #aaa;">Examples: Sentiment, document classification, speaker identification</p>

<p><strong>Pattern 2: Many-to-Many (Tagging)</strong></p>
<p>Sequence → BiLSTM → classifier at each timestep → labels</p>
<p style="font-size: 0.9em; color: #aaa;">Examples: NER, POS tagging, frame-level classification</p>

<p><strong>Pattern 3: Many-to-Many (Seq2Seq)</strong></p>
<p>Input → Encoder LSTM → context → Decoder LSTM → output sequence</p>
<p style="font-size: 0.9em; color: #aaa;">Examples: Translation, summarization, speech recognition</p>

<p><strong>Pattern 4: Encoder-Decoder with Attention</strong></p>
<p>Encoder → Attention weights → Decoder → output conditioned on context</p>
<p style="font-size: 0.9em; color: #aaa;">Examples: Translation, VQA, image captioning</p>
</div>
<div class="concept-box">
<h3>Implementation Best Practices</h3>
<p><strong>Input Preparation:</strong></p>
<ul>
<li>Normalize features (z-score for time series)</li>
<li>Pad/truncate to fixed length</li>
<li>Embed categorical features</li>
</ul>
<p><strong>Training:</strong></p>
<ul>
<li>Use appropriate loss (cross-entropy for classification, MSE for regression)</li>
<li>Monitor gradient norms</li>
<li>Early stopping to prevent overfitting</li>
<li>BiLSTM requires full sequence at training time</li>
</ul>
<p><strong>Inference &amp; Deployment:</strong></p>
<ul>
<li>Single-direction LSTM: Real-time streaming</li>
<li>BiLSTM/stacked: Requires buffering</li>
<li>Quantization/pruning: Reduce model size</li>
</ul>
<div class="warning-box">
<p><strong>Common Pitfalls:</strong> Leaking future information • Ignoring sequence length variations • Insufficient regularization • Not normalizing inputs</p>
</div>
</div>"""
    }
]
