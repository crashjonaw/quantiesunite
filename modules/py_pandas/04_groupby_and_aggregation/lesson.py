# GroupBy and Aggregation: Split-Apply-Combine Pattern

TITLE = "GroupBy and Aggregation"

SECTIONS = [
    {
        "id": "groupby_fundamentals",
        "title": "GroupBy: The Split-Apply-Combine Pattern",
        "body": """
<div class="concept-box">
<h2>Understanding GroupBy</h2>
<p>GroupBy implements the <strong>split-apply-combine</strong> pattern:</p>
<ol>
<li><strong>Split:</strong> Partition data into groups based on key(s)</li>
<li><strong>Apply:</strong> Compute operation on each group independently</li>
<li><strong>Combine:</strong> Reassemble results into new DataFrame/Series</li>
</ol>
<p><strong>From first principles:</strong> GroupBy creates internal groups using a hash table, then applies functions group-by-group. This is memory-efficient and scalable.</p>
</div>

<div class="worked-example">
<h3>Basic GroupBy Syntax</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'salary': [50000, 70000, 55000, 45000, 75000, 60000]
})

# Group by single column
sales_by_dept = df.groupby('department')['salary'].mean()
# Result:
# department
# HR      45000.0
# IT      72500.0
# Sales   55000.0

# Group by multiple columns
grouped = df.groupby(['department', 'name'])['salary'].sum()

# Access group object (don't compute yet)
group_obj = df.groupby('department')
# group_obj is lazy—no computation until you call a method

# Iterate through groups
for dept, group_data in df.groupby('department'):
    print(f"Department: {dept}")
    print(group_data)</code></pre>
</div>

<div class="warning-box">
<h3>GroupBy Returns Different Shapes</h3>
<ul>
<li>Single column → Series</li>
<li>Multiple columns → DataFrame</li>
<li>Aggregation → reduced dimensions</li>
<li>Transform → same shape as input</li>
<li>Apply → depends on function</li>
</ul>
</div>
"""
    },
    {
        "id": "aggregation_methods",
        "title": "Aggregation: Computing Group Statistics",
        "body": """
<div class="concept-box">
<h2>Aggregation Functions</h2>
<p>Aggregation reduces each group to a single value. Pandas provides many built-in aggregations, plus custom function support.</p>
</div>

<div class="worked-example">
<h3>Built-in Aggregations</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'salary': [50000, 70000, 55000, 45000, 75000, 60000]
})

grouped = df.groupby('department')['salary']

# Single aggregation
grouped.mean()
grouped.sum()
grouped.min()
grouped.max()
grouped.std()
grouped.count()  # Count non-null values

# Multiple aggregations at once
grouped.agg(['mean', 'sum', 'min', 'max'])

# Named aggregations (pandas 0.25+)
grouped.agg(
    avg_salary=('salary', 'mean'),
    total_salary=('salary', 'sum'),
    min_salary=('salary', 'min')
)

# Custom function
grouped.agg(lambda x: x.max() - x.min())  # Range

# Different functions per column
df.groupby('department').agg({
    'salary': 'mean',
    'name': 'count'
})</code></pre>
</div>

<div class="worked-example">
<h3>Multiple Groups and Complex Aggregations</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'year': [2022, 2022, 2023, 2023],
    'region': ['East', 'West', 'East', 'West'],
    'sales': [10000, 15000, 12000, 18000]
})

# Group by multiple columns
result = df.groupby(['year', 'region'])['sales'].sum()
# Result is Series with MultiIndex

# Convert to DataFrame for clarity
result.unstack()  # Pivot: regions as columns

# Using agg with dict for flexibility
result = df.groupby('year').agg({
    'sales': ['sum', 'mean'],
    'region': 'count'
})</code></pre>
</div>

<div class="success-box">
<h3>Common Aggregation Functions</h3>
<table>
<tr><td><code>mean()</code></td><td>Average</td></tr>
<tr><td><code>median()</code></td><td>Median</td></tr>
<tr><td><code>sum()</code></td><td>Total</td></tr>
<tr><td><code>count()</code></td><td>Non-null count</td></tr>
<tr><td><code>size()</code></td><td>Group size (including NaN)</td></tr>
<tr><td><code>min()/max()</code></td><td>Min/max value</td></tr>
<tr><td><code>std()/var()</code></td><td>Standard deviation/variance</td></tr>
<tr><td><code>first()/last()</code></td><td>First/last value in group</td></tr>
</table>
</div>
"""
    },
    {
        "id": "transform_and_apply",
        "title": "Transform and Apply: Beyond Aggregation",
        "body": """
<div class="concept-box">
<h2>Transform vs Aggregation</h2>
<p><strong>Aggregation:</strong> Reduces group to single value (output smaller than input)</p>
<p><strong>Transform:</strong> Returns same shape as input with computed values (broadcasting group results back)</p>
<p><strong>Apply:</strong> Applies arbitrary function to each group, flexible shape</p>
</div>

<div class="worked-example">
<h3>Transform: Return Same Shape as Input</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'salary': [50000, 70000, 55000, 45000, 75000, 60000]
})

# Aggregate: reduces to 3 rows (one per department)
dept_avg = df.groupby('department')['salary'].mean()
# HR      45000.0
# IT      72500.0
# Sales   55000.0

# Transform: returns 6 rows (broadcasts group value to each row)
df['dept_avg_salary'] = df.groupby('department')['salary'].transform('mean')
# Now df has new column with department average for each row

# Compute standardized salary (subtract group mean, divide by group std)
df['salary_zscore'] = df.groupby('department')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Remove outliers per group (> 2 std from mean)
df['outlier'] = df.groupby('department')['salary'].transform(
    lambda x: np.abs((x - x.mean()) / x.std()) > 2
)</code></pre>
</div>

<div class="worked-example">
<h3>Apply: Custom Functions Per Group</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'department': ['Sales', 'IT', 'Sales', 'IT'],
    'salary': [50000, 70000, 55000, 75000]
})

# apply() with custom function
def salary_range(group):
    return group['salary'].max() - group['salary'].min()

result = df.groupby('department').apply(salary_range)

# Complex processing returning DataFrame
def group_stats(group):
    return pd.DataFrame({
        'mean': [group['salary'].mean()],
        'std': [group['salary'].std()],
        'count': [len(group)]
    })

result = df.groupby('department').apply(group_stats)

# Filter groups meeting criteria
high_var_depts = df.groupby('department').filter(
    lambda x: x['salary'].std() > 5000
)</code></pre>
</div>

<div class="success-box">
<h3>Transform vs Aggregation Pattern</h3>
<pre><code"># Aggregation: reduces rows
df.groupby('dept')['salary'].mean()  # 3 rows (one per dept)

# Transform: keeps rows
df.groupby('dept')['salary'].transform('mean')  # 6 rows (broadcasts)

# Use transform when you need to:
# - Create new column with group statistics
# - Normalize values within groups
# - Filter outliers per group
# - Compare each value to group average</code></pre>
</div>
"""
    }
]
