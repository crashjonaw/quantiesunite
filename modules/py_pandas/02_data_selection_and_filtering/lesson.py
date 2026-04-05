# Data Selection and Filtering: Accessing and Querying Data

TITLE = "Data Selection and Filtering"

SECTIONS = [
    {
        "id": "label_based_selection",
        "title": "Label-Based Selection with .loc",
        "body": """
<div class="concept-box">
<h2>Label-Based Access (.loc)</h2>
<p>The <code>.loc</code> indexer selects data by <strong>label</strong> (index/column names). It uses the Index object's hash table for O(1) lookup.</p>
<p><strong>From first principles:</strong> <code>.loc</code> respects the semantic meaning of your index—it's the intended way to access data in real-world scenarios.</p>
</div>

<div class="worked-example">
<h3>Selection Patterns with .loc</h3>
<pre><code>import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 75000]
}, index=['emp1', 'emp2', 'emp3'])

# Single row by label
df.loc['emp1']  # Returns Series

# Single cell
df.loc['emp1', 'name']  # 'Alice'

# Multiple rows (list of labels)
df.loc[['emp1', 'emp3']]  # Returns DataFrame

# Slice with labels (INCLUSIVE of end!)
df.loc['emp1':'emp2']  # Includes both 'emp1' and 'emp2'

# Single column
df.loc[:, 'name']  # All rows, 'name' column

# Multiple columns
df.loc[:, ['name', 'age']]  # All rows, subset of columns

# Boolean indexing
df.loc[df['age'] > 26]  # Rows where age > 26</code></pre>
</div>

<div class="warning-box">
<h3>Label Slicing is Inclusive</h3>
<p>Unlike Python's slice notation, <code>.loc</code> slicing <strong>includes the endpoint</strong>:</p>
<pre><code>df.loc['emp1':'emp2']  # Includes BOTH 'emp1' and 'emp2'
# Different from Python: list[0:2] excludes index 2</code></pre>
<p>This matches the intuition of "select from label A to label B" in data analysis.</p>
</div>
"""
    },
    {
        "id": "position_based_selection",
        "title": "Position-Based Selection with .iloc",
        "body": """
<div class="concept-box">
<h2>Position-Based Access (.iloc)</h2>
<p>The <code>.iloc</code> indexer selects data by <strong>integer position</strong>, ignoring the index labels. It uses standard Python slicing semantics (exclusive end).</p>
<p><strong>Use case:</strong> When you want the 3rd row regardless of its label, or need predictable positional access.</p>
</div>

<div class="worked-example">
<h3>Selection Patterns with .iloc</h3>
<pre><code>import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 75000]
}, index=['emp1', 'emp2', 'emp3'])

# First row (position 0)
df.iloc[0]  # Returns Series for 'emp1'

# First cell
df.iloc[0, 0]  # 'Alice' (row 0, col 0)

# Rows 0 and 1 (standard Python slicing)
df.iloc[0:2]  # Excludes index 2

# Last row
df.iloc[-1]  # Last row (row 2)

# Column by position
df.iloc[:, 0]  # All rows, first column

# Multiple columns by position
df.iloc[:, [0, 2]]  # Columns 0 and 2

# Boolean indexing (must match length)
df.iloc[df['age'] > 26]  # ERROR: boolean array, use loc instead</code></pre>
</div>

<div class="success-box">
<h3>.loc vs .iloc Summary</h3>
<ul>
<li><code>.loc</code>: Labels → semantic, inclusive slicing</li>
<li><code>.iloc</code>: Positions → structural, exclusive slicing</li>
<li>Boolean masks work with <code>.loc</code> (aligned by index)</li>
<li><code>.iloc</code> requires positional boolean arrays</li>
</ul>
</div>
"""
    },
    {
        "id": "boolean_filtering",
        "title": "Boolean Filtering: Conditional Selection",
        "body": """
<div class="concept-box">
<h2>Boolean Indexing</h2>
<p>Boolean filtering creates a boolean array (True/False for each row) and selects rows where the result is True. This is the primary way to perform conditional queries.</p>
<p><strong>Key insight:</strong> Boolean arrays are aligned by index, ensuring correct row matching even with reordered or filtered data.</p>
</div>

<div class="worked-example">
<h3>Building Boolean Filters</h3>
<pre><code>import pandas as pd

df = pd.DataFrame({
    'product': ['Apple', 'Banana', 'Cherry', 'Date'],
    'quantity': [10, 5, 8, 12],
    'price': [1.50, 0.75, 2.00, 3.00]
})

# Single condition
df[df['quantity'] > 8]  # Rows where quantity > 8

# Multiple conditions (use &, |, ~)
df[(df['quantity'] > 5) & (df['price'] < 2.50)]  # AND operator
df[(df['product'] == 'Apple') | (df['product'] == 'Date')]  # OR operator
df[~(df['quantity'] < 8)]  # NOT operator (note ~ not !)

# String methods
df[df['product'].str.len() > 4]  # Products with >4 characters
df[df['product'].str.startswith('A')]  # Products starting with 'A'

# isin() for membership
df[df['product'].isin(['Apple', 'Banana'])]  # Multiple values

# Storing boolean arrays
mask = df['quantity'] > 8
df[mask]  # Use stored mask for clarity</code></pre>
</div>

<div class="warning-box">
<h3>Common Pitfalls with Boolean Indexing</h3>
<ul>
<li>Use <code>&</code> not <code>and</code> (element-wise vs single boolean)</li>
<li>Use <code>|</code> not <code>or</code></li>
<li>Use <code>~</code> not <code>not</code></li>
<li>Parenthesize conditions: <code>(df['a'] > 5) & (df['b'] < 10)</code></li>
<li>Result is always a DataFrame (even if single row)</li>
</ul>
</div>

<div class="success-box">
<h3>Efficient Filtering Pattern</h3>
<pre><code># Best practice: store mask for readability and reusability
expensive_items = df['price'] > 5.00
low_stock = df['quantity'] < 10
target = df[expensive_items & low_stock]

# Or use query() for string-based filtering
target = df.query('price > 5.00 and quantity < 10')</code></pre>
</div>
"""
    },
    {
        "id": "advanced_selection",
        "title": "Advanced Selection Techniques",
        "body": """
<div class="concept-box">
<h2>Query and Selection Methods</h2>
<p>Pandas offers multiple methods for selection, each optimized for different scenarios. Choose based on readability and performance needs.</p>
</div>

<div class="worked-example">
<h3>query() Method</h3>
<pre><code>import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 75000]
})

# query() uses string expressions (variables with @)
result = df.query('age > 26')
result = df.query('salary >= @threshold')  # Variables prefixed with @

# More readable than boolean arrays
# df[(df['age'] > 26) & (df['salary'] < 70000)]
df.query('age > 26 and salary < 70000')</code></pre>
</div>

<div class="worked-example">
<h3>isin() and Between()</h3>
<pre><code># isin() for membership testing
df[df['name'].isin(['Alice', 'Bob'])]

# between() for range queries
df[df['salary'].between(50000, 70000)]  # Inclusive on both ends

# Negation
df[~df['name'].isin(['Alice'])]  # NOT in list</code></pre>
</div>

<div class="success-box">
<h3>Selection Performance</h3>
<p><strong>For large datasets:</strong></p>
<ul>
<li><code>.query()</code> can be faster due to expression compilation</li>
<li><code>.isin()</code> is faster than multiple OR conditions</li>
<li><code>.between()</code> is optimized for range queries</li>
<li>Boolean indexing is fast but creates intermediate arrays</li>
</ul>
</div>
"""
    }
]
