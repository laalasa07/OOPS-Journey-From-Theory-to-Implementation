# Polymorphism in Python

# Base class
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class 3
class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.speak())

# Instances of derived classes
dog = Dog()
cat = Cat()
duck = Duck()

# Polymorphic behavior
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(duck) # Output: Quack!
