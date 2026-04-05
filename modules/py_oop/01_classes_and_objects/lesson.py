# Classes and Objects: First Principles

SECTIONS = [
    {
        'id': 'py_oop_01_01',
        'title': 'What are Classes?',
        'body': '''
<h2 class="accent-heading">Classes and Objects: First Principles</h2>

<div class="concept-box">
<h3>Core Concept: What is a Class?</h3>
<p>A <strong>class</strong> is a blueprint or template for creating objects. It defines the structure and behavior that instances will have. Think of a class as an architectural blueprint, and instances as the actual buildings constructed from that blueprint.</p>
</div>

<h3>The Relationship Between Classes and Objects</h3>
<p>A <strong>class</strong> is an abstract definition, while an <strong>object</strong> (instance) is a concrete realization of that definition.</p>

<div class="worked-example">
# Defining a simple class
class Dog:
    """A class representing a dog"""
    pass

# Creating instances (objects) from the class
my_dog = Dog()
your_dog = Dog()

# Both are instances of the Dog class
print(type(my_dog))  # <class '__main__.Dog'>
print(isinstance(my_dog, Dog))  # True
</div>

<h3>Key Principles</h3>
<ul>
<li><strong>Abstraction:</strong> Classes abstract away complexity by grouping related data and behavior</li>
<li><strong>Encapsulation:</strong> Classes bundle data and methods together</li>
<li><strong>Reusability:</strong> Once defined, a class can create unlimited instances</li>
</ul>

<div class="success-box">
<strong>Key Takeaway:</strong> Classes are blueprints; objects are instances created from those blueprints. Every Python object is an instance of some class.
</div>
'''
    },
    {
        'id': 'py_oop_01_02',
        'title': 'Class Definition and Instantiation',
        'body': '''
<h2 class="accent-heading">Class Definition and Instantiation</h2>

<div class="concept-box">
<h3>Defining a Class</h3>
<p>The <code>class</code> keyword creates a new class. The syntax is simple: <code>class ClassName:</code> followed by an indented block of code that defines the class body.</p>
</div>

<h3>The `__init__` Method</h3>
<p>The `__init__` method is the constructor. It's automatically called when you create a new instance and is where you initialize instance attributes.</p>

<div class="worked-example">
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

# Instantiation: calling Person(...) creates a new object
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.describe())  # Alice is 30 years old
print(bob.describe())    # Bob is 25 years old
print(alice.name)       # Alice
</div>

<h3>Understanding `self`</h3>
<p>The first parameter of instance methods is `self`, which refers to the specific instance calling the method. It's automatically passed by Python.</p>

<div class="warning-box">
<strong>Common Mistake:</strong> Don't include `self` when calling methods on an instance. Write `alice.describe()` not `alice.describe(alice)`. Python passes `self` automatically.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Classes are blueprints with `__init__` initializers. Calling a class creates an instance. The `self` parameter always refers to the current instance.
</div>
'''
    },
    {
        'id': 'py_oop_01_03',
        'title': 'Instance and Class Attributes',
        'body': '''
<h2 class="accent-heading">Instance vs Class Attributes</h2>

<h3>Instance Attributes</h3>
<p>Instance attributes are unique to each object. They're typically set in `__init__` using `self.attribute_name`.</p>

<div class="worked-example">
class Car:
    def __init__(self, color, brand):
        self.color = color  # Instance attribute
        self.brand = brand  # Instance attribute

car1 = Car("red", "Toyota")
car2 = Car("blue", "Honda")

print(car1.color)  # red
print(car2.color)  # blue (different instance, different value)
</div>

<h3>Class Attributes</h3>
<p>Class attributes are shared by all instances of the class. They're defined directly in the class body, outside of methods.</p>

<div class="worked-example">
class Species:
    kingdom = "Animalia"  # Class attribute (shared by all instances)

    def __init__(self, name):
        self.name = name  # Instance attribute (unique to each instance)

dog = Species("Dog")
cat = Species("Cat")

print(dog.kingdom)   # Animalia (shared)
print(cat.kingdom)   # Animalia (shared)
print(dog.name)      # Dog (unique)
print(cat.name)      # Cat (unique)
</div>

<div class="warning-box">
<strong>Caution:</strong> Modifying a class attribute affects all instances. Modifying an instance attribute affects only that instance.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use instance attributes for data unique to each object. Use class attributes for data shared across all instances.
</div>
'''
    },
    {
        'id': 'py_oop_01_04',
        'title': 'Object Identity and Equality',
        'body': '''
<h2 class="accent-heading">Object Identity and Equality</h2>

<div class="concept-box">
<h3>Identity vs Equality</h3>
<p><strong>Identity</strong> (using `is`) checks if two variables refer to the same object in memory. <strong>Equality</strong> (using `==`) checks if two objects have equal values.</p>
</div>

<h3>Using `is` for Identity</h3>
<p>The `is` operator checks memory identity using `id()`.</p>

<div class="worked-example">
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 0)
p2 = Point(0, 0)
p3 = p1

print(p1 is p2)      # False (different objects in memory)
print(p1 is p3)      # True (same object)
print(id(p1))        # Shows memory address
print(id(p2))        # Different address
</div>

<h3>Using `==` for Equality</h3>
<p>By default, `==` checks identity for custom classes. To customize equality, define `__eq__`.</p>

<div class="worked-example">
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(0, 0)
p2 = Point(0, 0)

print(p1 == p2)      # True (same values)
print(p1 is p2)      # False (different objects)
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use `is` for identity checks. Use `==` for value equality. Override `__eq__` to define custom equality.
</div>
'''
    }
]
