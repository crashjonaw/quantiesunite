# Inheritance: Code Reuse and Hierarchy

SECTIONS = [
    {
        'id': 'py_oop_03_01',
        'title': 'Introduction to Inheritance',
        'body': '''
<h2 class="accent-heading">Inheritance: Code Reuse and Hierarchy</h2>

<div class="concept-box">
<h3>What is Inheritance?</h3>
<p>Inheritance allows a class to inherit attributes and methods from another class. The inheriting class is called the <strong>child</strong> or <strong>derived</strong> class, and the inherited-from class is the <strong>parent</strong> or <strong>base</strong> class. This promotes code reuse and establishes hierarchical relationships.</p>
</div>

<h3>Basic Inheritance Syntax</h3>

<div class="worked-example">
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} barks"

dog = Dog("Rex")
print(dog.speak())      # Rex barks
print(dog.name)         # Rex (inherited from Animal)
</div>

<h3>The `super()` Function</h3>
<p>Use `super()` to call parent class methods. This is essential for extending parent behavior rather than completely replacing it.</p>

<div class="worked-example">
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        return f"{self.color} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, color, doors):
        super().__init__(brand, color)  # Call parent __init__
        self.doors = doors

    def info(self):
        parent_info = super().info()  # Call parent method
        return f"{parent_info} with {self.doors} doors"

car = Car("Toyota", "red", 4)
print(car.info())  # red Toyota with 4 doors
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Inheritance creates hierarchies and enables code reuse. Use `super()` to extend parent behavior without rewriting it.
</div>
'''
    },
    {
        'id': 'py_oop_03_02',
        'title': 'Method Resolution Order (MRO)',
        'body': '''
<h2 class="accent-heading">Method Resolution Order (MRO)</h2>

<div class="concept-box">
<h3>Understanding MRO</h3>
<p>The Method Resolution Order (MRO) determines which parent class method is called when multiple parents define the same method. Python uses the C3 Linearization algorithm to compute MRO.</p>
</div>

<h3>Viewing MRO</h3>

<div class="worked-example">
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D.mro())  # Shows the method resolution order
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]

d = D()
print(d.method())  # B (first in MRO after D)
</div>

<h3>Multiple Inheritance</h3>
<p>A class can inherit from multiple parents. MRO ensures predictable method lookup.</p>

<div class="worked-example">
class Swimmer:
    def swim(self):
        return "Swimming"

class Flyer:
    def fly(self):
        return "Flying"

class Duck(Swimmer, Flyer):
    pass

duck = Duck()
print(duck.swim())  # Swimming
print(duck.fly())   # Flying
print(Duck.mro())   # Shows order: Duck -> Swimmer -> Flyer -> object
</div>

<div class="warning-box">
<strong>Be Careful:</strong> Multiple inheritance can be complex. Use composition when inheritance becomes confusing.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> MRO determines method lookup order. Use `ClassName.mro()` to inspect it. Multiple inheritance follows C3 Linearization.
</div>
'''
    },
    {
        'id': 'py_oop_03_03',
        'title': 'Abstract Base Classes',
        'body': '''
<h2 class="accent-heading">Abstract Base Classes</h2>

<div class="concept-box">
<h3>What are Abstract Base Classes?</h3>
<p>Abstract Base Classes (ABCs) define an interface that subclasses must implement. They cannot be instantiated directly and enforce that derived classes implement specific methods.</p>
</div>

<h3>Using ABC</h3>

<div class="worked-example">
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Subclasses must implement this"""
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.area())  # 78.5

# This would raise TypeError:
# shape = Shape()  # Can't instantiate abstract class
</div>

<h3>Concrete Methods in Abstract Classes</h3>
<p>Abstract classes can contain concrete methods that subclasses inherit.</p>

<div class="worked-example">
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def introduce(self):  # Concrete method
        return f"I am {self.name}"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

cat = Cat("Whiskers")
print(cat.speak())      # Whiskers meows
print(cat.introduce())  # I am Whiskers
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use ABCs to enforce contracts. Subclasses must implement all abstract methods. This prevents bugs from incomplete implementations.
</div>
'''
    },
    {
        'id': 'py_oop_03_04',
        'title': 'Composition vs Inheritance',
        'body': '''
<h2 class="accent-heading">Composition vs Inheritance</h2>

<div class="concept-box">
<h3>The Choice: "Is-a" vs "Has-a"</h3>
<p>Inheritance models "is-a" relationships. Composition models "has-a" relationships. Choose composition when the relationship isn't a true specialization.</p>
</div>

<h3>Inheritance Example</h3>

<div class="worked-example">
# Inheritance: "is-a" relationship
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    pass

car = Car()
print(car.move())  # A car IS-A vehicle
</div>

<h3>Composition Example</h3>

<div class="worked-example">
# Composition: "has-a" relationship
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A engine

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine started
</div>

<h3>Why Composition Over Inheritance?</h3>
<ul>
<li><strong>Flexibility:</strong> Easily swap implementations without changing the class</li>
<li><strong>Simplicity:</strong> No complex inheritance hierarchies</li>
<li><strong>Testability:</strong> Easier to mock dependencies</li>
<li><strong>Reusability:</strong> Objects can use multiple components</li>
</ul>

<div class="warning-box">
<strong>Design Principle:</strong> Prefer composition over inheritance. Use inheritance only for true "is-a" relationships.
</div>

<div class="success-box">
<strong>Key Takeaway:</strong> Use inheritance for specialization ("is-a"). Use composition for capability ("has-a"). Composition is often more flexible.
</div>
'''
    }
]
