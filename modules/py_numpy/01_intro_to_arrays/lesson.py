# Introduction to NumPy Arrays

TITLE = "Introduction to NumPy Arrays"

SECTIONS = [
    {
        'id': 'py_numpy_01',
        'title': 'Arrays & Memory',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Arrays & Memory: First Principles</h2>

<div class="concept-box formula-box">
<h3>Understanding NumPy Arrays</h3>
<p>NumPy arrays are homogeneous, contiguous blocks of memory containing elements of the same data type. Unlike Python lists which store pointers to objects scattered in memory, NumPy arrays store values directly in a single memory block.</p>

<h4>Key Concepts:</h4>
<ul>
<li><strong>Homogeneity:</strong> All elements must be the same data type</li>
<li><strong>Contiguity:</strong> Elements are stored consecutively in memory</li>
<li><strong>Efficiency:</strong> Direct memory access enables fast operations</li>
<li><strong>dtype:</strong> Data type descriptor for array elements</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Code Example:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

# Create arrays with different dtypes
int_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
float_array = np.array([1.1, 2.2, 3.3], dtype=np.float64)

# Check memory layout
print(int_array.nbytes)  # Total bytes in array
print(int_array.itemsize)  # Bytes per element
print(int_array.strides)  # Byte offsets between elements
</pre>
</div>

<div class="warning-box" style="border-left: 4px solid #ff9999; padding: 16px; margin: 12px 0; border-radius: 4px">
<h4>Memory Implications:</h4>
<p>When you modify a NumPy array, you're directly modifying the underlying memory. Creating views or slices references the same memory block, not copies.</p>
</div>
</div>
'''
    },
    {
        'id': 'py_numpy_02',
        'title': 'Creation Methods',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Array Creation Methods</h2>

<div class="concept-box formula-box">
<h3>Creating Arrays from Scratch</h3>
<p>NumPy provides multiple methods to create arrays for different use cases. Each method allocates memory and initializes values according to specific patterns.</p>

<h4>Creation Functions:</h4>
<ul>
<li><code>np.zeros(shape)</code> - Array filled with zeros</li>
<li><code>np.ones(shape)</code> - Array filled with ones</li>
<li><code>np.arange(start, stop, step)</code> - Range of values</li>
<li><code>np.linspace(start, stop, num)</code> - Evenly spaced values</li>
<li><code>np.full(shape, fill_value)</code> - Array filled with constant</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Practical Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
# Creation from Python iterables
arr1 = np.array([1, 2, 3])

# Creation with specific patterns
zeros = np.zeros((3, 4))  # 3x4 matrix of zeros
ones = np.ones((2, 2, 2))  # 3D array of ones

# Range creation
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace_arr = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]

# Custom fill value
custom = np.full((2, 3), 7)  # All elements set to 7
</pre>
</div>

<div class="success-box">
<h4>Best Practice:</h4>
<p>Use <code>np.empty()</code> for uninitialized arrays when you will immediately fill values. This is faster than zero-initialization when the initial values will be overwritten.</p>
</div>
</div>
'''
    }
]
