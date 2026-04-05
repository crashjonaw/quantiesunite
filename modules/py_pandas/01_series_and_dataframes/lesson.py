# Series and DataFrames: Fundamental Data Structures

TITLE = "Series and DataFrames"

SECTIONS = [
    {
        "id": "series_fundamentals",
        "title": "Series: One-Dimensional Data",
        "body": """
<div class="concept-box">
<h2>Understanding Series</h2>
<p>A <code>Series</code> is a one-dimensional array with labeled indices. It is the fundamental building block for understanding pandas data structures.</p>
<p><strong>From first principles:</strong> A Series is essentially a dictionary-like mapping where each position has:</p>
<ul>
<li><strong>Index:</strong> A label (key) for the position</li>
<li><strong>Value:</strong> The data at that position</li>
<li><strong>Dtype:</strong> The data type of the value</li>
</ul>
</div>

<div class="worked-example">
<h3>Creating a Series</h3>
<pre><code>import pandas as pd

# From a list (generates default 0-based index)
s1 = pd.Series([10, 20, 30, 40])
# Result:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# From a dictionary (keys become indices)
s2 = pd.Series({'apple': 5, 'banana': 3, 'cherry': 8})
# Result:
# apple     5
# banana    3
# cherry    8
# dtype: int64

# With explicit index
s3 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
# Result:
# a    100
# b    200
# c    300
# dtype: int64</code></pre>
</div>

<div class="concept-box">
<h3>Memory Model</h3>
<p>Under the hood, a Series stores:</p>
<ol>
<li><strong>Data array:</strong> Contiguous memory block (numpy array)</li>
<li><strong>Index object:</strong> Separate metadata mapping labels to positions</li>
<li><strong>Name:</strong> Optional identifier for the Series</li>
<li><strong>Dtype:</strong> Single data type for all values</li>
</ol>
<p>This separation allows fast position-based lookup AND efficient label-based lookup via a hash table in the Index.</p>
</div>
"""
    },
    {
        "id": "dataframe_fundamentals",
        "title": "DataFrames: Two-Dimensional Data",
        "body": """
<div class="concept-box">
<h2>Understanding DataFrames</h2>
<p>A <code>DataFrame</code> is a two-dimensional table with labeled rows and columns. Think of it as a dictionary of Series objects sharing the same index.</p>
<p><strong>From first principles:</strong> A DataFrame is built on:</p>
<ul>
<li><strong>Columns:</strong> Each column is a Series (same length, shared index)</li>
<li><strong>Index:</strong> Row labels (same for all columns)</li>
<li><strong>Column names:</strong> Labels for each Series/column</li>
<li><strong>Shape:</strong> (n_rows, n_columns)</li>
</ul>
</div>

<div class="worked-example">
<h3>Creating a DataFrame</h3>
<pre><code>import pandas as pd

# From a dictionary of lists
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# From a list of dictionaries
df2 = pd.DataFrame([
    {'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'name': 'Bob', 'age': 30, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
])

# From a numpy array with index and columns
import numpy as np
df3 = pd.DataFrame(
    np.random.randn(3, 3),
    index=['row1', 'row2', 'row3'],
    columns=['col_a', 'col_b', 'col_c']
)</code></pre>
</div>

<div class="concept-box">
<h3>Memory Model</h3>
<p>A DataFrame is NOT a simple 2D array. Instead:</p>
<ol>
<li>Each column is stored as a separate Series (potentially different dtypes)</li>
<li>Columns share a common Index object for row alignment</li>
<li>Column order is preserved via a separate Index for columns</li>
<li>This allows efficient column addition/removal without reshuffling data</li>
</ol>
<p><strong>Key insight:</strong> DataFrames are optimized for column operations, not row operations.</p>
</div>

<div class="success-box">
<h3>Series vs DataFrame Relationship</h3>
<pre><code># Accessing a column returns a Series
df['name']  # type: pd.Series

# Accessing a row returns a Series
df.loc['row1']  # type: pd.Series

# DataFrame is a container of Series
type(df['name'])  # <class 'pandas.core.series.Series'></code></pre>
</div>
"""
    },
    {
        "id": "indexing_internals",
        "title": "Index: The Alignment Mechanism",
        "body": """
<div class="concept-box">
<h2>The Index Object</h2>
<p>The <code>Index</code> is the foundation of pandas alignment. It enables:</p>
<ul>
<li><strong>Label-based selection:</strong> Access data by meaningful names</li>
<li><strong>Automatic alignment:</strong> Operations align by index, not position</li>
<li><strong>Fast lookup:</strong> Hash table for O(1) membership testing</li>
</ul>
</div>

<div class="worked-example">
<h3>Index Types and Behavior</h3>
<pre><code># RangeIndex (default, 0-based)
s1 = pd.Series([1, 2, 3])
print(s1.index)  # RangeIndex(start=0, stop=3, step=1)

# Named index
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s2.index)  # Index(['a', 'b', 'c'], dtype='object')

# MultiIndex (hierarchical)
s3 = pd.Series(
    [1, 2, 3, 4],
    index=pd.MultiIndex.from_tuples([
        ('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')
    ])
)

# DatetimeIndex (for time series)
s4 = pd.Series(
    [1, 2, 3],
    index=pd.date_range('2024-01-01', periods=3, freq='D')
)</code></pre>
</div>

<div class="warning-box">
<h3>Index Immutability</h3>
<p>Pandas Index objects are <strong>immutable</strong> by design. This allows:</p>
<ul>
<li>Safe use as dictionary keys</li>
<li>Efficient memory sharing between Series/DataFrames</li>
<li>Predictable behavior in operations</li>
</ul>
<p>To modify an index, create a new one: <code>df.index = df.index.map(str.upper)</code></p>
</div>
"""
    }
]
