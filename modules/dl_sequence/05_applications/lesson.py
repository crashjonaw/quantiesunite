TITLE = "Applications: Translation, Summarization, and Beyond"

SECTIONS = [
    {
        "id": "machine_translation",
        "title": "Machine Translation: Bridging Languages",
        "body": "<p>Translate text from source language to target language. Encoder-decoder processes source tokens \\((x_1, \\ldots, x_T)\\) and generates target tokens \\((y_1, \\ldots, y_M)\\).</p><p>Key challenges: word order differences, morphological variations, rare words (handled via subword tokenization like BPE). Evaluation uses BLEU score, measuring n-gram overlap with reference translations.</p><p>Modern systems use Transformer models with beam search and length normalization for higher-quality outputs.</p>"
    },
    {
        "id": "text_summarization",
        "title": "Text Summarization: Distilling Key Information",
        "body": "<p>Abstractive summarization uses seq2seq to generate concise summaries. The encoder reads the full document; the decoder generates a condensed version.</p><p>Extractive summarization selects important sentences from the original text, often via attention weights or scoring functions.</p><p>Challenges: capturing essential information, avoiding redundancy, evaluating quality (ROUGE metrics measure overlap). Lead-3 baseline (first 3 sentences) is surprisingly strong for news articles.</p>"
    },
    {
        "id": "speech_and_audio",
        "title": "Speech Recognition and Audio-to-Text",
        "body": "<p>Convert audio spectrograms to text sequences. The encoder processes acoustic frames; the decoder generates character or subword sequences.</p><p>Connectionist Temporal Classification (CTC) loss aligns variable-length audio to text without explicit phoneme boundaries. CTC marginalizes over all possible alignments.</p><p>Modern systems use attention-based RNNs or Transformers directly on log-mel spectrograms, often trained with CTC or attention-based losses.</p>"
    },
    {
        "id": "dialogue_and_qa",
        "title": "Question Answering and Dialogue Systems",
        "body": "<p>For QA, the encoder reads context and question; the decoder generates an answer. Multi-turn dialogue requires tracking conversation history, often via hierarchical encoding.</p><p>Seq2seq models can pointer-generator networks: mix copying tokens from the input (via attention) and generating from vocabulary. This is useful when answers overlap with context.</p><p>Challenges: ensuring factual correctness, handling out-of-domain questions, avoiding generic responses in dialogue. Reinforcement learning (e.g., RLHF) fine-tunes models for better human preferences.</p>"
    }
]
