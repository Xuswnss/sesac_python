import random

names = [ "James", 'Jane', 'Michael', 'Emily', 'William','Olivia']
cities = ["New York", 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_name():
    return random.choice(names)

def generate_birthday():
    year = random.randint(1990,2020)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return f'{year}-{month:02d}-{day:02d}'



def generate_gender():
    return random.choice(['Male', 'Female'])


def generate_address():
    city = random.choice(cities)
    street_num = random.randint(1,100)
    return f'{street_num} {city}'
users = []

for i in range(100):
    name = generate_name()
    bday = generate_birthday()
    gender = generate_gender()
    address = generate_address()
    users.append((name, bday, gender, address))
    
    
for _ in users:
    print(users)

print(generate_name())
print(generate_birthday())