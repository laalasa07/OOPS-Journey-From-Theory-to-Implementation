# File: inheritance_example.py
# Description: A simple example demonstrating the concept of Inheritance in OOPS using Python.

# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Child class (Derived class) inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class using super()
        super().__init__(name, species="Dog")
        self.breed = breed

    # Method overriding (redefining the make_sound method)
    def make_sound(self):
        return "Woof!"

    # Additional method specific to Dog class
    def fetch(self, item):
        return f"{self.name} is fetching the {item}"

# Child class (Derived class) inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the parent class using super()
        super().__init__(name, species="Cat")
        self.color = color

    # Method overriding (redefining the make_sound method)
    def make_sound(self):
        return "Meow!"

    # Additional method specific to Cat class
    def climb(self, height):
        return f"{self.name} is climbing {height} meters"

# Main function to demonstrate inheritance
if __name__ == "__main__":
    # Create objects of the parent and child classes
    generic_animal = Animal("Generic", "Unknown Species")
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Black")

    # Print object details using __str__ method
    print(generic_animal)
    print(dog)
    print(cat)

    # Demonstrate inherited and overridden methods
    print(f"\n{generic_animal.name} says: {generic_animal.make_sound()}")
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")

    # Demonstrate additional methods in child classes
    print(f"\n{dog.fetch('ball')}")
    print(f"{cat.climb(3)}")
