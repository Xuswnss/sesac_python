import random

class NameGenerator:
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)
    #     self.names = [ "James", 'Jane', 'Michael', 'Emily', 'William','Olivia']
        
    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = file.read().splitlines()
        return data
    
    def generate_name(self):
        return random.choice(self.names)
    
    
class BirthdayGenerator:
    def generate_birthday(self):
        year = random.randint(1990,2020)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f'{year}-{month:02d}-{day:02d}'
    
class GenderGenerator:
    def generate_gender(self):
        return random.choice(['Male', 'Female'])
    
class AddressGenerate:
    def __init__(self):
        self.cities = ["New York", 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1,100)
        return f'{street_num} {city}'
    
class UserGenerator:
    def __init__(self):
        self.name_gen = NameGenerator('5.project/names.txt')
        self.bday_gen = BirthdayGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerate()
        
    def generator_user(self,count):
        users = []
        for _ in range(count):
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthday()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            users.append((name, bday, gender, address))

        return users

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generator_user(count)
        for name, birthday, gender ,address in  data:
            print(f'Name : {name}\nBirthday: {birthday}\nGender :{gender}\nAddress: {address}\n')
            

my_data = DisplayData()
my_data.print_data(100)