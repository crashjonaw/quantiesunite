# Encapsulation and Polymorphism: Data Protection and Flexibility

SECTIONS = [
    {
        'id': 'py_oop_04_01',
        'title': 'Encapsulation: Data Hiding',
        'body': '''
<h2 class="accent-heading">Encapsulation: Data Hiding</h2>

<div class="concept-box">
<h3>What is Encapsulation?</h3>
<p>Encapsulation is the bundling of data (attributes) and methods together while hiding internal implementation details. It protects object state from unauthorized access and modification.</p>
</div>

<h3>Access Modifiers in Python</h3>
<p>Python uses naming conventions to indicate access levels:</p>

<div class="worked-example">
class BankAccount:
    def __init__(self, balance):
        self.public = "Anyone can access"
        self._protected = balance  # Protected (convention: don't use outside)
        self.__private = balance   # Private (name mangling)

    def __validate_amount(self):  # Private method
        return self.__private > 0

    def withdraw(self, amount):
        if amount <= self.__private and self.__validate_amount():
            self.__private -= amount
            return True
        return False

account = BankAccount(1000)
print(account.public)           # OK
print(account._protected)       # Possible but discouraged
# print(account.__private)      # AttributeError!

# Name mangling: __private becomes _BankAccount__private
print(account._BankAccount__private)  # Works but don't do this!
</div>

<h3>Levels of Access</h3>
<ul>
<li><strong>Public:</strong> `name` - No restrictions</li>
<li><strong>Protected:</strong> `_name` - Meant for internal use; convention-based</li>
<li><strong>Private:</strong> `__name` - Name mangled; discourage access</li>
</ul>

<div class="warning-box">
<strong>Important:</strong> Python has no true private attributes. Name mangling discourages access but doesn't prevent it. Use conventions and documentation.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use naming conventions to indicate intended access levels. Encapsulation protects invariants and enables future changes without breaking clients.
</div>
'''
    },
    {
        'id': 'py_oop_04_02',
        'title': 'Polymorphism: Many Forms',
        'body': '''
<h2 class="accent-heading">Polymorphism: Many Forms</h2>

<div class="concept-box">
<h3>What is Polymorphism?</h3>
<p>Polymorphism means "many forms." It allows different classes to be used interchangeably, with each providing their own implementation of a method. This enables flexible and extensible code.</p>
</div>

<h3>Subtype Polymorphism (Runtime)</h3>

<div class="worked-example">
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_areas(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")

shapes = [Circle(5), Rectangle(4, 6)]
print_areas(shapes)  # Works for both shapes!
</div>

<h3>Duck Typing (Pythonic Polymorphism)</h3>
<p>Python supports "duck typing": if it walks like a duck and quacks like a duck, it's a duck. No inheritance needed.</p>

<div class="worked-example">
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())  # Works with any object that has speak()

animal_sound(Dog())  # Woof
animal_sound(Cat())  # Meow
# No common base class needed!
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Polymorphism enables writing code that works with multiple types. Python's duck typing is flexible and Pythonic.
</div>
'''
    },
    {
        'id': 'py_oop_04_03',
        'title': 'Operator Overloading',
        'body': '''
<h2 class="accent-heading">Operator Overloading</h2>

<div class="concept-box">
<h3>Customizing Operators</h3>
<p>By defining special methods, you can customize how operators work with your objects. This enables intuitive, readable code.</p>
</div>

<h3>Common Operator Methods</h3>

<div class="worked-example">
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v1 * 2)       # Vector(2, 4)
</div>

<h3>Common Operator Methods</h3>
<ul>
<li>`__add__` (+), `__sub__` (-), `__mul__` (*)</li>
<li>`__eq__` (==), `__ne__` (!=), `__lt__` (<), `__gt__` (>)</li>
<li>`__getitem__` ([]), `__len__` (len())</li>
<li>`__str__` (str()), `__repr__` (repr())</li>
</ul>

<div class="success-box">
<strong>Key Takeaway:</strong> Operator overloading makes classes feel natural. Implement only methods that make semantic sense for your class.
</div>
'''
    },
    {
        'id': 'py_oop_04_04',
        'title': 'Liskov Substitution Principle',
        'body': '''
<h2 class="accent-heading">Liskov Substitution Principle</h2>

<div class="concept-box">
<h3>LSP: A Core Design Principle</h3>
<p>The Liskov Substitution Principle states: "Objects of a superclass should be replaceable with objects of its subclasses without breaking the application." In other words, subtypes must be substitutable for their base types.</p>
</div>

<h3>Good Example: LSP Followed</h3>

<div class="worked-example">
class Bird:
    def fly(self):
        return "Flying"

class Eagle(Bird):
    def fly(self):
        return "Eagle soaring high"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow fluttering"

def make_bird_fly(bird):
    return bird.fly()

# Both can be used interchangeably
print(make_bird_fly(Eagle()))    # Eagle soaring high
print(make_bird_fly(Sparrow()))  # Sparrow fluttering
</div>

<h3>Bad Example: LSP Violated</h3>

<div class="worked-example">
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# This breaks expectations!
def make_bird_fly(bird):
    return bird.fly()

# make_bird_fly(Penguin())  # Raises exception!
</div>

<h3>The Correct Approach</h3>
<p>Use a better class hierarchy:</p>

<div class="worked-example">
class Animal:
    pass

class FlyingBird(Animal):
    def fly(self):
        return "Flying"

class SwimmingBird(Animal):
    def swim(self):
        return "Swimming"

class Penguin(SwimmingBird):
    pass  # Doesn't override fly()

# Now Penguin isn't expected to fly!
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Design hierarchies so subclasses can replace their base class. If a subclass can't fulfill the contract, reconsider the hierarchy.
</div>
'''
    }
]

