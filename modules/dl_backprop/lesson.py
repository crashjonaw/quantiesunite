SECTIONS = [
    {"id": "bp_chain_rule", "title": "The Chain Rule in Calculus", "content": '<p>$$\\frac{df}{dx} = \\frac{df}{dg} \\cdot \\frac{dg}{dx}$$</p><p>For composition \\(f(g(x))\\), we multiply derivatives.</p>'},
    {"id": "bp_computation_graph", "title": "Computation Graph Representation", "content": '<p>Each operation is a node. Edges represent data flow. Backprop traverses graph backward computing gradients.</p>'},
    {"id": "bp_algorithm", "title": "Backpropagation Algorithm", "content": '<p>1. Forward pass: compute all activations. 2. Backward pass: compute \\(\\frac{\\partial L}{\\partial w_i}\\) for all weights.</p>'},
    {"id": "bp_layer_wise", "title": "Layer-wise Gradient Flow", "content": '<p>$$\\frac{\\partial L}{\\partial \\mathbf{a}^{(l-1)}} = \\left(\\frac{\\partial L}{\\partial \\mathbf{z}^{(l)}} \\mathbf{W}^{(l)T}\\right) \\odot \\sigma\'(\\mathbf{z}^{(l-1)})$$</p>'},
    {"id": "bp_vanishing_gradients", "title": "Vanishing and Exploding Gradients", "content": '<p>In deep networks, gradients can shrink or explode. Sigmoid derivative: \\(\\sigma\'(z) \\leq 0.25\\). Over L layers: \\((0.25)^L \\to 0\\).</p>'},
    {"id": "bp_implementation", "title": "Automatic Differentiation in Practice", "content": '<p>Modern frameworks (PyTorch, TF) compute gradients automatically via autodiff. Users write forward pass; backward computed automatically.</p>'}
]