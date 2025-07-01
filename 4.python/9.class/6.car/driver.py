from person import Person
from typing import Optional
from car import Car

class Driver(Person):
    def __init__(self, name, age, license_type, car : Optional[Car] = None) -> None:
        super().__init__(name, age)
        self._license_type = license_type
        self._car: Optional[Car] = car
        
    def assign_car(self, car: Car)->None:
        self._car = car
        
    def drive(self, distance : int) -> None :
        if self._car :
            self._car.increment_odometer(distance)
            self._car.read_odometer()
        else:
            print()
        