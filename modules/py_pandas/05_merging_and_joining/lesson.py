# Merging and Joining: Combining DataFrames

TITLE = "Merging and Joining"

SECTIONS = [
    {
        "id": "merge_types",
        "title": "Merge Operations: SQL-Like Joins",
        "body": """
<div class="concept-box">
<h2>Understanding Merge</h2>
<p><code>pd.merge()</code> combines two DataFrames based on shared key columns, similar to SQL JOIN operations.</p>
<p><strong>From first principles:</strong> Merge performs a lookup: for each row in the left DataFrame, find matching rows in the right DataFrame based on key values.</p>
</div>

<div class="worked-example">
<h3>Merge Join Types</h3>
<pre><code>import pandas as pd

# Sample data
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30, 40],
    'dept_name': ['Sales', 'IT', 'HR', 'Finance']
})

# INNER JOIN (default): only matching keys
inner = pd.merge(employees, departments, on='dept_id')
# Result: 4 rows (all employees have matching departments)

# LEFT JOIN: all from left, matching from right
left = pd.merge(employees, departments, on='dept_id', how='left')
# Result: 4 rows (all employees, NaN for non-matching depts)

# RIGHT JOIN: all from right, matching from left
right = pd.merge(employees, departments, on='dept_id', how='right')
# Result: 4 rows (all departments, NaN for employees without dept)

# OUTER JOIN: all from both
outer = pd.merge(employees, departments, on='dept_id', how='outer')
# Result: 5 rows (all employees AND all departments)</code></pre>
</div>

<div class="worked-example">
<h3>Merge on Different Column Names</h3>
<pre><code>import pandas as pd

employees = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'department_id': [10, 20, 10]
})

departments = pd.DataFrame({
    'id': [10, 20, 30],
    'name': ['Sales', 'IT', 'HR']
})

# left_on / right_on for different column names
result = pd.merge(
    employees, departments,
    left_on='department_id',
    right_on='id',
    how='inner'
)

# Rename conflicting columns
result = result.rename(columns={
    'name_x': 'employee_name',
    'name_y': 'department_name'
})</code></pre>
</div>

<div class="success-box">
<h3>Merge Strategy</h3>
<ul>
<li><strong>INNER:</strong> Only rows with keys in BOTH DataFrames</li>
<li><strong>LEFT:</strong> Keep all left rows, add matching right data</li>
<li><strong>RIGHT:</strong> Keep all right rows, add matching left data</li>
<li><strong>OUTER:</strong> Keep all rows from both, use NaN for missing</li>
</ul>
<p><strong>Most common:</strong> LEFT merge (preserve original records, augment with lookup data)</p>
</div>
"""
    },
    {
        "id": "index_based_joins",
        "title": "Index-Based Joins and Concatenation",
        "body": """
<div class="concept-box">
<h2>Index-Based Operations</h2>
<p>When the alignment key is the index (not a column), use <code>.join()</code> or <code>pd.concat()</code>.</p>
</div>

<div class="worked-example">
<h3>join() Method</h3>
<pre><code>import pandas as pd

# DataFrames with meaningful indices
prices = pd.DataFrame({
    'price': [100, 200, 300]
}, index=['apple', 'banana', 'cherry'])

inventory = pd.DataFrame({
    'stock': [50, 30, 20]
}, index=['apple', 'banana', 'cherry'])

# join() aligns by index (like SQL join on row labels)
result = prices.join(inventory)
# Result:
#         price  stock
# apple    100     50
# banana   200     30
# cherry   300     20

# Left join (default)
left_result = prices.join(inventory, how='left')

# Right join
right_result = prices.join(inventory, how='right')

# Outer join
outer_result = prices.join(inventory, how='outer')</code></pre>
</div>

<div class="worked-example">
<h3>concat() for Combining Multiple DataFrames</h3>
<pre><code>import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['row1', 'row2'])

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
}, index=['row3', 'row4'])

# Concatenate vertically (stack rows)
result = pd.concat([df1, df2], axis=0)  # axis=0 is default
# Result: 4 rows (rows from df1, then df2)

# Concatenate horizontally (side by side)
result = pd.concat([df1, df2], axis=1)
# Result: 2 rows, 4 columns

# Concatenate multiple DataFrames
result = pd.concat([df1, df2, df3], axis=0)

# Keys for hierarchical index
result = pd.concat([df1, df2], axis=0, keys=['set1', 'set2'])
# Creates MultiIndex</code></pre>
</div>

<div class="warning-box">
<h3>Difference: merge() vs join() vs concat()</h3>
<ul>
<li><code>pd.merge()</code>: Column-based JOIN (like SQL)</li>
<li><code>.join()</code>: Index-based alignment (shorthand for merge on index)</li>
<li><code>pd.concat()</code>: Stack/combine without alignment (axis=0 for rows, axis=1 for columns)</li>
</ul>
<p><strong>When to use:</strong></p>
<ul>
<li>Lookup table? Use <code>merge()</code></li>
<li>Augment with index-keyed data? Use <code>join()</code></li>
<li>Combine sequential data (e.g., multiple CSV files)? Use <code>concat()</code></li>
</ul>
</div>
"""
    },
    {
        "id": "advanced_joining",
        "title": "Advanced: Multi-Key Joins and Validation",
        "body": """
<div class="concept-box">
<h2>Complex Joining Scenarios</h2>
<p>Real-world data often requires multi-key joins, handling duplicates, and validating join results.</p>
</div>

<div class="worked-example">
<h3>Multi-Key Merge</h3>
<pre><code">import pandas as pd

orders = pd.DataFrame({
    'customer_id': [1, 1, 2, 2],
    'order_date': ['2024-01', '2024-02', '2024-01', '2024-03'],
    'amount': [100, 150, 200, 250]
})

payments = pd.DataFrame({
    'customer_id': [1, 1, 2, 2],
    'order_date': ['2024-01', '2024-02', '2024-01', '2024-03'],
    'paid_amount': [100, 150, 200, 250]
})

# Merge on multiple keys
result = pd.merge(
    orders, payments,
    on=['customer_id', 'order_date'],
    how='inner'
)</code></pre>
</div>

<div class="worked-example">
<h3>Validating Join Results</h3>
<pre><code">import pandas as pd

left = pd.DataFrame({
    'key': [1, 2, 3],
    'value_l': ['a', 'b', 'c']
})

right = pd.DataFrame({
    'key': [1, 2, 2, 4],
    'value_r': ['x', 'y', 'z', 'w']
})

# validate parameter catches data quality issues
# '1:1' - each key appears once in both
# 'm:1' - many in left, one in right
# '1:m' - one in left, many in right
# 'm:m' - many in both (cartesian product!)

result = pd.merge(left, right, on='key', validate='m:1')
# Raises if validation fails

# Check for duplicates before merge
assert not left.duplicated(subset=['key']).any()
assert not right.duplicated(subset=['key']).any()</code></pre>
</div>

<div class="success-box">
<h3>Join Performance Tips</h3>
<ul>
<li>Merge on indexed columns for speed (set_index before merge)</li>
<li>Smaller DataFrame on right (left is the "driving" table)</li>
<li>Filter before merging to reduce data size</li>
<li>Use validate parameter to catch data issues early</li>
<li>For many-to-many joins, result can explode in size (cartesian product)</li>
</ul>
</div>
"""
    }
]
