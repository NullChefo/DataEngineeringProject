from car import Car
from driver import Driver
from garage import Garage

# Create car instances
car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Civic", 2018, "Red")
car3 = Car("Ford", "Mustang", 2022, "Yellow")

# Create driver instance
driver = Driver("John Doe", 30)

# Create garage instance
garage = Garage("My Garage")

# Add cars to the driver's collection
driver.add_car(car1)
driver.add_car(car2)

# Add cars to the garage
garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)

# Display driver's cars
driver.list_cars()

# Display cars in the garage
garage.list_cars()

# Start the first car
car1.start()

# Drive the first car
car1.drive(50)

# Stop the first car
car1.stop()

# Remove a car from the driver's collection
driver.remove_car(car2)

# Remove a car from the garage
garage.remove_car(car2)

# Display driver's cars again
driver.list_cars()

# Display cars in the garage again
garage.list_cars()
