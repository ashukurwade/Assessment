class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def get_description(self):
        return f"{self.year} {self.make} {self.model} - {self.color}"

# Example usage:
my_car = Car(make="Toyota", model="Camry", year=2020, color="Blue")
print(my_car.get_description())  # Output: 2020 Toyota Camry - Blue