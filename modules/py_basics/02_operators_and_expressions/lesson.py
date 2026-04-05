# Operators and Expressions

TITLE = "Operators and Expressions"

SECTIONS = [
    {
        'id': 'op_expr_01',
        'title': 'Arithmetic Operators',
        'body': '''
<h3>Basic Arithmetic Operations</h3>
<div class="concept-box">
    <p>Arithmetic operators perform mathematical calculations. From a first-principles perspective, the CPU executes these as low-level machine instructions.</p>
</div>

<h4>Addition and Subtraction</h4>
<div class="worked-example">
    <pre><code>a = 10
b = 3

sum_result = a + b       # 13
diff_result = a - b      # 7
negative = -b            # -3</code></pre>
</div>

<h4>Multiplication and Division</h4>
<div class="worked-example">
    <pre><code>a = 10
b = 3

product = a * b          # 30
quotient = a / b         # 3.333... (float division)
integer_div = a // b     # 3 (floor division)
remainder = a % b        # 1 (modulo/remainder)</code></pre>
</div>

<div class="warning-box">
    <strong>First Principles:</strong> The <code>/</code> operator always returns a float, even with whole number operands. The <code>//</code> operator performs floor division (rounds toward negative infinity).
</div>

<h4>Exponentiation</h4>
<div class="worked-example">
    <pre><code>base = 2
exponent = 3
result = base ** exponent  # 8 (2 raised to power 3)
square_root = 16 ** 0.5    # 4.0 (using fractional exponents)</code></pre>
</div>

<h3>Operator Precedence</h3>
<div class="concept-box">
    <p>Python follows the standard mathematical order of operations (PEMDAS):</p>
    <ol>
        <li>Parentheses: <code>()</code></li>
        <li>Exponentiation: <code>**</code></li>
        <li>Multiplication/Division: <code>*</code>, <code>/</code>, <code>//</code>, <code>%</code></li>
        <li>Addition/Subtraction: <code>+</code>, <code>-</code></li>
    </ol>
</div>

<div class="worked-example">
    <p><strong>Precedence Example:</strong></p>
    <pre><code>result = 2 + 3 * 4      # 14 (not 20, multiplication first)
result = (2 + 3) * 4    # 20 (parentheses override precedence)
result = 2 ** 3 ** 2    # 512 (right-associative: 2^(3^2) = 2^9)</code></pre>
</div>

<h3>Augmented Assignment Operators</h3>
<div class="worked-example">
    <p>Combine assignment with operations for concise code:</p>
    <pre><code>x = 10
x += 5      # x = x + 5  → 15
x -= 3      # x = x - 3  → 12
x *= 2      # x = x * 2  → 24
x /= 4      # x = x / 4  → 6.0
x //= 2     # x = x // 2 → 3.0
x **= 2     # x = x ** 2 → 9.0
x %= 5      # x = x % 5  → 4.0</code></pre>
</div>
'''
    },
    {
        'id': 'op_expr_02',
        'title': 'Comparison and Logical Operators',
        'body': '''
<h3>Comparison Operators</h3>
<div class="concept-box">
    <p>Comparison operators test relationships between values and return boolean results (True or False). These evaluate to single Boolean objects.</p>
</div>

<div class="worked-example">
    <pre><code>a = 10
b = 5

print(a > b)       # True
print(a < b)       # False
print(a == b)      # False (equality)
print(a != b)      # True (not equal)
print(a >= b)      # True (greater than or equal)
print(a <= b)      # False (less than or equal)</code></pre>
</div>

<div class="warning-box">
    <strong>Critical:</strong> Use <code>==</code> for value comparison and <code>is</code> for identity comparison (checking if variables reference the same object in memory).
    <pre><code>a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)      # True (equal values)
print(a is b)      # False (different objects in memory)</code></pre>
</div>

<h3>Logical Operators</h3>
<div class="concept-box">
    <p>Logical operators combine boolean values using AND, OR, and NOT logic.</p>
</div>

<h4>and Operator</h4>
<div class="worked-example">
    <pre><code>age = 25
has_license = True

can_drive = (age >= 18) and has_license  # True
print(can_drive)</code></pre>
</div>

<p>Truth table for <code>and</code>:</p>
<div class="worked-example">
    <pre><code>True and True    # True
True and False   # False
False and True   # False
False and False  # False</code></pre>
</div>

<h4>or Operator</h4>
<div class="worked-example">
    <pre><code>is_weekend = True
is_holiday = False

day_off = is_weekend or is_holiday  # True
print(day_off)</code></pre>
</div>

<h4>not Operator</h4>
<div class="worked-example">
    <pre><code>is_raining = True
can_go_outside = not is_raining  # False
print(can_go_outside)</code></pre>
</div>

<h3>Short-Circuit Evaluation</h3>
<div class="concept-box">
    <p>Python evaluates logical expressions from left to right and stops as soon as the result is determined (first-principles efficiency).</p>
</div>

<div class="worked-example">
    <pre><code># 'and' stops at first False
result = False and expensive_function()  # expensive_function NOT called

# 'or' stops at first True
result = True or expensive_function()    # expensive_function NOT called</code></pre>
</div>

<div class="success-box">
    <p><strong>Performance Insight:</strong> Use short-circuit evaluation strategically to avoid unnecessary computations.</p>
</div>
'''
    },
    {
        'id': 'op_expr_03',
        'title': 'String and Membership Operators',
        'body': '''
<h3>String Operators</h3>
<div class="concept-box">
    <p>Python provides special operators for string manipulation, demonstrating how operators can be overloaded for different types.</p>
</div>

<h4>Concatenation with +</h4>
<div class="worked-example">
    <pre><code>first = "Hello"
second = "World"
greeting = first + " " + second  # "Hello World"</code></pre>
</div>

<h4>Repetition with *</h4>
<div class="worked-example">
    <pre><code>dash = "-"
border = dash * 20  # "--------------------"
word = "Ha"
laugh = word * 3    # "HaHaHa"</code></pre>
</div>

<h3>Membership Operators</h3>
<div class="concept-box">
    <p>The <code>in</code> and <code>not in</code> operators check if a value exists within a sequence.</p>
</div>

<div class="worked-example">
    <pre><code>text = "Python is awesome"
print("Python" in text)        # True
print("Java" in text)          # False
print("Java" not in text)      # True

letters = ['a', 'e', 'i', 'o', 'u']
print('a' in letters)          # True
print('b' in letters)          # False</code></pre>
</div>

<h3>Operator Overloading Principle</h3>
<div class="concept-box">
    <p>The same operator (<code>+</code>, <code>*</code>, etc.) behaves differently based on data type. This is operator overloading—a first-principles object-oriented programming concept.</p>
</div>

<div class="worked-example">
    <p><strong>Same operator, different behavior:</strong></p>
    <pre><code>result = 5 + 3          # Addition: 8 (int)
result = "5" + "3"      # Concatenation: "53" (str)
result = [1] + [2]      # Concatenation: [1, 2] (list)</code></pre>
</div>
'''
    }
]
