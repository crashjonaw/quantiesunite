# Data Cleaning and Missing Values: Handling Real-World Data

TITLE = "Data Cleaning and Missing Values"

SECTIONS = [
    {
        "id": "missing_values_detection",
        "title": "Detecting and Understanding Missing Values",
        "body": """
<div class="concept-box">
<h2>Missing Value Representation</h2>
<p>Pandas uses <code>NaN</code> (Not a Number) to represent missing values across all dtypes. This is a special float value that propagates through calculations.</p>
<p><strong>From first principles:</strong></p>
<ul>
<li><code>NaN</code> is contagious: any operation with NaN produces NaN</li>
<li>Equality testing fails: <code>NaN == NaN</code> is False</li>
<li><code>None</code> and <code>NaN</code> are treated equivalently in pandas</li>
<li>Use <code>.isna()</code> or <code>.isnull()</code> (aliases) to detect</li>
</ul>
</div>

<div class="worked-example">
<h3>Detecting Missing Values</h3>
<pre><code">import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'David'],
    'age': [25, np.nan, 35, 40],
    'email': ['a@ex.com', 'b@ex.com', 'c@ex.com', None]
})

# Element-wise detection
df.isna()  # Returns boolean DataFrame

# Count missing per column
df.isna().sum()  # Count of NaN in each column
df.isnull().sum()  # Same (aliases)

# Total missing
df.isna().sum().sum()

# Rows with ANY missing
df.isna().any(axis=1)

# Rows with ALL missing
df.isna().all(axis=1)

# DataFrame-level info
df.info()  # Shows non-null counts
df.describe()  # Automatically excludes NaN</code></pre>
</div>

<div class="warning-box">
<h3>NaN Behavior with Operations</h3>
<pre><code"># NaN propagates
5 + np.nan  # nan
np.mean([1, 2, np.nan])  # nan (without skipna=True)

# But pandas aggregations skip NaN by default
df['age'].mean()  # Skips NaN values (different from numpy!)
df['age'].sum()  # Also skips NaN

# Explicit control
df['age'].sum(skipna=True)  # Default
df['age'].sum(skipna=False)  # Returns NaN if any missing</code></pre>
</div>
"""
    },
    {
        "id": "handling_missing_values",
        "title": "Strategies for Handling Missing Data",
        "body": """
<div class="concept-box">
<h2>Missing Value Treatment Options</h2>
<p>Different strategies for handling missing data:</p>
<ol>
<li><strong>Deletion:</strong> Remove rows/columns with missing values</li>
<li><strong>Forward fill:</strong> Propagate last valid value forward (time series)</li>
<li><strong>Backward fill:</strong> Propagate next valid value backward</li>
<li><strong>Interpolation:</strong> Estimate missing values mathematically</li>
<li><strong>Imputation:</strong> Replace with mean/median/mode/custom value</li>
</ol>
<p><strong>Key principle:</strong> Choose based on the mechanism of missingness—MCAR, MAR, or MNAR.</p>
</div>

<div class="worked-example">
<h3>Deletion: dropna()</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
})

# Drop rows with ANY missing
df.dropna()  # axis=0 (rows) is default

# Drop rows with ALL missing
df.dropna(how='all')

# Drop columns with ANY missing
df.dropna(axis=1)  # axis=1 (columns)

# Drop if missing in specific column(s)
df.dropna(subset=['A'])  # Keep rows where 'A' is not NaN

# Threshold: drop if < 2 non-null values
df.dropna(thresh=2)</code></pre>
</div>

<div class="worked-example">
<h3>Forward/Backward Fill: fillna() and fill_value</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'value': [1.0, np.nan, np.nan, 4.0, np.nan, 6.0]
}, index=pd.date_range('2024-01-01', periods=6))

# Forward fill (last observation carried forward)
df.ffill()  # or fillna(method='ffill') in older versions
df.ffill(limit=1)  # Fill only 1 value per gap

# Backward fill
df.bfill()

# Fill with constant
df.fillna(0)

# Fill with different values per column
df.fillna({'A': 0, 'B': 'unknown'})

# Interpolation (linear between values)
df.interpolate()  # Linear interpolation</code></pre>
</div>

<div class="worked-example">
<h3>Imputation: Replacing with Statistics</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'age': [25, np.nan, 35, np.nan, 50],
    'salary': [50000, 60000, np.nan, 75000, 80000]
})

# Fill with mean
df.fillna(df.mean())

# Fill with median (robust to outliers)
df.fillna(df.median())

# Fill with mode (most common value)
df.fillna(df.mode().iloc[0])

# Column-specific imputation
df['age'].fillna(df['age'].mean())
df['salary'].fillna(df['salary'].median())

# Group-based imputation
df['age'].fillna(df.groupby('department')['age'].transform('mean'))</code></pre>
</div>

<div class="success-box">
<h3>Best Practices</h3>
<ul>
<li><strong>Document your decisions:</strong> Record which strategy you chose and why</li>
<li><strong>Analyze patterns:</strong> Check if missingness is random (MCAR) or systematic</li>
<li><strong>Preserve information:</strong> Create indicator columns for imputed values if important</li>
<li><strong>Validate impact:</strong> Compare results with and without missing data</li>
<li><strong>For time series:</strong> Prefer forward fill over deletion</li>
<li><strong>For cross-sectional:</strong> Consider deletion or mean/median imputation</li>
</ul>
</div>
"""
    },
    {
        "id": "data_type_conversion",
        "title": "Data Type Conversion and Validation",
        "body": """
<div class="concept-box">
<h2>Type Conversion and Validation</h2>
<p>Proper data types enable efficient storage and correct operations. Pandas provides flexible conversion methods.</p>
</div>

<div class="worked-example">
<h3>astype() for Type Conversion</h3>
<pre><code">import pandas as pd

df = pd.DataFrame({
    'id': ['1', '2', '3'],
    'amount': ['100.50', '200.75', '300.25'],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03']
})

# Convert to appropriate types
df['id'] = df['id'].astype('int64')
df['amount'] = df['amount'].astype('float64')
df['date'] = pd.to_datetime(df['date'])

# Category type for memory efficiency
df['category'] = df['category'].astype('category')

# Nullable integer type (handles NaN)
df['count'] = df['count'].astype('Int64')  # Capital I

# String type
df['name'] = df['name'].astype('string')</code></pre>
</div>

<div class="warning-box">
<h3>Type Conversion Errors</h3>
<pre><code"># This raises ValueError
df['amount'].astype('int64')  # '100.50' cannot convert to int

# Use to_numeric() with error handling
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Invalid → NaN
df['amount'] = pd.to_numeric(df['amount'], errors='ignore')  # Keep original on error

# Type coercion in operations
df['id'].astype('float')  # Convert before division for float result</code></pre>
</div>

<div class="success-box">
<h3>Data Validation Pattern</h3>
<pre><code">import pandas as pd

# Check dtypes
df.dtypes
df.info()

# Validate ranges
assert df['age'].min() >= 0, "Age cannot be negative"
assert df['age'].max() <= 150, "Age seems unrealistic"

# Check for duplicates
df.duplicated().sum()
df[df.duplicated(keep=False)]  # Show all duplicates

# Remove duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['email'])  # On specific columns</code></pre>
</div>
"""
    }
]
