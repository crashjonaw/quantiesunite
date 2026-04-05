# Indexing and Slicing

TITLE = "Indexing and Slicing"

SECTIONS = [
    {
        'id': 'py_numpy_05',
        'title': 'Basic Indexing and Slicing',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Basic Indexing and Slicing</h2>

<div class="concept-box formula-box">
<h3>Accessing Array Elements</h3>
<p>NumPy provides multiple ways to access and extract elements from arrays. Understanding the difference between views and copies is critical for efficient memory usage.</p>

<h4>Indexing Methods:</h4>
<ul>
<li><strong>Integer indexing:</strong> Access single elements by position</li>
<li><strong>Slicing:</strong> Extract contiguous ranges using start:stop:step</li>
<li><strong>Fancy indexing:</strong> Use arrays of indices to select elements</li>
<li><strong>Boolean indexing:</strong> Select elements matching a condition</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Code Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Integer indexing
first = arr[0]  # 10
last = arr[-1]  # 50

# Slicing (creates view, not copy)
subset = arr[1:4]  # [20, 30, 40]
reverse = arr[::-1]  # [50, 40, 30, 20, 10]

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
element = matrix[1, 2]  # 6
row = matrix[0, :]  # [1, 2, 3]
col = matrix[:, 1]  # [2, 5, 8]
submatrix = matrix[0:2, 1:3]  # Top-right 2x2
</pre>
</div>

<div class="success-box">
<h4>View vs Copy:</h4>
<p>Slicing creates a view (reference) to the original data. Modifying a slice modifies the original array. Use <code>.copy()</code> to create independent data.</p>
</div>
</div>
'''
    },
    {
        'id': 'py_numpy_06',
        'title': 'Advanced Indexing',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Advanced Indexing Techniques</h2>

<div class="concept-box formula-box">
<h3>Fancy and Boolean Indexing</h3>
<p>Beyond basic slicing, NumPy allows powerful selection using arrays and boolean conditions. These techniques always return copies, not views.</p>

<h4>Advanced Techniques:</h4>
<ul>
<li><strong>Fancy indexing:</strong> Arrays of indices select arbitrary elements</li>
<li><strong>Boolean indexing:</strong> Boolean masks select elements matching conditions</li>
<li><strong>np.where:</strong> Conditional selection and replacement</li>
<li><strong>Multidimensional indexing:</strong> Complex selections across dimensions</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Advanced Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing with index array
indices = np.array([0, 2, 4])
selected = arr[indices]  # [10, 30, 50]

# Boolean indexing
mask = arr > 25  # [False, False, True, True, True]
filtered = arr[mask]  # [30, 40, 50]

# Conditional operations with np.where
arr2 = np.array([1, 2, 3, 4, 5])
result = np.where(arr2 > 3, arr2 * 10, arr2)  # [1, 2, 3, 40, 50]

# 2D fancy indexing
matrix = np.arange(12).reshape(3, 4)
rows = np.array([0, 2])
cols = np.array([1, 3])
selected = matrix[rows[:, np.newaxis], cols]  # Select (0,1), (0,3), (2,1), (2,3)
</pre>
</div>

<div class="warning-box" style="border-left: 4px solid #ff9999; padding: 16px; margin: 12px 0; border-radius: 4px">
<h4>Memory Implications:</h4>
<p>Fancy and boolean indexing create new arrays (copies), not views. They use more memory but allow flexible element selection.</p>
</div>
</div>
'''
    }
]
