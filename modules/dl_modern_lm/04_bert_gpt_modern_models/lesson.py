TITLE = "BERT, GPT, and Modern Language Models"

SECTIONS = [
    {
        "title": "BERT: Bidirectional Encoder Representations from Transformers",
        "body": """BERT (2018) revolutionized NLP with bidirectional pre-training. Encoder-only architecture optimized for understanding.

Architecture:
12-24 transformer layers (depth varies by size)
Bidirectional attention: each token attends to all other tokens
Vocabulary: 30K WordPiece tokens
Max sequence: 512 tokens

Variants by size:
BERT-base: 110M parameters, 12 layers, 768 hidden
BERT-large: 340M parameters, 24 layers, 1024 hidden
Smaller variants: MobileBERT (25M), DistilBERT (66M) for efficiency

Pre-training:
Masked Language Modeling (MLM): mask 15%, predict from context
Next Sentence Prediction (NSP): predict if sentences are consecutive (less important than MLM)
Trained on 3.3B words from Wikipedia and BookCorpus

Fine-tuning applications:
Classification: add linear layer on [CLS] token
Sequence tagging: predict label per token
Question-answering: predict answer span in context
Semantic similarity: compare [CLS] representations

Performance (original paper):
GLUE benchmark: 80.4% (vs 78.3% previous best)
SQuAD 2.0 Q&A: 93.2% (vs 91.6% previous)

Strength: excellent for understanding tasks, symmetric bidirectional attention
Limitation: cannot generate text naturally (bidirectional architecture unsuitable for autoregressive generation)"""
    },
    {
        "title": "GPT Series: Generative Pre-trained Transformers",
        "body": """GPT (2018+) pursues large-scale autoregressive pre-training. Decoder-only architecture for generation and reasoning.

GPT-1 (2018): 117M params
Simple: decoder-only, CLM pre-training
Task-agnostic fine-tuning: add linear layer, fine-tune

GPT-2 (2019): 1.5B params, shocking in-context learning
40GB web text (Common Crawl)
Few-shot learning: examples in prompt, no fine-tuning
Showed emergent capabilities: summarization, translation without task-specific training

GPT-3 (2020): 175B params, paradigm shift
Few-shot and zero-shot learning
In-context learning: answer questions from prompt alone
Versatility: code, essays, math, creative writing
Cost: estimated 1M+ GPUs to train

GPT-3.5/GPT-4 (2023): multimodal, instruction-tuning
RLHF training: reinforcement learning from human feedback
Instruction following: better at following user intent
Multimodal (GPT-4): text and image understanding

Architecture:
Decoder-only transformer
Causal masking: tokens attend only to past
Positional embeddings: absolute or rotary
Large context window (2K-128K tokens depending on version)

Advantages:
Natural language generation: autoregressive matches training
Few-shot learning: in-context examples enable new tasks
Zero-shot: can solve tasks with just descriptions
Reasoning: chain-of-thought prompting unlocks reasoning

Scaling trend: 10x parameters ≈ 10x more capable (rough)
GPT-3 > GPT-3.5 > GPT-4: each generation significantly stronger"""
    },
    {
        "title": "Other Important Architectures",
        "body": """RoBERTa (2019): improved BERT
Better pre-training: longer training, larger batches, better masking
Performance: +2-3% over BERT on GLUE/SQuAD

ALBERT (2019): parameter reduction
Factorized embeddings: smaller vocab embedding, projected to hidden
Cross-layer sharing: same weights across layers
66M params vs 110M (BERT-base), similar performance

Sentence-BERT (SBERT, 2019): specialized for semantic similarity
Fine-tuned BERT for sentence embeddings
Useful for semantic search, clustering, recommendation

T5 (2019): unified text-to-text framework
Encoder-decoder: combines bidirectional encoding with autoregressive decoding
All NLP tasks as seq2seq: translate, summarize, classify via "Classify: [input] →"
Denoising pre-training: corrupt input (span corruption), learn to reconstruct
Dominant for 2019-2022, versatile across tasks

RoBERTa/Llama family (2022+): efficient scaling
Llama (2023): open-source, efficient training
7B, 13B, 70B parameters
Outperforms closed models at similar scale
Instruction-tuned variants: Llama 2 with RLHF

Mistral, Zephyr (2023): sparse experts
Mixture of Experts (MoE): route tokens to different expert networks
Sparser computation: not all parameters active per token
Better inference efficiency

Recent trend: decoder-only dominance
GPT-3 success: few-shot, in-context learning, reasoning
Most new models are decoder-only (LLaMA, Mistral, Claude, Gemini)"""
    }
]