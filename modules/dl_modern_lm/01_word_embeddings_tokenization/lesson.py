TITLE = "Word Embeddings and Tokenization"

SECTIONS = [
    {
        "title": "What are Word Embeddings?",
        "body": """Word embeddings map words to dense vectors in continuous space. They capture semantic relationships: similar words have similar vectors, and vector arithmetic reveals meaning.

Classical approach: one-hot encoding (1000 vocab size → 1000-dim sparse vector for each word). Problems: huge dimensionality, no semantic relationship, orthogonal vectors.

Dense embeddings: learn 50-300 dimensional vectors where semantics are encoded in the space itself.

Key embeddings models:
- Word2Vec (2013): Skip-gram and CBOW. Fast, effective. learns: king - man + woman ≈ queen
- GloVe (2014): Global Vectors. Combines local context (like Word2Vec) with global statistics
- FastText: handles OOV words via subword vectors

Limitation of static embeddings: same vector for "bank" (financial) and "bank" (river). Contextual embeddings fix this."""
    },
    {
        "title": "Tokenization Strategies",
        "body": """Tokenization converts raw text into discrete units (tokens). Three levels:

Character-level: 'hello' → ['h','e','l','l','o']. Too granular. Hard to learn semantic patterns. Huge sequence length. Need 128-256 tokens per language.

Word-level: 'hello' → ['hello']. Simple but problematic: huge vocabulary (100K+ for English), rare words, spelling variations ('running' vs 'runs' are different tokens).

Subword-level: 'hello' → ['he','ll','o'] (BPE) or ['hell','o'] (WordPiece). Sweet spot: manageable vocab (30K-50K), handles rare words via composition, captures morphology.

Common subword algorithms:
- Byte Pair Encoding (BPE): start with characters, iteratively merge most frequent pairs until target vocab size
- WordPiece: used in BERT, greedily merges pairs to maximize likelihood, marks subword boundaries with ##
- SentencePiece: operates on bytes/characters directly, language-agnostic, good for multilingual"""
    },
    {
        "title": "Vocabulary Size Trade-offs",
        "body": """Vocabulary size is a key hyperparameter. Trade-offs:

Small vocab (5K tokens): each concept requires multiple tokens, longer sequences, model sees more token transitions, harder to learn discrete semantics, faster inference (fewer embedding lookups).

Large vocab (100K tokens): covers most words as single tokens, shorter sequences, more embedding parameters, larger model size, slower inference, better expressiveness per sequence position.

Typical choice: 30K-50K for English. 100K+ for multilingual models (need coverage across languages).

Practical impact:
- Tokenizing 'unbelievable' with small vocab: ['un','be','lie','va','ble'] (5 tokens) vs large vocab: ['unbelievable'] (1 token)
- Long sequences → attention complexity O(n^2), more memory
- Shorter sequences → better for transformers, faster training"""
    },
    {
        "title": "BPE, WordPiece, SentencePiece Explained",
        "body": """Byte Pair Encoding (BPE):
Algorithm: start with character vocabulary, iteratively merge most frequent adjacent token pairs until reaching target size. Greedy, deterministic.
Example: corpus ['hello', 'world']. Initial chars: {h,e,l,o,w,r,d}. Merge 'l'+'l'→'ll', then 'he'+'ll'→'hell', etc.

WordPiece (BERT):
Similar to BPE but merges pairs based on likelihood increase, not frequency. Marks subword continuations with ##.
Example: 'unbelievable' → ['un','##believ','##able']. '##' prefix indicates continuation of previous word.
Advantage: cleaner subword boundaries, better for morphology.

SentencePiece:
Operates on raw bytes, not characters. Language-agnostic: no need for language-specific preprocessing.
Can handle any unicode character. Trains on byte sequences directly.
Advantage: works with all languages uniformly, good for multilingual and low-resource languages.

Trade-offs:
- BPE: simple, interpretable, widely supported
- WordPiece: better morphological boundaries, used in BERT family
- SentencePiece: language-agnostic, but less interpretable byte sequences"""
    }
]
