# Input/Output

TITLE = "Input/Output"

SECTIONS = [
    {
        'id': 'io_01',
        'title': 'Output with print()',
        'body': '''
<h3>The print() Function</h3>
<div class="concept-box">
    <p>The <code>print()</code> function outputs text to the console (standard output stream). From a first-principles perspective, it's a built-in function that writes data to stdout.</p>
</div>

<h3>Basic Output</h3>
<div class="worked-example">
    <p><strong>Simple printing:</strong></p>
    <pre><code>print("Hello, World!")
print(42)
print(3.14)
print(True)</code></pre>
</div>

<h3>Printing Multiple Values</h3>
<div class="worked-example">
    <p><strong>Separate multiple items with commas:</strong></p>
    <pre><code>name = "Alice"
age = 30
print("Name:", name)        # "Name: Alice"
print(name, age)            # "Alice 30"
print(name, age, "years")   # "Alice 30 years"</code></pre>
</div>

<div class="concept-box">
    <p>By default, <code>print()</code> separates items with spaces and adds a newline at the end. Both behaviors can be customized with keyword arguments.</p>
</div>

<h3>Customizing print() Behavior</h3>

<h4>sep Parameter (Separator)</h4>
<div class="worked-example">
    <pre><code>print("apple", "banana", "cherry")
# Output: apple banana cherry

print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("one", "two", "three", sep="-")
# Output: one-two-three</code></pre>
</div>

<h4>end Parameter (Line Ending)</h4>
<div class="worked-example">
    <pre><code>print("Line 1")
print("Line 2")
# Output: (two separate lines)

print("No newline", end="")
print(" - same line")
# Output: No newline - same line (on one line)

print("Item:", end=" ")
print("Value")
# Output: Item: Value</code></pre>
</div>

<h4>Combining sep and end</h4>
<div class="worked-example">
    <pre><code>for i in range(1, 4):
    print(i, end=" | ")
print()  # Final newline
# Output: 1 | 2 | 3 |</code></pre>
</div>

<h3>Type Conversion in print()</h3>
<div class="concept-box">
    <p>The <code>print()</code> function automatically converts all arguments to strings before output, using each object's <code>__str__()</code> method.</p>
</div>

<div class="worked-example">
    <pre><code>number = 42
decimal = 3.14159
is_true = True

print(number)      # "42"
print(decimal)     # "3.14159"
print(is_true)     # "True"</code></pre>
</div>

<h3>Debugging with print()</h3>
<div class="success-box">
    <p><strong>First-Principles Debugging:</strong> Strategic <code>print()</code> statements help trace program execution and inspect variable values during development.</p>
</div>

<div class="worked-example">
    <pre><code>x = 5
y = 10
print(f"Debug: x={x}, y={y}")  # Output program state
result = x + y
print(f"Result: {result}")
print(f"Type: {type(result)}")  # Check data type</code></pre>
</div>
'''
    },
    {
        'id': 'io_02',
        'title': 'Input with input()',
        'body': '''
<h3>The input() Function</h3>
<div class="concept-box">
    <p>The <code>input()</code> function reads text from the console (standard input stream) and returns it as a string. It blocks program execution until the user presses Enter.</p>
</div>

<h3>Basic Input</h3>
<div class="worked-example">
    <p><strong>Simple user input:</strong></p>
    <pre><code>name = input()
print("You entered:", name)</code></pre>
</div>

<h3>Prompts</h3>
<div class="concept-box">
    <p>Include a prompt message inside <code>input()</code> to guide the user about what to enter.</p>
</div>

<div class="worked-example">
    <pre><code>name = input("What is your name? ")
age = input("How old are you? ")
print(f"{name} is {age} years old")</code></pre>
</div>

<h3>Important: input() Returns a String</h3>
<div class="warning-box">
    <strong>Critical First-Principles Concept:</strong> <code>input()</code> always returns a string, even if the user enters only numbers. Type conversion is required for numeric operations.
</div>

<div class="worked-example">
    <pre><code>age_input = input("Enter your age: ")
print(type(age_input))  # <class 'str'>

# Wrong (concatenates instead of adding):
result = age_input + 10  # TypeError: can't concatenate str and int

# Correct (convert to int first):
age = int(age_input)
next_year = age + 1
print(f"Next year you'll be {next_year}")</code></pre>
</div>

<h3>Multi-line Input</h3>
<div class="worked-example">
    <p><strong>Reading multiple values sequentially:</strong></p>
    <pre><code>name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

print(f"Contact: {name}, {email}, {phone}")</code></pre>
</div>

<h3>Input Validation Concepts</h3>
<div class="concept-box">
    <p>In practice, input validation checks if user data is in the expected format before using it. A first-principles approach requires explicit error handling.</p>
</div>

<div class="worked-example">
    <p><strong>Simple validation pattern:</strong></p>
    <pre><code>user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print(f"You entered {number}")
else:
    print("Invalid input. Please enter a number.")</code></pre>
</div>

<div class="success-box">
    <p><strong>Best Practice:</strong> Always validate and convert user input appropriately before using it in calculations or operations.</p>
</div>
'''
    },
    {
        'id': 'io_03',
        'title': 'Formatted Output',
        'body': '''
<h3>Print Formatting Techniques</h3>
<div class="concept-box">
    <p>Formatted output presents data in a controlled, readable way. Multiple approaches exist, each with different use cases.</p>
</div>

<h3>f-String Formatting (Modern Standard)</h3>
<div class="worked-example">
    <p><strong>Basic f-string printing:</strong></p>
    <pre><code>name = "Bob"
score = 95

print(f"Name: {name}")
print(f"Score: {score}")
print(f"{name} scored {score}%")</code></pre>
</div>

<div class="worked-example">
    <p><strong>Formatting numbers:</strong></p>
    <pre><code>pi = 3.14159265
price = 29.995

print(f"Pi rounded: {pi:.2f}")      # "Pi rounded: 3.14"
print(f"Price: ${price:.2f}")       # "Price: $30.00"
print(f"Large number: {1000000:,}") # "Large number: 1,000,000"</code></pre>
</div>

<h3>Column Alignment</h3>
<div class="worked-example">
    <p><strong>Aligned tabular data:</strong></p>
    <pre><code>items = [("apple", 5), ("banana", 3), ("cherry", 8)]

for item, count in items:
    print(f"{item:<10} {count:>3}")
# Output:
# apple         5
# banana        3
# cherry        8</code></pre>
</div>

<h3>format() Method</h3>
<div class="worked-example">
    <p><strong>Using the format() method:</strong></p>
    <pre><code>template = "Name: {}, Score: {}"
print(template.format("Alice", 92))

template2 = "Name: {name}, Score: {score}"
print(template2.format(name="Charlie", score=88))</code></pre>
</div>

<h3>Multiline Output</h3>
<div class="worked-example">
    <p><strong>Printing formatted blocks:</strong></p>
    <pre><code>name = "Eve"
age = 28

output = f"""
User Profile
============
Name: {name}
Age: {age}
Status: Active
"""

print(output)</code></pre>
</div>

<h3>String Concatenation for Output</h3>
<div class="concept-box">
    <p>Strings can be combined before printing, though f-strings are generally preferred for clarity.</p>
</div>

<div class="worked-example">
    <pre><code>greeting = "Hello"
name = "Frank"
message = greeting + ", " + name + "!"
print(message)  # "Hello, Frank!"

# Better with f-strings:
print(f"{greeting}, {name}!")</code></pre>
</div>
'''
    }
]
