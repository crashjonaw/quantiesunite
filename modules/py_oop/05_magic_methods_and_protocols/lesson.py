# Magic Methods and Protocols: Advanced Customization

SECTIONS = [
    {
        'id': 'py_oop_05_01',
        'title': 'Introduction to Magic Methods',
        'body': '''
<h2 class="accent-heading">Magic Methods and Protocols</h2>

<div class="concept-box">
<h3>What are Magic Methods?</h3>
<p>Magic methods (or dunder methods) are special methods with double underscores (`__name__`). Python calls them automatically in response to built-in operations. They enable customization of how objects behave with operators, functions, and language constructs.</p>
</div>

<h3>Object Lifecycle Magic Methods</h3>

<div class="worked-example">
class Resource:
    def __new__(cls):
        """Called before __init__ to create the instance"""
        print("Creating instance...")
        return super().__new__(cls)

    def __init__(self):
        """Called after __new__ to initialize the instance"""
        print("Initializing instance...")
        self.name = "Resource"

    def __del__(self):
        """Called when instance is about to be destroyed"""
        print(f"Destroying {self.name}...")

r = Resource()
# Creating instance...
# Initializing instance...
del r
# Destroying Resource...
</div>

<h3>String Representation Magic Methods</h3>

<div class="worked-example">
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Readable string (for end users)"""
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(str(p))   # Alice, 30 years old
print(repr(p))  # Person('Alice', 30)
print(f"{p}")   # Alice, 30 years old (uses __str__)
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Magic methods customize object behavior. Implement `__init__`, `__str__`, and `__repr__` in every class for clarity.
</div>
'''
    },
    {
        'id': 'py_oop_05_02',
        'title': 'Container Protocols',
        'body': '''
<h2 class="accent-heading">Container Protocols</h2>

<div class="concept-box">
<h3>Making Your Class Behave Like a Container</h3>
<p>By implementing container magic methods, your objects can behave like lists, dicts, or other containers. This requires `__len__`, `__getitem__`, `__setitem__`, and `__delitem__`.</p>
</div>

<h3>Implementing the Sequence Protocol</h3>

<div class="worked-example">
class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        """Returns number of items"""
        return len(self.songs)

    def __getitem__(self, index):
        """Access items with []"""
        return self.songs[index]

    def __setitem__(self, index, value):
        """Set items with []"""
        self.songs[index] = value

    def __delitem__(self, index):
        """Delete items with del"""
        del self.songs[index]

    def add(self, song):
        self.songs.append(song)

playlist = Playlist()
playlist.add("Song A")
playlist.add("Song B")

print(len(playlist))      # 2
print(playlist[0])        # Song A
playlist[0] = "Song C"
print(playlist[0])        # Song C
</div>

<h3>Making Objects Iterable</h3>

<div class="worked-example">
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """Returns an iterator"""
        self.current = self.start
        return self

    def __next__(self):
        """Returns the next value"""
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for i in Range(1, 4):
    print(i)  # 1, 2, 3
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Implement container protocols to make custom objects work with Python's built-in functions like `len()`, subscripting, and `for` loops.
</div>
'''
    },
    {
        'id': 'py_oop_05_03',
        'title': 'Context Managers and Protocols',
        'body': '''
<h2 class="accent-heading">Context Managers and Protocols</h2>

<div class="concept-box">
<h3>The Context Manager Protocol</h3>
<p>Context managers enable setup and cleanup code using the `with` statement. Implement `__enter__` and `__exit__` to create context managers.</p>
</div>

<h3>Creating a Context Manager</h3>

<div class="worked-example">
class Database:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}...")
        self.connection = f"Connection to {self.filename}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block (always called)"""
        print(f"Closing {self.filename}...")
        # Return True to suppress exceptions
        return False

with Database("mydb.db") as db:
    print(f"Using {db}")
    # Closing happens automatically
</div>

<h3>Exception Handling in Context Managers</h3>

<div class="worked-example">
class FileHandler:
    def __enter__(self):
        print("Opening file...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}")
        return False  # Let exceptions propagate

try:
    with FileHandler():
        print("Doing work...")
        raise ValueError("Oops!")
except ValueError:
    print("Caught the error")
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use context managers to ensure cleanup code runs. The `with` statement guarantees `__exit__` is called, even on exceptions.
</div>
'''
    },
    {
        'id': 'py_oop_05_04',
        'title': 'Callable Objects and Descriptors',
        'body': '''
<h2 class="accent-heading">Callable Objects and Descriptors</h2>

<h3>Callable Objects with `__call__`</h3>
<p>Implement `__call__` to make instances behave like functions.</p>

<div class="worked-example">
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Makes instances callable like functions"""
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
</div>

<h3>Descriptors</h3>
<p>Descriptors customize attribute access using `__get__`, `__set__`, and `__delete__`.</p>

<div class="worked-example">
class ValidatedString:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, "")

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        obj.__dict__[self.name] = value

class Person:
    name = ValidatedString("name")

    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)       # Alice
# p.name = 123      # Raises TypeError!
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use `__call__` for callable objects. Use descriptors for advanced attribute control and validation.
</div>
'''
    }
]
