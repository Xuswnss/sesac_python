## User.csv
import sys
import os
import csv
sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')
from generators.address_generator import AddressGenerator
from generators.date_generator import DateGenerator
from generators.id_generator import IdGenerator
from gender_generator import GenderGenerator
from name_generator import NameGenerator
from age_generator import AgeGenerator


class UserGenerator:
    def __init__(self):
        self.generate_name = NameGenerator('text/name.text')
        self.generate_birthday = DateGenerator()
        self.generate_gender = GenderGenerator()
        self.generate_address = AddressGenerator('csv/region_list.csv')
        self.generate_userId = IdGenerator()
        self.generate_age = AgeGenerator()
        
    def generator_user(self, count):
        users =[]
        for _ in range(count):
            name = self.generate_name.generate_name()
            age = self.generate_age.generate_age()
            birthday = self.generate_birthday.generate_date()
            address = self.generate_address.generate_address()
            gender = self.generate_gender.generate_gender()
            id = self.generate_userId.generate_id()
           # user => Id,Name,Gender,Age,Birthdate,Address
            users.append((id,name, gender, age, birthday,address))
        return users
    
class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generator_user(count)
        for id, name, gender, age,  birthday, address in data:
            print(f'ID:{id}\nName:{name}\nGender:{gender}\nAge:{age}\nBirthday:{birthday}\nAddress:{address}\n')
            
    def save_to_csv(self,count,file_name):
        data = self.generator_user(count)
        
        header = ['ID', 'Name', 'Gender', 'Age', 'Birthday', 'Address']
        
        with open(file_name, mode='w', newline='', encoding='utf-8')as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for id, name, gender, age, birthday, address in data:
                writer.writerow([id,name,gender,age,birthday,address])
        

def main():
    my_data = DisplayData()
    # my_data.print_data(100)
    my_data.save_to_csv(100, './csv/user_data.csv')

if __name__ == "__main__":
    main()
