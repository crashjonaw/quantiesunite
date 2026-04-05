MINDMAP = {
    "concepts": [
        {"title": "Classes & Objects", "points": [
            "class Dog: — defines a blueprint",
            "__init__(self, name): — constructor, called on creation",
            "self refers to the instance: self.name = name",
            "Instance: my_dog = Dog('Rex')",
        ]},
        {"title": "Methods", "points": [
            "Instance methods: def bark(self): ...",
            "Class methods: @classmethod, receives cls instead of self",
            "Static methods: @staticmethod, no self or cls",
            "Special methods: __str__, __repr__, __len__, __eq__",
        ]},
        {"title": "Inheritance", "points": [
            "class Puppy(Dog): — Puppy inherits from Dog",
            "super().__init__() to call parent constructor",
            "Override methods to change behaviour",
            "isinstance() and issubclass() for type checking",
        ]},
        {"title": "Encapsulation & Properties", "points": [
            "Convention: _private (single underscore), __mangled (double)",
            "@property decorator for getter, @name.setter for setter",
            "Keep internals hidden, expose clean interface",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Use classes when you have data + behaviour that belong together",
        "Prefer composition over inheritance for flexibility",
        "Implement __repr__ for debugging and __str__ for user-facing output",
    ],
}
