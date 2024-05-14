class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.make} {car.model} added to {self.name} garage.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.make} {car.model} removed from {self.name} garage.")
        else:
            print(f"{car.make} {car.model} is not present in {self.name} garage.")

    def list_cars(self):
        print(f"Cars in {self.name} garage:")
        if self.cars:
            for car in self.cars:
                print(f"- {car.make} {car.model}")
        else:
            print("No cars present in the garage.")
