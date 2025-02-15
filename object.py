# File: object_example.py
# Description: A simple example demonstrating the concept of Objects in OOPS using Python.

# Define a class named 'Car'
class Car:
    # Class attribute (shared by all instances of the class)
    vehicle_type = "Automobile"

    # Constructor method (initializes object attributes)
    def __init__(self, make, model, year):
        self.make = make       # Instance attribute
        self.model = model     # Instance attribute
        self.year = year       # Instance attribute
        self.speed = 0         # Default instance attribute

    # Instance method (behavior of the object)
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.make} {self.model} is accelerating. Current speed: {self.speed} km/h")

    # Instance method (behavior of the object)
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
        print(f"{self.make} {self.model} is braking. Current speed: {self.speed} km/h")

    # Magic method (string representation of the object)
    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - Type: {self.vehicle_type}"

# Main function to demonstrate the usage of objects
if __name__ == "__main__":
    # Create objects (instances) of the Car class
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Tesla", "Model S", 2023)

    # Print object details using __str__ method
    print("Car 1 Details:", car1)
    print("Car 2 Details:", car2)

    # Demonstrate object behavior (methods)
    print("\nTesting Car 1:")
    car1.accelerate(30)  # Accelerate car1 by 30 km/h
    car1.brake(10)       # Brake car1 by 10 km/h

    print("\nTesting Car 2:")
    car2.accelerate(50)  # Accelerate car2 by 50 km/h
    car2.brake(20)       # Brake car2 by 20 km/h

    # Accessing class attribute
    print(f"\nVehicle type of Car 1: {car1.vehicle_type}")
    print(f"Vehicle type of Car 2: {car2.vehicle_type}")

    # Modifying instance attributes
    car1.year = 2021
    print("\nUpdated Car 1 Details:", car1)
