# Attributes and Methods: Behavior and State

SECTIONS = [
    {
        'id': 'py_oop_02_01',
        'title': 'Methods: Functions in Classes',
        'body': '''
<h2 class="accent-heading">Methods: Functions in Classes</h2>

<div class="concept-box">
<h3>What are Methods?</h3>
<p>Methods are functions defined inside a class. They operate on the data (attributes) of an instance. Methods enable objects to have behavior beyond just storing data.</p>
</div>

<h3>Instance Methods</h3>
<p>Instance methods take `self` as the first parameter and can access/modify instance data.</p>

<div class="worked-example">
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Instance method to deposit money"""
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        """Instance method to withdraw money"""
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds"

account = BankAccount("Alice", 1000)
print(account.deposit(500))    # Deposited 500. New balance: 1500
print(account.withdraw(200))   # Withdrew 200. New balance: 1300
</div>

<h3>Method Chaining</h3>
<p>Methods can return `self` to enable chaining multiple method calls.</p>

<div class="worked-example">
class Builder:
    def __init__(self):
        self.value = 0

    def add(self, n):
        self.value += n
        return self  # Return self for chaining

    def multiply(self, n):
        self.value *= n
        return self

result = Builder().add(5).multiply(2).add(3).value
print(result)  # 13 ((5 * 2) + 3)
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Methods define how objects behave. Return `self` from methods to enable method chaining for fluent interfaces.
</div>
'''
    },
    {
        'id': 'py_oop_02_02',
        'title': 'Class Methods and Static Methods',
        'body': '''
<h2 class="accent-heading">Class Methods and Static Methods</h2>

<div class="concept-box">
<h3>Class Methods</h3>
<p>Class methods use the `@classmethod` decorator and receive the class itself (`cls`) as the first parameter instead of an instance (`self`). They can access and modify class-level state.</p>
</div>

<div class="worked-example">
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return f"Total instances: {cls.count}"

c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # Total instances: 2
</div>

<h3>Static Methods</h3>
<p>Static methods use the `@staticmethod` decorator. They don't receive `self` or `cls` and cannot access instance or class state.</p>

<div class="worked-example">
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_positive(n):
        return n > 0

print(Math.add(5, 3))        # 8
print(Math.is_positive(-5))  # False

# Can call on instances too (though unusual)
m = Math()
print(m.add(2, 3))           # 5
</div>

<h3>When to Use What</h3>
<ul>
<li><strong>Instance methods:</strong> Work with instance data (most common)</li>
<li><strong>Class methods:</strong> Work with class data or alternative constructors</li>
<li><strong>Static methods:</strong> Utility functions logically grouped with the class</li>
</ul>

<div class="success-box">
<strong>Key Takeaway:</strong> Use decorators to create different method types. Instance methods are most common. Class methods work with shared state. Static methods are utilities.
</div>
'''
    },
    {
        'id': 'py_oop_02_03',
        'title': 'Properties and Getters/Setters',
        'body': '''
<h2 class="accent-heading">Properties and Getters/Setters</h2>

<div class="concept-box">
<h3>Properties: Pythonic Getters and Setters</h3>
<p>Properties let you use getters and setters while maintaining attribute-like access syntax. Use the `@property` decorator for getters and `@name.setter` for setters.</p>
</div>

<h3>Using Properties</h3>

<div class="worked-example">
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Private by convention

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32

temp = Temperature(0)
print(temp.celsius)      # 0 (uses getter)
print(temp.fahrenheit)   # 32.0 (computed)
temp.celsius = 100       # Uses setter
print(temp.fahrenheit)   # 212.0
</div>

<h3>Why Properties Matter</h3>
<p>Properties allow you to add validation and computation while keeping a clean interface. You can change implementation details without breaking the API.</p>

<div class="warning-box">
<strong>Convention:</strong> Use `_name` (single underscore) for internal attributes that shouldn't be accessed directly from outside.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use properties to validate data and compute values while maintaining attribute-like syntax. This follows the principle of least surprise.
</div>
'''
    },
    {
        'id': 'py_oop_02_04',
        'title': 'Working with Attributes Dynamically',
        'body': '''
<h2 class="accent-heading">Working with Attributes Dynamically</h2>

<div class="concept-box">
<h3>Introspection: Inspecting Objects</h3>
<p>Python provides tools to inspect object attributes at runtime using `getattr()`, `setattr()`, `hasattr()`, and `dir()`.</p>
</div>

<h3>Using getattr, setattr, hasattr</h3>

<div class="worked-example">
class Config:
    def __init__(self):
        self.debug = True
        self.port = 8000

config = Config()

# Check if attribute exists
if hasattr(config, 'debug'):
    print("Has debug")

# Get attribute value (with default)
port = getattr(config, 'port', 5000)
print(port)  # 8000

# Set attribute value
setattr(config, 'host', 'localhost')
print(config.host)  # localhost

# List all attributes
print(dir(config))  # Shows all attributes and methods
</div>

<h3>The `__dict__` Attribute</h3>
<p>Every instance has a `__dict__` dictionary containing its attributes.</p>

<div class="worked-example">
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.__dict__)           # {'name': 'Alice'}
print(vars(p))              # Same as __dict__

# Modify via __dict__
p.__dict__['age'] = 30
print(p.age)                # 30
</div>

<div class="warning-box">
<strong>Caution:</strong> Dynamic attribute access is powerful but can make code harder to understand. Use it carefully and document when attributes are expected.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use introspection tools to work with attributes dynamically. `__dict__` gives you full access to an object's state.
</div>
'''
    }
]
