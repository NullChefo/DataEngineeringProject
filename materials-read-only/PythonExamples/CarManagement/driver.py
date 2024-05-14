class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{self.name} added a {car.make} {car.model} to their collection.")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{self.name} removed a {car.make} {car.model} from their collection.")
        else:
            print(f"{self.name} does not own the {car.make} {car.model}.")

    def list_cars(self):
        if self.cars:
            print(f"{self.name}'s Cars:")
            for car in self.cars:
                print(f"- {car.make} {car.model}")
        else:
            print(f"{self.name} does not own any cars.")
