# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a Vehicle class without any variables and methods.
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Create a Vehicle class without any variables and methods.
class Vehicle:
    pass

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seats):
        super().__init__(max_speed, mileage)