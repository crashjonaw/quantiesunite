# Type Conversion

TITLE = "Type Conversion"

SECTIONS = [
    {
        'id': 'tc_01',
        'title': 'Explicit Type Conversion',
        'body': '''
<h3>What is Type Conversion?</h3>
<div class="concept-box">
    <p>Type conversion (also called type casting) is the process of converting a value from one data type to another. From a first-principles perspective, this involves creating a new object of the target type with the data from the source object.</p>
</div>

<h3>Converting to Integer: int()</h3>
<div class="worked-example">
    <p><strong>From string:</strong></p>
    <pre><code>age_str = "25"
age_int = int(age_str)      # 25
print(type(age_int))        # <class 'int'></code></pre>
</div>

<div class="worked-example">
    <p><strong>From float (truncates decimal):</strong></p>
    <pre><code>price = 19.99
quantity = int(price)       # 19 (decimal part removed)
print(quantity)</code></pre>
</div>

<div class="worked-example">
    <p><strong>From boolean:</strong></p>
    <pre><code>print(int(True))            # 1
print(int(False))           # 0</code></pre>
</div>

<div class="warning-box">
    <strong>Error Case:</strong> Converting invalid strings raises ValueError:
    <pre><code>result = int("abc")         # ValueError: invalid literal for int()
result = int("12.5")        # ValueError: invalid literal for int()</code></pre>
</div>

<h3>Converting to Float: float()</h3>
<div class="worked-example">
    <p><strong>From string:</strong></p>
    <pre><code>pi_str = "3.14159"
pi_float = float(pi_str)    # 3.14159
print(type(pi_float))       # <class 'float'></code></pre>
</div>

<div class="worked-example">
    <p><strong>From integer:</strong></p>
    <pre><code>count = 10
decimal_count = float(count)  # 10.0
print(decimal_count)</code></pre>
</div>

<div class="worked-example">
    <p><strong>Special float values:</strong></p>
    <pre><code>infinity = float("inf")     # Positive infinity
neg_infinity = float("-inf") # Negative infinity
not_a_number = float("nan")  # NaN (Not a Number)</code></pre>
</div>

<h3>Converting to String: str()</h3>
<div class="worked-example">
    <p><strong>From any type:</strong></p>
    <pre><code>number = 42
text = str(number)          # "42"
print(type(text))           # <class 'str'></code></pre>
</div>

<div class="worked-example">
    <pre><code>print(str(3.14))            # "3.14"
print(str(True))            # "True"
print(str(None))            # "None"
print(str([1, 2, 3]))       # "[1, 2, 3]"</code></pre>
</div>

<h3>Converting to Boolean: bool()</h3>
<div class="concept-box">
    <p>The <code>bool()</code> function converts values using Python's truthiness rules. Most values are "truthy", but certain values are "falsy".</p>
</div>

<div class="worked-example">
    <p><strong>Falsy values (convert to False):</strong></p>
    <pre><code>print(bool(0))              # False
print(bool(0.0))            # False
print(bool(""))             # False (empty string)
print(bool([]))             # False (empty list)
print(bool(None))           # False</code></pre>
</div>

<div class="worked-example">
    <p><strong>Truthy values (convert to True):</strong></p>
    <pre><code>print(bool(1))              # True
print(bool(-5))             # True
print(bool("Hello"))        # True (non-empty string)
print(bool([1, 2]))         # True (non-empty list)</code></pre>
</div>

<h3>Real-World Example: User Input</h3>
<div class="success-box">
    <p>Type conversion is essential when processing user input, which is always a string:</p>
</div>

<div class="worked-example">
    <pre><code># Get user input (always string)
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

# Convert to numbers
num1 = float(num1_str)
num2 = float(num2_str)

# Perform calculation
result = num1 + num2
print(f"Sum: {result}")</code></pre>
</div>
'''
    },
    {
        'id': 'tc_02',
        'title': 'Implicit Type Conversion (Coercion)',
        'body': '''
<h3>What is Implicit Type Conversion?</h3>
<div class="concept-box">
    <p>Implicit type conversion (coercion) occurs automatically when Python converts between types during operations. Unlike explicit conversion, the programmer doesn't explicitly call a conversion function.</p>
</div>

<h3>Numeric Type Promotion</h3>
<div class="concept-box">
    <p>When mixing int and float in arithmetic operations, Python automatically promotes int to float. The result is always float when floats are involved.</p>
</div>

<div class="worked-example">
    <p><strong>Integer and float mixing:</strong></p>
    <pre><code>x = 5          # int
y = 2.5        # float
result = x + y # 7.5 (float)
print(type(result))  # <class 'float'></code></pre>
</div>

<div class="worked-example">
    <pre><code>division = 10 / 4      # 2.5 (always float, even with int operands)
division2 = 10 // 4    # 2 (integer floor division)
product = 3 * 2.0      # 6.0 (float)</code></pre>
</div>

<h3>Boolean Coercion in Operations</h3>
<div class="worked-example">
    <p><strong>Booleans act as 0 and 1 in arithmetic:</strong></p>
    <pre><code>result = True + 5       # 6 (True is treated as 1)
result = False * 10     # 0 (False is treated as 0)
result = True + True    # 2</code></pre>
</div>

<h3>String Concatenation (No Coercion)</h3>
<div class="warning-box">
    <strong>Important Exception:</strong> Python does NOT implicitly convert non-strings when concatenating with strings. This raises a TypeError.
</div>

<div class="worked-example">
    <pre><code># This raises TypeError: can't concat str to int
result = "I am " + 25

# Solution: explicit conversion
result = "I am " + str(25)  # "I am 25"</code></pre>
</div>

<h3>Comparison Operations</h3>
<div class="worked-example">
    <p><strong>Comparing different numeric types works seamlessly:</strong></p>
    <pre><code>print(5 == 5.0)         # True (values are equal)
print(5 is 5.0)         # False (different types, different objects)
print(10 > 9.5)         # True</code></pre>
</div>

<div class="warning-box">
    <strong>Avoid comparing different types loosely:</strong> While numeric comparisons work, comparing strings to numbers always returns False (never raises error).
    <pre><code>print("5" == 5)         # False (string vs int)
print("5" < 10)         # TypeError in Python 3</code></pre>
</div>

<h3>Container Type Conversion</h3>
<div class="concept-box">
    <p>Python provides functions to convert between container types (list, tuple, set, dict).</p>
</div>

<div class="worked-example">
    <p><strong>Converting collections:</strong></p>
    <pre><code>string = "hello"
print(list(string))        # ['h', 'e', 'l', 'l', 'o']

numbers = [1, 2, 3]
print(tuple(numbers))      # (1, 2, 3)

items = [1, 2, 2, 3, 3, 3]
print(set(items))          # {1, 2, 3} (removes duplicates)</code></pre>
</div>
'''
    },
    {
        'id': 'tc_03',
        'title': 'Type Checking and Conversion Strategy',
        'body': '''
<h3>Checking Types Before Conversion</h3>
<div class="concept-box">
    <p>Best practice: validate data type before conversion to handle errors gracefully. Use helper functions and conditional logic.</p>
</div>

<h3>isinstance() Function</h3>
<div class="worked-example">
    <p><strong>Check if variable is a specific type:</strong></p>
    <pre><code>value = 42

print(isinstance(value, int))      # True
print(isinstance(value, float))    # False
print(isinstance(value, str))      # False</code></pre>
</div>

<div class="worked-example">
    <p><strong>Check multiple types at once:</strong></p>
    <pre><code>value = 3.14
print(isinstance(value, (int, float)))  # True
print(isinstance(value, (int, str)))    # False</code></pre>
</div>

<h3>Safe Conversion Pattern</h3>
<div class="worked-example">
    <p><strong>Convert with error handling:</strong></p>
    <pre><code>user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"Converted: {number}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")</code></pre>
</div>

<h3>Type Conversion Strategy</h3>
<div class="concept-box">
    <p>A first-principles approach to type conversion:</p>
    <ol>
        <li><strong>Validate:</strong> Check the input type and format</li>
        <li><strong>Convert:</strong> Explicitly convert to target type</li>
        <li><strong>Verify:</strong> Confirm conversion succeeded and result is expected</li>
    </ol>
</div>

<div class="worked-example">
    <p><strong>Complete safe conversion example:</strong></p>
    <pre><code>def get_positive_integer(prompt):
    """Safely get and convert user input to positive integer."""
    while True:
        user_input = input(prompt)

        # Check if string contains only digits
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a valid integer.")

age = get_positive_integer("Enter your age: ")
print(f"You are {age} years old.")</code></pre>
</div>

<h3>Common Conversion Use Cases</h3>

<h4>Reading Numeric Input</h4>
<div class="worked-example">
    <pre><code>height = float(input("Height (m): "))  # Always convert input
weight = float(input("Weight (kg): "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")</code></pre>
</div>

<h4>Formatting Output</h4>
<div class="worked-example">
    <pre><code>score = 95
total = 100
percentage = (score / total) * 100
print(f"Score: {int(percentage)}%")</code></pre>
</div>

<h4>Data Processing</h4>
<div class="worked-example">
    <pre><code>csv_data = "1,2,3,4,5"  # String from file
numbers = [int(x) for x in csv_data.split(",")]
print(sum(numbers))  # 15</code></pre>
</div>

<div class="success-box">
    <p><strong>Key Principle:</strong> Always be explicit about type conversions. Clear, intentional conversion makes code maintainable and prevents subtle bugs.</p>
</div>
'''
    }
]
