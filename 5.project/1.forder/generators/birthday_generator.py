import random
class BirthdayGenerator:
    def generate_birthday(self):
        year = random.randint(1990,2020)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f'{year}-{month:02d}-{day:02d}'