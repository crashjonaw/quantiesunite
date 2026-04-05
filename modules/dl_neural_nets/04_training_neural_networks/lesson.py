TITLE = "Training Neural Networks"

SECTIONS = [
    {
        "id": "nn_initialization",
        "title": "Weight Initialization Schemes",
        "body": '<h2>Starting from the Right Place</h2><p>Proper weight initialization is critical for successful training. Poor initialization can lead to vanishing or exploding gradients, causing the network to get stuck in suboptimal solutions.</p><div class="concept-box"><h3>Xavier Initialization (Glorot)</h3><p>Initialize weights from a uniform distribution:</p><p>$$\\mathbf{W} \\sim \\text{Uniform}\\left(-\\sqrt{\\frac{6}{n_{in} + n_{out}}}, \\sqrt{\\frac{6}{n_{in} + n_{out}}}\\right)$$</p><p>Designed to maintain equal variance of activations across layers, preventing saturation in sigmoid/tanh networks.</p></div><div class="worked-example"><h3>He Initialization for ReLU</h3><p>Since ReLU zeroes out negative values, use a slightly larger variance:</p><p>$$\\mathbf{W} \\sim \\mathcal{N}\\left(0, \\frac{2}{n_{in}}\\right)$$</p><p>This maintains gradient magnitudes through ReLU networks, enabling much deeper architectures.</p></div><div class="success-box"><p><strong>Bias initialization:</strong> Always initialize biases to zero.</p></div>'
    },
    {
        "id": "nn_gradient_descent",
        "title": "Backpropagation and Gradient Descent",
        "body": '<h2>Learning Through Error Propagation</h2><p>Backpropagation is an efficient algorithm for computing gradients by applying the chain rule backwards through the network. Gradient descent uses these gradients to update weights and minimize the loss.</p><div class="concept-box"><h3>The Learning Update</h3><p>For each weight: \\(\\mathbf{w} \\leftarrow \\mathbf{w} - \\eta \\frac{\\partial L}{\\partial \\mathbf{w}}\\)</p><p>Where \\(\\eta\\) is the learning rate and \\(\\frac{\\partial L}{\\partial \\mathbf{w}}\\) is the gradient computed via backpropagation.</p></div><div class="warning-box"><p><strong>Learning rate matters:</strong> Too large causes divergence, too small causes slow convergence.</p></div>'
    },
    {
        "id": "nn_loss_functions",
        "title": "Loss Functions for Different Tasks",
        "body": '<h2>Measuring Prediction Error</h2><p>The loss function quantifies how far predictions deviate from true targets. The choice depends on the task.</p><div class="concept-box"><h3>Common Loss Functions</h3><p><strong>Classification (Cross-Entropy):</strong> \\(L = -\\sum_c y_c \\log(\\hat{y}_c)\\)</p><p><strong>Regression (MSE):</strong> \\(L = \\frac{1}{n}\\sum_i (y_i - \\hat{y}_i)^2\\)</p></div><div class="worked-example"><h3>Why Cross-Entropy for Classification?</h3><p>Cross-entropy provides stronger gradients for misclassified samples, enabling faster learning compared to MSE. It naturally handles probability distributions from softmax outputs.</p></div>'
    },
    {
        "id": "nn_learning_dynamics",
        "title": "Understanding Training Dynamics",
        "body": '<h2>How Networks Learn Over Time</h2><p>Neural network training progresses through distinct phases: initial random phase, rapid learning phase, and convergence phase.</p><div class="concept-box"><h3>Training Curves</h3><p>Loss typically decreases exponentially initially, then slows down. Validation loss may diverge from training loss, indicating overfitting.</p></div><div class="success-box"><p><strong>Early stopping:</strong> Monitor validation loss and stop when it plateaus to prevent overfitting.</p></div>'
    }
]
