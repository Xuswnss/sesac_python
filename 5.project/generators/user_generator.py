from gender_generator import GenderGenerator
from address_generator import AddressGenerate
from birthday_generator import BirthdayGenerator
from name_generator import NameGenerator
 
class UserGenerator:
    def __init__(self):
        self.name_gen = NameGenerator('./5.project/names.txt')
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
    
