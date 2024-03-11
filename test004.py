class Car:
    # Constructor method to initialize the Car object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display information about the Car
    def display_car_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Creating a Car object
my_car = Car("Toyota", "Corolla", 2020)

# Calling the method to display information about the car
my_car.display_car_info()
