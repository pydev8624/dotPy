class Person:
    def __new__(cls, name):
        print("Creating instance in __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("Initializing instance in __init__")
        self.name = name

# Create first instance
p = Person("Ali")

# Create second instance using the class, not the object
pn1 = Person("Amir")

# Verify both instances
print(f"p.name: {p.name}")
print(f"pn1.name: {pn1.name}")
