import random

class DateGenerator:
    def generate_date(self):
        year = random.randint(1990,2020)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f'{year}-{month:02d}-{day:02d}'
    
    def generate_date_time(self):
        year = random.randint(1990,2020)
        month = random.randint(1,12)
        day = random.randint(1,28)
        HH = random.randint(0,23)
        MM = random.randint(0,60)
        SS = random.randint(0,60)
        date_format = f'{year}-{month:02d}-{day:02d} {HH:02d}:{MM:02d}:{SS:02d}'
        return date_format
    

        