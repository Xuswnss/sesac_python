from driver import Driver
from car import Car

driver = Driver("Bob", 40, "1종보통")

driver.drive(30)

car = Car("Tesla", "model s")

driver.assign_car(car)

driver.drive(50)
driver.drive(100)

car.update_odometer(100)
car.update_odometer(200)
car.read_odometer()

car2 = Car("Hyundai", "K5")
driver2 = Driver("David", 30, "2종보통", car2)
driver2.drive(500)