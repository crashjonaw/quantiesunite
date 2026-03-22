SECTIONS = [
    {"id": "seq_language_modeling", "title": "Language Modeling: Predicting Next Token", "content": '<p>Given sequence \\(x_1, \\ldots, x_{t-1}\\), predict \\(x_t\\). Loss: $$L = -\\log P(x_t | x_1, \\ldots, x_{t-1})$$</p>'},
    {"id": "seq_machine_translation", "title": "Encoder-Decoder for Translation", "content": '<p>Encoder RNN reads source: \\(h = \\text{Encoder}(x_1, \\ldots, x_T)\\). Decoder generates target: \\(y_1, \\ldots, y_M\\) from initial state \\(h\\).</p>'},
    {"id": "seq_attention_context", "title": "Attention: Dynamic Context Vector", "content": '<p>Instead of single fixed context, compute attention weights over encoder states. Output: \\(c_t = \\sum_i \\alpha_{ti} h_i\\)</p>'},
    {"id": "seq_beam_search", "title": "Beam Search Decoding", "content": '<p>At each step, keep top-K hypotheses (beam width). Expand and rescore. Enables better than greedy decoding.</p>'},
    {"id": "seq_speech_recognition", "title": "Speech Recognition: Audio-to-Text", "content": '<p>Spectrograms as input, character sequences as output. Often CTC (Connectionist Temporal Classification) loss for alignment.</p>'},
    {"id": "seq_music_generation", "title": "Music Generation Applications", "content": '<p>Learn sequential patterns in note sequences or audio. Sampling strategies (temperature, top-k) for diversity.</p>'}
]