class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
        self.mileage = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model} has been started.")
        else:
            print(f"The {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has been stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

    def drive(self, distance):
        if self.is_running:
            self.mileage += distance
            print(f"The {self.make} {self.model} has been driven for {distance} miles.")
        else:
            print(f"The {self.make} {self.model} needs to be started first.")

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} miles")
        if self.is_running:
            print("The car is currently running.")
        else:
            print("The car is currently stopped.")
