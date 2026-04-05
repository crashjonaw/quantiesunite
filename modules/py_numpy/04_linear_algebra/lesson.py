# Linear Algebra with NumPy

TITLE = "Linear Algebra with NumPy"

SECTIONS = [
    {
        'id': 'py_numpy_07',
        'title': 'Matrix Operations',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Matrix Operations and Linear Algebra</h2>

<div class="concept-box formula-box">
<h3>Core Linear Algebra Operations</h3>
<p>NumPy's linear algebra submodule (np.linalg) provides efficient implementations of matrix operations fundamental to scientific computing, machine learning, and data analysis.</p>

<h4>Key Operations:</h4>
<ul>
<li><strong>Matrix multiplication:</strong> np.dot, @, np.matmul</li>
<li><strong>Transpose:</strong> arr.T, np.transpose</li>
<li><strong>Determinant:</strong> np.linalg.det</li>
<li><strong>Inverse:</strong> np.linalg.inv</li>
<li><strong>Eigenvalues:</strong> np.linalg.eig</li>
<li><strong>Decompositions:</strong> SVD, QR, Cholesky</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Code Examples:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)  # or A @ B
print(C)  # [[19, 22], [43, 50]]

# Transpose
At = A.T  # [[1, 3], [2, 4]]

# Determinant
det_A = np.linalg.det(A)

# Inverse
A_inv = np.linalg.inv(A)
identity = A @ A_inv  # Should be identity matrix

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Solve linear system Ax = b
b = np.array([3, 7])
x = np.linalg.solve(A, b)
</pre>
</div>

<div class="success-box">
<h4>Linear System Solving:</h4>
<p>Use <code>np.linalg.solve(A, b)</code> instead of <code>np.linalg.inv(A) @ b</code>. The solve function is more efficient and numerically stable.</p>
</div>
</div>
'''
    },
    {
        'id': 'py_numpy_08',
        'title': 'Vectorization and Performance',
        'body': '''
<div class="worked-example">
<h2 class="accent-heading">Vectorization and Performance Optimization</h2>

<div class="concept-box formula-box">
<h3>Why Vectorization Matters</h3>
<p>Vectorization—replacing explicit loops with array operations—is the foundation of NumPy's performance. Operations execute in compiled C code, avoiding Python's interpreter overhead.</p>

<h4>Vectorization Strategies:</h4>
<ul>
<li>Replace explicit loops with array operations</li>
<li>Use broadcasting to avoid reshaping</li>
<li>Leverage ufuncs (universal functions) for element-wise operations</li>
<li>Minimize array copies and temporary allocations</li>
<li>Choose appropriate dtypes to reduce memory</li>
</ul>
</div>

<div class="worked-example success-box">
<h4>Loop vs Vectorized:</h4>
<pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
import numpy as np
import time

x = np.random.randn(1000000)

# Slow: Python loop
start = time.time()
result_loop = [i ** 2 for i in x]
loop_time = time.time() - start

# Fast: Vectorized
start = time.time()
result_vec = x ** 2
vec_time = time.time() - start

print(f"Loop: {loop_time:.4f}s, Vectorized: {vec_time:.6f}s")
# Typical speedup: 100-1000x

# Broadcasting example
matrix = np.random.randn(1000, 1000)
row_sum = matrix.sum(axis=1, keepdims=True)

# Slow: explicit loop
# result_loop = np.zeros_like(matrix)
# for i in range(matrix.shape[0]):
#     result_loop[i] = matrix[i] / row_sum[i]

# Fast: broadcasting
result_vec = matrix / row_sum
</pre>
</div>

<div class="warning-box" style="border-left: 4px solid #ff9999; padding: 16px; margin: 12px 0; border-radius: 4px">
<h4>Memory Efficiency:</h4>
<p>Be aware of temporary array creation. Operations like <code>a + b * c</code> may create intermediate arrays. Use in-place operations (<code>*=, +=</code>) sparingly, only when memory is critical.</p>
</div>
</div>
'''
    }
]
