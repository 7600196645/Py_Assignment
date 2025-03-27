
# 11) Write a Python program to create a class and access the properties of the class using an object. 
# Define a class
class Car:
    """A simple Car class"""
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Accessing properties of the object
print("Car Details:")
print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Year:", my_car.year)

# Modifying an attribute
my_car.year = 2024
print("\nUpdated Year:", my_car.year)

