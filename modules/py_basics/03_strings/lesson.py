# Strings

TITLE = "Strings"

SECTIONS = [
    {
        'id': 'str_01',
        'title': 'String Fundamentals',
        'body': '''
<h3>What Are Strings?</h3>
<div class="concept-box">
    <p>A string is a sequence of Unicode characters. From a first-principles perspective, a string is:</p>
    <ul>
        <li>An immutable sequence (cannot be modified after creation)</li>
        <li>Stored as Unicode codepoints in memory</li>
        <li>An iterable object (can loop through characters)</li>
    </ul>
</div>

<h3>Creating Strings</h3>
<div class="worked-example">
    <p><strong>Single and Double Quotes:</strong></p>
    <pre><code>single_quote = "Hello"
double_quote = "World"
# Both are equivalent; choose consistently</code></pre>
</div>

<div class="worked-example">
    <p><strong>Triple Quotes (Multiline):</strong></p>
    <pre><code>multiline = """This is a longer string
spanning multiple lines.
Useful for longer text blocks."""

poem = "Roses are red,\\nViolets are blue,\\nStrings are immutable,\\nThat much is true."</code></pre>
</div>

<h3>Escaping Special Characters</h3>
<div class="concept-box">
    <p>Special characters require escape sequences (backslash notation) to be included in strings.</p>
</div>

<div class="worked-example">
    <pre><code>newline = "Line 1\\nLine 2"
tab = "Column1\\tColumn2"
quote = "He said \\"Hello\\""
backslash = "Path: C:\\\\Users"
unicode = "Unicode: \\u03B1\\u03B2"</code></pre>
</div>

<h3>String Length and Indexing</h3>
<div class="concept-box">
    <p>Strings are sequences with zero-based indexing. Access individual characters by position or slice ranges.</p>
</div>

<div class="worked-example">
    <p><strong>Length and Character Access:</strong></p>
    <pre><code>word = "Python"
print(len(word))       # 6

print(word[0])         # P (first character)
print(word[5])         # n (last character)
print(word[-1])        # n (last, using negative index)
print(word[-2])        # o (second from end)</code></pre>
</div>

<div class="warning-box">
    <strong>Immutability:</strong> You cannot modify a string character directly. Attempting word[0] = J raises a TypeError. Instead, create a new string.
</div>

<h3>String Slicing</h3>
<div class="worked-example">
    <p><strong>Extracting Substrings:</strong></p>
    <pre><code>text = "Python Programming"

print(text[0:6])       # Python
print(text[7:])        # Programming (to end)
print(text[:6])        # Python (from start)
print(text[::2])       # PtoPomig (every 2nd character)
print(text[::-1])      # gnimmargorP nohtyP (reversed)</code></pre>
</div>

<div class="success-box">
    <p><strong>Slicing Syntax:</strong> string[start:end:step] where start and end are exclusive/inclusive respectively.</p>
</div>
'''
    },
    {
        'id': 'str_02',
        'title': 'String Methods and Formatting',
        'body': '''
<h3>Common String Methods</h3>
<div class="concept-box">
    <p>String methods are functions built into the string object. They do not modify the original string (due to immutability) but return new string objects.</p>
</div>

<h4>Case Conversion</h4>
<div class="worked-example">
    <pre><code>text = "Hello World"

print(text.upper())           # HELLO WORLD
print(text.lower())           # hello world
print(text.title())           # Hello World
print(text.capitalize())      # Hello world
print(text.swapcase())        # hELLO wORLD</code></pre>
</div>

<h4>Searching and Replacing</h4>
<div class="worked-example">
    <pre><code>sentence = "The quick brown fox jumps over the lazy dog"

print(sentence.find("quick"))        # 4 (index where found)
print(sentence.find("xyz"))          # -1 (not found)
print(sentence.count("o"))           # 4 (occurrences)
print(sentence.replace("fox", "cat")) # Returns new string with replacement
print(sentence.startswith("The"))    # True
print(sentence.endswith("dog"))      # True</code></pre>
</div>

<h4>Trimming and Splitting</h4>
<div class="worked-example">
    <pre><code>text = "  Hello, World!  "

print(text.strip())            # Hello, World! (remove leading/trailing whitespace)
print(text.lstrip())           # Hello, World!
print(text.rstrip())           #   Hello, World!

words = "apple,banana,cherry"
print(words.split(","))        # [apple, banana, cherry]

lines = "One\\nTwo\\nThree"
print(lines.split("\\n"))      # [One, Two, Three]</code></pre>
</div>

<h3>String Formatting</h3>
<div class="concept-box">
    <p>Python provides multiple approaches to format strings with dynamic values. The most modern is f-strings (f-string literals).</p>
</div>

<h4>f-Strings (Recommended)</h4>
<div class="worked-example">
    <p><strong>Simple substitution:</strong></p>
    <pre><code>name = "Alice"
age = 30
text = f"My name is {name} and I am {age} years old"
print(text)  # My name is Alice and I am 30 years old</code></pre>
</div>

<div class="worked-example">
    <p><strong>Expressions inside f-strings:</strong></p>
    <pre><code>x = 5
y = 3
result = f"The sum of {x} and {y} is {x + y}"
print(result)  # The sum of 5 and 3 is 8</code></pre>
</div>

<h4>format() Method</h4>
<div class="worked-example">
    <pre><code>text = "Hello, {}! You have {} messages."
print(text.format("Bob", 5))
# Hello, Bob! You have 5 messages.

template = "{name} is {age} years old"
print(template.format(name="Charlie", age=25))
# Charlie is 25 years old</code></pre>
</div>

<h4>Old-Style % Formatting (Legacy)</h4>
<div class="worked-example">
    <pre><code>name = "David"
age = 35
text = "My name is %s and I am %d years old" % (name, age)
print(text)  # My name is David and I am 35 years old</code></pre>
</div>

<h3>Format Specifiers</h3>
<div class="worked-example">
    <p><strong>Controlling decimal places and alignment:</strong></p>
    <pre><code>price = 19.5678
print(f"Price: ${price:.2f}")          # Price: $19.57

number = 42
print(f"Number: {number:05d}")         # Number: 00042

text = "Python"
print(f"{text:>10}")                   #     Python (right-aligned)
print(f"{text:<10}")                   # Python     (left-aligned)
print(f"{text:^10}")                   #   Python   (centered)</code></pre>
</div>
'''
    },
    {
        'id': 'str_03',
        'title': 'String Iteration and Advanced Concepts',
        'body': '''
<h3>Iterating Through Strings</h3>
<div class="concept-box">
    <p>Strings are iterable sequences. You can loop through each character using a for loop.</p>
</div>

<div class="worked-example">
    <p><strong>Character-by-character iteration:</strong></p>
    <pre><code>word = "Python"

for char in word:
    print(char)
# Output: P, y, t, h, o, n (each on separate line)</code></pre>
</div>

<div class="worked-example">
    <p><strong>Using enumerate() for index and character:</strong></p>
    <pre><code>word = "Code"

for index, char in enumerate(word):
    print(f"{index}: {char}")
# Output: 0: C, 1: o, 2: d, 3: e</code></pre>
</div>

<h3>String Membership Testing</h3>
<div class="concept-box">
    <p>The in operator checks if a substring exists within a string.</p>
</div>

<div class="worked-example">
    <pre><code>text = "Python is powerful"

print("Python" in text)      # True
print("java" in text)        # False
print("is" in text)          # True
print("xyz" not in text)     # True</code></pre>
</div>

<h3>String Comparison</h3>
<div class="concept-box">
    <p>Strings are compared lexicographically (dictionary order), using Unicode codepoint values at the first differing character.</p>
</div>

<div class="worked-example">
    <pre><code>print("apple" < "banana")    # True (lexicographic comparison)
print("apple" == "apple")    # True
print("Apple" < "apple")     # True (uppercase < lowercase in ASCII)</code></pre>
</div>

<h3>Raw Strings</h3>
<div class="concept-box">
    <p>Raw strings (prefixed with r) treat backslashes as literal characters, ignoring escape sequences. Useful for file paths and regular expressions.</p>
</div>

<div class="worked-example">
    <pre><code>normal_path = "C:\\\\Users\\\\Data"
raw_path = r"C:\\Users\\Data"
# Both represent the same path, raw strings are more readable

regex = r"\\d{3}-\\d{3}-\\d{4}"  # Phone number pattern
print(regex)  # \\d{3}-\\d{3}-\\d{4} (backslashes preserved)</code></pre>
</div>

<h3>String Interning and Memory</h3>
<div class="concept-box">
    <p>Python caches certain string values (a first-principles optimization). Short strings and strings without special characters may share memory locations.</p>
</div>

<div class="worked-example">
    <pre><code>a = "hello"
b = "hello"
print(a is b)              # True (interned—same memory location)

c = "hello world"
d = "hello world"
print(c is d)              # May be True or False (implementation detail)</code></pre>
</div>
'''
    }
]
