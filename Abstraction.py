# Abstraction in Python

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete Class 1
class Car(Vehicle):
    def start(self):
        return "Car started"

    def stop(self):
        return "Car stopped"

# Concrete Class 2
class Bike(Vehicle):
    def start(self):
        return "Bike started"

    def stop(self):
        return "Bike stopped"

# Function demonstrating abstraction
def drive(vehicle):
    print(vehicle.start())
    print(vehicle.stop())

# Instances of concrete classes
car = Car()
bike = Bike()

# Using abstraction
drive(car)   # Output: Car started \n Car stopped
drive(bike)  # Output: Bike started \n Bike stopped
