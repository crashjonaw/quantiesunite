"""
QuantiesUnite — Full Curriculum Graph Data
Singapore-aligned: Kindergarten → P5–P6 → Sec 1–2 → Sec 3–4 → J1–2 → University → Deep Learning
"""

TOPICS = {
    # ─── KINDERGARTEN ───────────────────────────────────────────────────────────
    "k_numbers":    {"name":"Number Recognition (0–20)","level":"Kindergarten","sg":"KG","color":"#7FFFD4","prereqs":[],"hours":2,"emoji":"🔢","tagline":"What does '5' really mean?"},
    "k_counting":   {"name":"Counting & Ordering","level":"Kindergarten","sg":"KG","color":"#7FFFD4","prereqs":["k_numbers"],"hours":2,"emoji":"🔟","tagline":"One, two, three — in order!"},
    "k_addition":   {"name":"Addition within 10","level":"Kindergarten","sg":"KG","color":"#7FFFD4","prereqs":["k_counting"],"hours":3,"emoji":"➕","tagline":"Putting things together"},
    "k_subtraction":{"name":"Subtraction within 10","level":"Kindergarten","sg":"KG","color":"#7FFFD4","prereqs":["k_counting"],"hours":3,"emoji":"➖","tagline":"Taking things away"},
    "k_shapes":     {"name":"Shapes & Patterns","level":"Kindergarten","sg":"KG","color":"#7FFFD4","prereqs":["k_numbers"],"hours":2,"emoji":"🔷","tagline":"Circles, squares, and beyond"},

    # ─── PRIMARY 1–2 ────────────────────────────────────────────────────────────
    "p12_whole_1000":     {"name":"Whole Numbers to 1,000","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["k_addition","k_subtraction"],"hours":4,"emoji":"🔢","tagline":"Hundreds, tens, and ones"},
    "p12_add_sub":        {"name":"Multi-digit Addition & Subtraction","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_whole_1000"],"hours":5,"emoji":"🧮","tagline":"Carrying and borrowing"},
    "p12_multiply":       {"name":"Multiplication (2, 5, 10 tables)","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_add_sub"],"hours":4,"emoji":"✖️","tagline":"Repeated addition made fast"},
    "p12_divide":         {"name":"Division Basics","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_multiply"],"hours":4,"emoji":"➗","tagline":"Sharing equally"},
    "p12_fractions_basic":{"name":"Simple Fractions (½, ¼, ¾)","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_divide"],"hours":3,"emoji":"🍕","tagline":"Parts of a whole"},
    "p12_measurement":    {"name":"Measurement (length, mass, volume)","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_add_sub"],"hours":3,"emoji":"📏","tagline":"How long? How heavy?"},
    "p12_time":           {"name":"Telling Time","level":"Primary 1–2","sg":"P1–P2","color":"#90EE90","prereqs":["p12_whole_1000"],"hours":2,"emoji":"🕐","tagline":"Reading clocks and calendars"},

    # ─── PRIMARY 3–4 ────────────────────────────────────────────────────────────
    "p34_whole_100k":   {"name":"Whole Numbers to 100,000","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p12_whole_1000"],"hours":4,"emoji":"🔢","tagline":"Thousands and ten-thousands"},
    "p34_all_tables":   {"name":"All Multiplication Tables","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p12_multiply"],"hours":4,"emoji":"📋","tagline":"3×7=21, fast!"},
    "p34_long_mult_div":{"name":"Long Multiplication & Division","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p34_all_tables","p34_whole_100k"],"hours":5,"emoji":"📐","tagline":"Big numbers, same idea"},
    "p34_fractions":    {"name":"Fractions (equivalent, unlike denominators)","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p12_fractions_basic","p34_long_mult_div"],"hours":6,"emoji":"🍕","tagline":"Adding ½ + ⅓ = ?"},
    "p34_decimals":     {"name":"Decimals (to 3 places)","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p34_fractions","p34_whole_100k"],"hours":5,"emoji":"0️⃣.","tagline":"Tenths, hundredths, thousandths"},
    "p34_perimeter_area":{"name":"Perimeter & Area","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p12_measurement","p34_whole_100k"],"hours":4,"emoji":"📐","tagline":"Around and inside shapes"},
    "p34_angles":       {"name":"Angles & Basic Geometry","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["k_shapes","p34_whole_100k"],"hours":3,"emoji":"📐","tagline":"Degrees of turn"},
    "p34_data":         {"name":"Data Representation","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p34_whole_100k"],"hours":3,"emoji":"📊","tagline":"Bar graphs and line graphs"},
    "p34_symmetry":     {"name":"Symmetry","level":"Primary 3–4","sg":"P3–P4","color":"#98FB98","prereqs":["p34_angles"],"hours":2,"emoji":"🪞","tagline":"Mirror images"},

    # ─── PRIMARY 5–6 ────────────────────────────────────────────────────────────
    "p56_fractions_adv":  {"name":"Advanced Fractions","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p34_fractions","p34_decimals"],"hours":6,"emoji":"🍕","tagline":"Complex fractions solved step-by-step"},
    "p56_ratio":          {"name":"Ratio & Proportion","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p56_fractions_adv"],"hours":5,"emoji":"⚖️","tagline":"3:5 — what does it mean?"},
    "p56_percentage":     {"name":"Percentage","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p56_fractions_adv","p34_decimals"],"hours":5,"emoji":"%","tagline":"Per hundred — discounts, GST, interest"},
    "p56_average":        {"name":"Average (Mean)","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p34_data","p34_long_mult_div"],"hours":3,"emoji":"📊","tagline":"What's the fair share?"},
    "p56_algebra_intro":  {"name":"Intro to Algebra","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p34_long_mult_div"],"hours":5,"emoji":"🔡","tagline":"Let x be the unknown"},
    "p56_volume":         {"name":"Volume (3D shapes)","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p34_perimeter_area"],"hours":4,"emoji":"📦","tagline":"How much fits inside?"},
    "p56_data_analysis":  {"name":"Data Analysis","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p34_data","p56_average"],"hours":3,"emoji":"📈","tagline":"Pie charts, tables, interpretation"},
    "p56_problem_solving":{"name":"Problem Solving (PSLE-style)","level":"P5–P6","sg":"P5–P6","color":"#3CB371","prereqs":["p56_ratio","p56_percentage","p56_algebra_intro"],"hours":8,"emoji":"🧩","tagline":"Heuristics and model drawing"},

    # ─── SEC 1–2 ────────────────────────────────────────────────────────────────
    "sec12_algebra":     {"name":"Algebra (expressions & linear equations)","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["p56_algebra_intro"],"hours":8,"emoji":"🔡","tagline":"Solve for x systematically"},
    "sec12_simultaneous":{"name":"Simultaneous Equations","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["sec12_algebra"],"hours":6,"emoji":"🔗","tagline":"Two unknowns, two equations"},
    "sec12_indices":     {"name":"Indices & Standard Form","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["p34_whole_100k","sec12_algebra"],"hours":5,"emoji":"⬆️","tagline":"Powers and very large/small numbers"},
    "sec12_geometry":    {"name":"Geometry (angles, triangles, polygons)","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["p34_angles","p34_symmetry"],"hours":7,"emoji":"📐","tagline":"Properties and proofs"},
    "sec12_pythagoras":  {"name":"Pythagoras' Theorem","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["sec12_geometry"],"hours":4,"emoji":"📐","tagline":"a² + b² = c²"},
    "sec12_statistics":  {"name":"Statistics (mean, median, mode)","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["p56_average","p34_data"],"hours":5,"emoji":"📊","tagline":"Describing data with numbers"},
    "sec12_probability": {"name":"Basic Probability","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["p34_fractions","sec12_statistics"],"hours":4,"emoji":"🎲","tagline":"Chances from 0 to 1"},
    "sec12_coordinates": {"name":"Coordinate Geometry","level":"Sec 1–2","sg":"Sec 1–2","color":"#4169E1","prereqs":["sec12_algebra","sec12_geometry"],"hours":5,"emoji":"🗺️","tagline":"Points, lines, gradients"},

    # ─── SEC 3–4 (E-Math) ───────────────────────────────────────────────────────
    "olevel_quadratic":  {"name":"Quadratic Equations & Functions","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_algebra","sec12_simultaneous"],"hours":8,"emoji":"📈","tagline":"Parabolas and the quadratic formula"},
    "olevel_graphs":     {"name":"Graphs & Functions","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_coordinates","olevel_quadratic"],"hours":6,"emoji":"📈","tagline":"Sketching and interpreting graphs"},
    "olevel_inequalities":{"name":"Linear Inequalities","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_algebra"],"hours":4,"emoji":"≤","tagline":"Ranges of solutions"},
    "olevel_sets":       {"name":"Set Theory","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_algebra"],"hours":4,"emoji":"🔵","tagline":"Unions, intersections, Venn diagrams"},
    "olevel_trigonometry":{"name":"Trigonometry","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_pythagoras","sec12_coordinates"],"hours":8,"emoji":"📐","tagline":"sin, cos, tan from the unit circle"},
    "olevel_circles":    {"name":"Circle Properties","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_geometry"],"hours":5,"emoji":"⭕","tagline":"Chords, tangents, arcs"},
    "olevel_vectors2d":  {"name":"Vectors (2D)","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_coordinates"],"hours":5,"emoji":"➡️","tagline":"Direction and magnitude"},
    "olevel_stats_adv":  {"name":"Advanced Statistics","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_statistics"],"hours":5,"emoji":"📊","tagline":"Cumulative frequency, box plots"},
    "olevel_prob_adv":   {"name":"Advanced Probability","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_probability"],"hours":5,"emoji":"🎲","tagline":"Tree diagrams, combined events"},
    "olevel_matrices":   {"name":"Matrices (basic)","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["sec12_algebra"],"hours":4,"emoji":"🔢","tagline":"Arrays of numbers that transform"},

    # ─── SEC 3–4 (A-Math) ───────────────────────────────────────────────────────
    "amath_polynomials": {"name":"Polynomials & Partial Fractions","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["olevel_quadratic"],"hours":6,"emoji":"🧮","tagline":"Factoring and decomposing expressions"},
    "amath_binomial":    {"name":"Binomial Theorem","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["amath_polynomials"],"hours":5,"emoji":"🔢","tagline":"Expanding (a+b)ⁿ systematically"},
    "amath_exp_log":     {"name":"Exponential & Logarithmic Functions","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["olevel_graphs"],"hours":7,"emoji":"📈","tagline":"e, ln, and the laws of logs"},
    "amath_trig_adv":    {"name":"Advanced Trigonometry","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["olevel_trigonometry"],"hours":7,"emoji":"〰️","tagline":"Identities, R-formula, equations"},
    "amath_diff_intro":  {"name":"Differentiation (intro)","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["olevel_graphs","amath_polynomials","amath_exp_log"],"hours":8,"emoji":"d/dx","tagline":"The rate of change — from first principles"},
    "amath_int_intro":   {"name":"Integration (intro)","level":"Sec 3–4","sg":"Sec 3–4","color":"#1E90FF","prereqs":["amath_diff_intro"],"hours":8,"emoji":"∫","tagline":"Reversing differentiation, area under curves"},

    # ─── J1–2 (JC / H2 Math) ────────────────────────────────────────────────────
    "alevel_functions":    {"name":"Functions & Graphs (advanced)","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["amath_exp_log","amath_polynomials"],"hours":8,"emoji":"𝑓","tagline":"Domain, range, inverse, composite"},
    "alevel_sequences":    {"name":"Sequences & Series","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["amath_polynomials","amath_binomial"],"hours":7,"emoji":"∑","tagline":"AP, GP, and sigma notation"},
    "alevel_vectors3d":    {"name":"Vectors (3D)","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["olevel_vectors2d","olevel_trigonometry"],"hours":8,"emoji":"➡️","tagline":"Lines and planes in 3D space"},
    "alevel_complex":      {"name":"Complex Numbers","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["olevel_quadratic","olevel_trigonometry"],"hours":7,"emoji":"𝑖","tagline":"Imaginary numbers unlock new dimensions"},
    "alevel_diff_adv":     {"name":"Differentiation (advanced)","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["amath_diff_intro","alevel_functions"],"hours":9,"emoji":"d/dx","tagline":"Chain rule, implicit, parametric"},
    "alevel_int_adv":      {"name":"Integration (advanced)","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["amath_int_intro","alevel_diff_adv"],"hours":10,"emoji":"∫","tagline":"By parts, substitution, volumes"},
    "alevel_de":           {"name":"Differential Equations","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["alevel_diff_adv","alevel_int_adv"],"hours":7,"emoji":"dy/dx","tagline":"Equations involving rates of change"},
    "alevel_counting":     {"name":"Permutations & Combinations","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["olevel_prob_adv"],"hours":6,"emoji":"🎰","tagline":"How many ways can you arrange things?"},
    "alevel_distributions":{"name":"Probability Distributions","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["alevel_counting","olevel_prob_adv"],"hours":8,"emoji":"🔔","tagline":"Binomial, Poisson, Normal distributions"},
    "alevel_hypothesis":   {"name":"Hypothesis Testing","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["alevel_distributions","olevel_stats_adv"],"hours":7,"emoji":"🔬","tagline":"Is this result statistically significant?"},
    "alevel_regression":   {"name":"Correlation & Regression","level":"J1–2","sg":"J1–2","color":"#9400D3","prereqs":["olevel_stats_adv","alevel_distributions"],"hours":5,"emoji":"📉","tagline":"Finding relationships in data"},

    # ─── LINEAR ALGEBRA (University) ────────────────────────────────────────────
    "la_systems":       {"name":"Systems of Linear Equations","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["alevel_int_adv","olevel_matrices"],"hours":6,"emoji":"🔗","tagline":"Many equations, many unknowns"},
    "la_gauss":         {"name":"Gaussian Elimination","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_systems"],"hours":5,"emoji":"↘️","tagline":"Row reduction to row echelon form"},
    "la_matrix_ops":    {"name":"Matrix Operations","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["olevel_matrices","la_gauss"],"hours":6,"emoji":"🔢","tagline":"Add, multiply, transpose matrices"},
    "la_determinants":  {"name":"Determinants","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_matrix_ops"],"hours":5,"emoji":"det","tagline":"A single number that encodes a matrix"},
    "la_vector_spaces": {"name":"Vector Spaces","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_gauss","alevel_vectors3d"],"hours":8,"emoji":"🌐","tagline":"Abstract spaces that satisfy key axioms"},
    "la_linear_trans":  {"name":"Linear Transformations","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_vector_spaces","la_matrix_ops"],"hours":7,"emoji":"🔄","tagline":"Matrices as geometric transformations"},
    "la_eigenvalues":   {"name":"Eigenvalues & Eigenvectors","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_linear_trans","la_determinants"],"hours":8,"emoji":"λ","tagline":"Vectors unchanged in direction by a transform"},
    "la_orthogonality": {"name":"Orthogonality & Least Squares","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_vector_spaces"],"hours":7,"emoji":"⊥","tagline":"Perpendicular spaces and best-fit solutions"},
    "la_svd":           {"name":"Singular Value Decomposition","level":"Linear Algebra","sg":"University","color":"#FF4500","prereqs":["la_eigenvalues","la_orthogonality"],"hours":8,"emoji":"∑","tagline":"The most important matrix factorisation"},

    # ─── PROBABILITY & STATISTICS (University) ──────────────────────────────────
    "ps_probability":   {"name":"Probability Theory (axioms)","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["alevel_distributions"],"hours":7,"emoji":"🎲","tagline":"Kolmogorov's axioms from first principles"},
    "ps_random_vars":   {"name":"Random Variables & Distributions","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_probability"],"hours":7,"emoji":"📊","tagline":"Discrete and continuous random variables"},
    "ps_expectation":   {"name":"Expectation, Variance & Moments","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_random_vars"],"hours":6,"emoji":"𝔼","tagline":"E[X], Var(X), and beyond"},
    "ps_clt":           {"name":"Central Limit Theorem","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_expectation"],"hours":5,"emoji":"🔔","tagline":"Why the normal distribution is everywhere"},
    "ps_inference":     {"name":"Statistical Inference","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_clt","alevel_hypothesis"],"hours":8,"emoji":"🔬","tagline":"MLE, confidence intervals, p-values"},
    "ps_bayesian":      {"name":"Bayesian Statistics","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_probability"],"hours":7,"emoji":"🧠","tagline":"Updating beliefs with evidence"},
    "ps_markov":        {"name":"Markov Chains","level":"Probability & Statistics","sg":"University","color":"#FF6347","prereqs":["ps_probability","la_matrix_ops"],"hours":6,"emoji":"⛓️","tagline":"Probabilistic state transitions"},

    # ─── PYTHON PROGRAMMING ──────────────────────────────────────────────────────
    "py_basics":      {"name":"Python Basics","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["p56_algebra_intro"],"hours":6,"emoji":"🐍","tagline":"Variables, types, and your first program"},
    "py_control":     {"name":"Control Flow","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_basics"],"hours":5,"emoji":"🔀","tagline":"if / else / for / while"},
    "py_functions":   {"name":"Functions & Modules","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_control"],"hours":5,"emoji":"🔧","tagline":"Reusable blocks of logic"},
    "py_data_structs":{"name":"Data Structures","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_functions"],"hours":6,"emoji":"🗂️","tagline":"Lists, dicts, sets, tuples"},
    "py_numpy":       {"name":"NumPy","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_data_structs","olevel_matrices"],"hours":7,"emoji":"🔢","tagline":"Fast numerical arrays and matrix ops"},
    "py_pandas":      {"name":"Pandas","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_numpy"],"hours":6,"emoji":"🐼","tagline":"DataFrames for data wrangling"},
    "py_matplotlib":  {"name":"Matplotlib & Visualisation","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_numpy"],"hours":5,"emoji":"📊","tagline":"Plotting data like a scientist"},
    "py_oop":         {"name":"Object-Oriented Programming","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_functions"],"hours":7,"emoji":"🏗️","tagline":"Classes, objects, inheritance"},
    "py_scipy":       {"name":"Scientific Computing (SciPy)","level":"Python","sg":"Programming","color":"#FFD700","prereqs":["py_numpy","alevel_int_adv"],"hours":6,"emoji":"🔬","tagline":"Integration, optimisation, linear algebra in Python"},

    # ─── DEEP LEARNING FOUNDATIONS ───────────────────────────────────────────────
    "dl_neural_nets": {"name":"Neural Networks from First Principles","level":"Deep Learning","sg":"Deep Learning","color":"#FF1493","prereqs":["la_matrix_ops","ps_expectation","py_numpy"],"hours":10,"emoji":"🧠","tagline":"Perceptrons to multi-layer networks"},
    "dl_gradient":    {"name":"Gradient Descent & Optimisation","level":"Deep Learning","sg":"Deep Learning","color":"#FF1493","prereqs":["dl_neural_nets","alevel_diff_adv"],"hours":8,"emoji":"⬇️","tagline":"Finding minima by following the slope"},
    "dl_backprop":    {"name":"Backpropagation","level":"Deep Learning","sg":"Deep Learning","color":"#FF1493","prereqs":["dl_gradient"],"hours":8,"emoji":"↩️","tagline":"Chain rule applied to neural networks"},
    "dl_activations": {"name":"Activation Functions","level":"Deep Learning","sg":"Deep Learning","color":"#FF1493","prereqs":["dl_neural_nets"],"hours":4,"emoji":"⚡","tagline":"ReLU, sigmoid, tanh — why they matter"},
    "dl_loss":        {"name":"Loss Functions & Regularisation","level":"Deep Learning","sg":"Deep Learning","color":"#FF1493","prereqs":["ps_probability","dl_neural_nets"],"hours":6,"emoji":"📉","tagline":"MSE, cross-entropy, L1/L2"},

    # ─── DEEP LEARNING ADVANCED (LSTM & TRANSFORMERS) ────────────────────────────
    "dl_rnn":           {"name":"Recurrent Neural Networks (RNN)","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_backprop","dl_activations"],"hours":8,"emoji":"🔄","tagline":"Networks with memory for sequences"},
    "dl_lstm":          {"name":"LSTM Architecture","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_rnn"],"hours":10,"emoji":"💾","tagline":"Long short-term memory — solving vanishing gradients"},
    "dl_sequence":      {"name":"Sequence Modelling Applications","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_lstm","py_pandas"],"hours":8,"emoji":"📝","tagline":"Time series, NLP, speech"},
    "dl_attention":     {"name":"Attention Mechanism","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_rnn","la_eigenvalues"],"hours":9,"emoji":"👁️","tagline":"Learning what to focus on"},
    "dl_transformer":   {"name":"Transformer Architecture","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_attention","la_svd"],"hours":12,"emoji":"⚡","tagline":"Attention is all you need"},
    "dl_self_attention":{"name":"Self-Attention & Multi-Head Attention","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_transformer"],"hours":8,"emoji":"🪞","tagline":"Every token attending to every other"},
    "dl_modern_lm":     {"name":"Modern Language Models (BERT, GPT)","level":"Deep Learning Advanced","sg":"Deep Learning","color":"#C71585","prereqs":["dl_transformer","dl_self_attention"],"hours":10,"emoji":"🤖","tagline":"Pre-training, fine-tuning, and the LLM revolution"},
}


LEVELS_ORDER = [
    "Kindergarten",
    "Primary 1–2",
    "Primary 3–4",
    "P5–P6",
    "Sec 1–2",
    "Sec 3–4",
    "J1–2",
    "Linear Algebra",
    "Probability & Statistics",
    "Python",
    "Deep Learning",
    "Deep Learning Advanced",
]

LEVEL_DESCRIPTIONS = {
    "Kindergarten": "Counting, shapes, and the very first ideas in mathematics.",
    "Primary 1–2": "Singapore P1–P2: Numbers to 1,000, times tables, simple fractions.",
    "Primary 3–4": "Singapore P3–P4: Long division, decimals, geometry, data.",
    "Primary 5–6": "Singapore P5–P6: Ratio, percentage, algebra, volume — PSLE exam-ready.",
    "Sec 1–2": "Singapore Sec 1–2: Algebra, Pythagoras, coordinates, probability.",
    "Sec 3–4": "Singapore Sec 3–4: Quadratics, trigonometry, calculus preview, advanced trig (E-Math + A-Math).",
    "J1–2": "Singapore JC (H2 Math): Full calculus, complex numbers, probability distributions.",
    "Linear Algebra": "University: Matrices, eigenvectors, SVD — the language of ML.",
    "Probability & Statistics": "University: Rigorous probability, CLT, Bayesian methods.",
    "Python": "Programming track: Python for scientific computing and data science.",
    "Deep Learning": "Neural networks from scratch: gradient descent, backpropagation.",
    "Deep Learning Advanced": "LSTM and Transformer architectures from first principles.",
}

LEVEL_TROPHY_NAMES = {
    "Kindergarten":            {"name": "Kindergarten Champion",     "emoji": "🌟"},
    "Primary 1–2":             {"name": "Primary School Starter",    "emoji": "🏫"},
    "Primary 3–4":             {"name": "Primary School Builder",    "emoji": "🧱"},
    "Primary 5–6":             {"name": "Primary School Master",     "emoji": "🎓"},
    "Sec 1–2":                 {"name": "Secondary Scholar",         "emoji": "📚"},
    "Sec 3–4":                 {"name": "O-Level Champion",          "emoji": "🏅"},
    "J1–2":                    {"name": "JC Conqueror",              "emoji": "🎯"},
    "Linear Algebra":          {"name": "Matrix Master",             "emoji": "🔢"},
    "Probability & Statistics": {"name": "Probability Pro",          "emoji": "🎲"},
    "Python":                  {"name": "Python Programmer",         "emoji": "🐍"},
    "Deep Learning":           {"name": "Neural Network Novice",     "emoji": "🧠"},
    "Deep Learning Advanced":  {"name": "Deep Learning Grandmaster", "emoji": "🤖"},
}


def get_graph_data():
    """Return nodes and edges for D3 graph rendering."""
    nodes = []
    edges = []
    for tid, t in TOPICS.items():
        nodes.append({
            "id": tid,
            "name": t["name"],
            "level": t["level"],
            "color": t["color"],
            "emoji": t["emoji"],
            "hours": t["hours"],
            "tagline": t["tagline"],
            "sg": t["sg"],
        })
        for prereq in t["prereqs"]:
            edges.append({"source": prereq, "target": tid})
    return {"nodes": nodes, "links": edges}


def get_topic(tid):
    return TOPICS.get(tid)


def get_unlocked_by(tid):
    """Topics that become available after completing tid."""
    return [k for k, v in TOPICS.items() if tid in v["prereqs"]]
