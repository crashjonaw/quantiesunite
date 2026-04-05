# Array Operations and Broadcasting

TITLE = "Array Operations and Broadcasting"

SECTIONS = [
    {
        'id': 'py_numpy_03',
        'title': 'Element-wise Operations',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Element-wise Operations</h2>

<div class="concept-box formula-box">
<h3>Vectorized Operations</h3>
<p>NumPy operations are applied element-by-element across entire arrays. This vectorized approach is much faster than Python loops because operations are implemented in compiled C code.</p>

<h4>Supported Operations:</h4>
<ul>
<li><strong>Arithmetic:</strong> +, -, *, /, //, %, **</li>
<li><strong>Comparison:</strong> ==, !=, <, >, <=, >=</li>
<li><strong>Logical:</strong> &, |, ^, ~</li>
<li><strong>Mathematical:</strong> np.sqrt, np.sin, np.exp, np.log</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Code Example:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise operations
c = a + b  # [6, 8, 10, 12]
d = a * b  # [5, 12, 21, 32]
e = np.sqrt(a)  # [1, 1.414, 1.732, 2]

# Comparison creates boolean array
mask = a > 2  # [False, False, True, True]

# Operations with scalars
f = a * 2  # [2, 4, 6, 8]
</pre>
</div>

<div class="success-box">
<h4>Performance Note:</h4>
<p>Vectorized NumPy operations are 10-100x faster than Python loops. Always prefer array operations over explicit iteration.</p>
</div>
</div>
'''
    },
    {
        'id': 'py_numpy_04',
        'title': 'Broadcasting Rules',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Broadcasting: Operating on Different Shapes</h2>

<div class="concept-box formula-box">
<h3>Broadcasting Fundamentals</h3>
<p>Broadcasting allows NumPy to work with arrays of different shapes by automatically expanding smaller arrays to match the shape of larger ones, without copying data.</p>

<h4>Broadcasting Rules:</h4>
<ol>
<li>If arrays have different numbers of dimensions, pad the smaller shape with 1s on the left</li>
<li>Arrays are compatible if dimensions are equal or one is 1</li>
<li>Dimension with size 1 is stretched to match the other array</li>
</ol>
</div>

<div class="worked-example success-box">
<h4>Broadcasting Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

# Scalar broadcasts to any shape
a = np.array([[1, 2], [3, 4]])
b = 2
c = a * b  # Each element multiplied by 2

# Row vector broadcasts to match matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
result = matrix + row  # row broadcast to (2, 3)

# Column vector broadcasts
col = np.array([[1], [2], [3]])
result2 = col + np.array([10, 20])  # Broadcasting to (3, 2)

# Check if shapes can broadcast
shapes = (3, 4)
other = (4,)  # Compatible: (3, 4) and (1, 4) -> (3, 4)
</pre>
</div>

<div class="warning-box" style="border-left: 4px solid #ff9999; padding: 16px; margin: 12px 0; border-radius: 4px">
<h4>Common Broadcasting Errors:</h4>
<p>Shapes (3, 4) and (3,) are incompatible without reshaping. The dimension sizes don't align—you need explicit reshaping with <code>[:, np.newaxis]</code> or <code>.reshape()</code>.</p>
</div>
</div>
'''
    }
]
