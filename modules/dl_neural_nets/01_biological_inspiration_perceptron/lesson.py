TITLE = "Biological Inspiration and the Perceptron"

SECTIONS = [
    {
        "id": "nn_biological_inspiration",
        "title": "The Biological Neuron & Mathematical Abstraction",
        "body": '<h2>From Biology to Mathematics</h2><p>A biological neuron receives inputs via dendrites, processes them in the soma, and transmits outputs via the axon. This biological system inspired the artificial neuron: a simple computational unit that captures the essence of neural information processing.</p><div class="concept-box"><h3>The Artificial Neuron</h3><p>An artificial neuron computes a weighted sum of inputs plus bias, then applies an activation function:</p><p>\\(z = \\sum_{i=1}^{n} w_i x_i + b\\)</p><p>\\(a = \\sigma(z)\\)</p><p>Where \\(w_i\\) are weights, \\(b\\) is the bias, and \\(\\sigma\\) is the activation function.</p></div>'
    },
    {
        "id": "nn_perceptron_basics",
        "title": "The Perceptron Learning Rule",
        "body": '<h2>First Artificial Neural Network</h2><p>The perceptron is the simplest neural network: a single artificial neuron with a step activation function. It learns to classify linearly separable data.</p><div class="worked-example"><h3>Perceptron Update Rule</h3><p>If prediction is wrong: \\(\\mathbf{w} \\leftarrow \\mathbf{w} + \\eta y \\mathbf{x}\\)</p><p>Where \\(\\eta\\) is the learning rate and \\(y\\) is the true label.</p></div><div class="warning-box"><p><strong>Limitation:</strong> Cannot learn non-linearly separable patterns like XOR.</p></div>'
    },
    {
        "id": "nn_activation_functions",
        "title": "Activation Functions: Introducing Nonlinearity",
        "body": '<h2>Beyond Linear Combinations</h2><p>Activation functions introduce nonlinearity, allowing neurons to learn complex patterns. Common choices include:</p><div class="concept-box"><h3>Popular Activation Functions</h3><p><strong>Sigmoid:</strong> \\(\\sigma(z) = \\frac{1}{1 + e^{-z}}\\)</p><p><strong>Tanh:</strong> \\(\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}\\)</p><p><strong>ReLU:</strong> \\(\\text{ReLU}(z) = \\max(0, z)\\)</p></div><div class="success-box"><p>ReLU is preferred in modern deep networks due to computational efficiency and better gradient flow.</p></div>'
    }
]
