import random
class AddressGenerate:
    def __init__(self):
        self.cities = ["New York", 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1,100)
        return f'{street_num} {city}'