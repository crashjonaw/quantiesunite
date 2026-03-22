QUIZ = [
    {
        "question": "In self-attention, what does each position's query attend to?",
        "answer": "All positions in the sequence, including itself",
        "explanation": "Query from position i computes attention scores with all keys (all positions), then weighted averages values."
    },
    {
        "question": "Why can Transformers parallelize but RNNs can't?",
        "answer": "Transformer: all positions computed simultaneously (matrix ops). RNN: sequential (each step depends on previous hidden state)",
        "explanation": "RNN must compute h₁, then h₂, then h₃... sequentially. Transformer computes all in parallel."
    },
    {
        "question": "How does sinusoidal positional encoding work?",
        "answer": "Uses sin/cos functions at different frequencies: high dims change slowly (far positions), low dims change fast (near positions)",
        "explanation": "PE encodes position as signal with varying frequencies, generalizes to unseen lengths."
    },
    {
        "question": "What is causal masking in Transformer decoder?",
        "answer": "Prevents position t from attending to positions > t (future). Sets future scores to -∞ before softmax.",
        "explanation": "During language generation, can't see future tokens. Causal mask enforces this constraint."
    },
    {
        "question": "What is the main limitation of Transformers for very long sequences?",
        "answer": "O(n²) attention complexity: memory and computation become infeasible for large n",
        "explanation": "4K tokens: manageable. 64K tokens: 4 billion attention scores, runs out of memory."
    }
]
