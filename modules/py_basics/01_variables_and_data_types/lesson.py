# Variables and Data Types

TITLE = "Variables and Data Types"

SECTIONS = [
    {
        'id': 'var_dt_01',
        'title': 'Introduction to Variables',
        'body': '''
<h3>What is a Variable?</h3>
<div class="concept-box">
    <p>A variable is a named container that stores a value in memory. From a first-principles perspective, when you create a variable in Python, you are:</p>
    <ol>
        <li>Allocating memory space</li>
        <li>Creating a label/reference to that memory location</li>
        <li>Storing data at that location</li>
    </ol>
</div>

<h3>Variable Assignment: The First Principles</h3>
<div class="worked-example">
    <p><strong>Example:</strong></p>
    <pre><code>name = "Alice"
age = 25
temperature = 98.6</code></pre>
    <p>When Python executes <code>name = "Alice"</code>:</p>
    <ol>
        <li>Python creates a string object "Alice" in memory</li>
        <li>Python creates a variable named <code>name</code></li>
        <li>The variable <code>name</code> references the memory address of "Alice"</li>
    </ol>
</div>

<h3>Variable Naming Rules</h3>
<div class="concept-box">
    <p>Valid variable names follow these rules (first principles):</p>
    <ul>
        <li>Must start with a letter (a-z, A-Z) or underscore (_)</li>
        <li>Can contain letters, numbers, and underscores</li>
        <li>Case-sensitive: <code>Name</code> and <code>name</code> are different variables</li>
        <li>Cannot be Python keywords (if, for, while, etc.)</li>
    </ul>
</div>

<div class="worked-example">
    <p><strong>Valid and Invalid Examples:</strong></p>
    <pre><code># Valid\\nuser_name = "Bob"
_private = 100
price2 = 29.99

# Invalid
2nd_place = "Silver"  # Starts with number\\nuser-name = "Bob"     # Contains hyphen
for = 5               # Python keyword</code></pre>
</div>
'''
    },
    {
        'id': 'var_dt_02',
        'title': 'Core Data Types',
        'body': '''
<h3>The Five Core Data Types</h3>

<h4>1. Integer (int)</h4>
<div class="concept-box">
    <p>Whole numbers without decimal points. At the binary level, integers are stored using two's complement representation.</p>
</div>

<div class="worked-example">
    <pre><code>count = 42
temperature = -5
year = 2024</code></pre>
</div>

<h4>2. Float (float)</h4>
<div class="concept-box">
    <p>Decimal numbers. Floats use IEEE 754 double-precision format internally, which can introduce rounding errors (first-principles understanding).</p>
</div>

<div class="worked-example">
    <pre><code>pi = 3.14159
price = 19.99
ratio = 0.5</code></pre>
</div>

<div class="warning-box">
    <strong>First Principles Caution:</strong> Due to binary representation, some decimal values cannot be represented exactly:
    <pre><code>result = 0.1 + 0.2
print(result)  # May not be exactly 0.3</code></pre>
</div>

<h4>3. String (str)</h4>
<div class="concept-box">
    <p>Sequences of Unicode characters enclosed in quotes. Strings are immutable at the fundamental level.</p>
</div>

<div class="worked-example">
    <pre><code>greeting = "Hello, World!"
author = 'Jane Doe'
path = """C:\\\\Users\\\\Data"""</code></pre>
</div>

<h4>4. Boolean (bool)</h4>
<div class="concept-box">
    <p>Values that are either True or False. Fundamentally, True equals 1 and False equals 0 in binary logic.</p>
</div>

<div class="worked-example">
    <pre><code>is_student = True
has_license = False
is_valid = (age >= 18)</code></pre>
</div>

<h4>5. None</h4>
<div class="concept-box">
    <p>The absence of a value. None is a singleton object representing null/undefined.</p>
</div>

<div class="worked-example">
    <pre><code>result = None\\nuser = None</code></pre>
</div>

<h3>Checking Data Types</h3>
<div class="worked-example">
    <p>Use the <code>type()</code> function to determine an object's data type:</p>
    <pre><code>print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("Hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'></code></pre>
</div>
'''
    },
    {
        'id': 'var_dt_03',
        'title': 'Memory and Identity',
        'body': '''
<h3>Object Identity: id() and Memory Addresses</h3>
<div class="concept-box">
    <p>Each object in Python occupies a specific location in memory. The <code>id()</code> function returns the memory address (identity) of an object, demonstrating first-principles memory allocation.</p>
</div>

<div class="worked-example">
    <pre><code>a = 100
b = 100
print(id(a))        # Memory address
print(id(b))        # May be same address (small integer caching)
print(a is b)       # True (due to Python's integer caching)</code></pre>
</div>

<h3>Reference vs. Value</h3>
<div class="concept-box">
    <p>Variables hold references to objects, not the values themselves. Multiple variables can reference the same object:</p>
</div>

<div class="worked-example">
    <pre><code>x = [1, 2, 3]
y = x
print(id(x) == id(y))  # True - same object in memory
y.append(4)
print(x)  # [1, 2, 3, 4] - x changed because x and y reference same list</code></pre>
</div>

<h3>Mutable vs. Immutable Types</h3>
<div class="concept-box">
    <p><strong>Immutable:</strong> Cannot be changed after creation (int, float, str, bool, None). Operations create new objects.</p>
    <p><strong>Mutable:</strong> Can be changed after creation (list, dict, set). Operations modify the existing object.</p>
</div>

<div class="worked-example">
    <p><strong>Immutable Example:</strong></p>
    <pre><code>text = "Hello"
print(id(text))
text = text + " World"  # Creates NEW string object
print(id(text))  # Different memory address</code></pre>
</div>

<div class="success-box">
    <p><strong>Key Insight:</strong> Understanding immutability is crucial for writing efficient Python code and avoiding unexpected behavior in complex programs.</p>
</div>
'''
    }
]
