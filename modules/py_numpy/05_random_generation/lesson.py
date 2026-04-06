# Random Number Generation

TITLE = "Random Number Generation"

SECTIONS = [
    {
        'id': 'py_numpy_09',
        'title': 'Random Distributions',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Random Number Generation and Distributions</h2>

<div class="concept-box formula-box">
<h3>Generating Random Numbers</h3>
<p>NumPy provides efficient random number generation with support for many probability distributions. The random module uses fast pseudorandom algorithms optimized for array generation.</p>

<h4>Common Distributions:</h4>
<ul>
<li><strong>Uniform:</strong> np.random.uniform(low, high, size)</li>
<li><strong>Normal:</strong> np.random.normal(loc, scale, size)</li>
<li><strong>Exponential:</strong> np.random.exponential(scale, size)</li>
<li><strong>Poisson:</strong> np.random.poisson(lam, size)</li>
<li><strong>Integer:</strong> np.random.randint(low, high, size)</li>
<li><strong>Permutation:</strong> np.random.permutation, shuffle</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Code Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Uniform distribution [0, 1)\\nuniform = np.random.uniform(0, 1, 5)

# Standard normal distribution (mean=0, std=1)
normal = np.random.normal(0, 1, (3, 4))

# Integers in range [0, 10)
integers = np.random.randint(0, 10, 5)

# Random choice from array
choices = np.random.choice([1, 2, 3, 4, 5], size=3, replace=False)

# Shuffle array in-place
arr = np.arange(10)
np.random.shuffle(arr)

# Permutation (returns shuffled copy)
perm = np.random.permutation(10)

# Sample from specific distribution
exponential = np.random.exponential(scale=2, size=1000)
poisson = np.random.poisson(lam=3, size=100)
</pre>
</div>

<div class="success-box">
<h4>Reproducibility:</h4>
<p>Set <code>np.random.seed()</code> at the beginning of your script to ensure consistent results across runs. This is crucial for debugging and sharing reproducible analyses.</p>
</div>
</div>
'''
    },
    {
        'id': 'py_numpy_10',
        'title': 'Random State and Generators',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Random State Management and New Generator API</h2>

<div class="concept-box formula-box">
<h3>Modern Random Number Generation</h3>
<p>NumPy's new <code>Generator</code> API provides better control over random state and supports multiple bit generators for different use cases and quality levels.</p>

<h4>Generator API Features:</h4>
<ul>
<li><strong>BitGenerators:</strong> PCG64, MT19937, SFC64, Philox</li>
<li><strong>Independent streams:</strong> Each Generator has separate state</li>
<li><strong>Reproducibility:</strong> Explicit state management and seeding</li>
<li><strong>Performance:</strong> Some generators faster than others</li>
<li><strong>Parallel safety:</strong> Multiple independent generators for multiprocessing</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>New Generator API:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np
from numpy.random import Generator, PCG64

# Create a Generator with specific bit generator
rng = Generator(PCG64(seed=42))

# Generate random numbers
arr = rng.standard_normal(1000)
integers = rng.integers(0, 100, size=10)\\nuniform = rng.uniform(0, 1, 5)

# Multiple independent streams for parallel work
rngs = [Generator(PCG64(seed=i)) for i in range(4)]

# Access and restore state
state = rng.bit_generator.state
# ... do something ...
# Restore: rng.bit_generator.state = state

# Compare performance
print(rng.bit_generator.state)
</pre>
</div>

<div class="warning-box" style="border-left: 4px solid #ff9999; padding: 16px; margin: 12px 0; border-radius: 4px">
<h4>Legacy vs Modern:</h4>
<p>The old <code>np.random.seed()</code> and global state are deprecated. New code should use the <code>Generator</code> API. Existing code using the legacy API will still work but should be updated for thread safety.</p>
</div>
</div>
'''
    }
]
