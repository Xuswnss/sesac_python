from person import Person

class Driver(Person):
    def __init__(self, name, age, driver_license, car):
        super().__init__(name, age)