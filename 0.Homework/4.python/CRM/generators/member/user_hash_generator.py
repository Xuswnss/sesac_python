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
from password_generator import PasswordGenerator

class UserGenerator:
    def __init__(self):
        self.generate_name = NameGenerator('data/name.text')
        self.generate_birthday = DateGenerator()
        self.generate_gender = GenderGenerator()
        self.generate_address = AddressGenerator('csv/region_list.csv')
        self.generate_userId = IdGenerator()
        self.generate_age = AgeGenerator()
        self.generate_password = PasswordGenerator()  # 비밀번호 생성기 추가
             
    def generator(self, count):
        users = []
        for _ in range(count):
            name = self.generate_name.generate_name()
            age = self.generate_age.generate_age()
            birthday = self.generate_birthday.generate_date()
            address = self.generate_address.generate_address()
            gender = self.generate_gender.generate_gender()
            id = self.generate_userId.generate_id()
            
            # 비밀번호 생성 및 해시화
            raw_password, hashed_password = self.generate_password.generate_and_hash_password()
            
            # user => Id, Name, Gender, Age, Birthdate, Address, RawPassword, HashedPassword
            users.append((id, name, gender, age, birthday, address, raw_password, hashed_password))
        return users

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generator(count)
        for id, name, gender, age, birthday, address, raw_password, hashed_password in data:
            print(f'ID: {id}')
            print(f'Name: {name}')
            print(f'Gender: {gender}')
            print(f'Age: {age}')
            print(f'Birthday: {birthday}')
            print(f'Address: {address}')
            print(f'Raw Password: {raw_password}')
            print(f'Hashed Password: {hashed_password}')
            print('-' * 50)
                 
    def save_to_csv(self, count, file_name, include_raw_password=False):
        """
        CSV 파일로 저장
        
        Args:
            count: 생성할 사용자 수
            file_name: 저장할 파일명
            include_raw_password: 원본 비밀번호도 함께 저장할지 여부 (기본값: False)
        """
        data = self.generator(count)
        
        if include_raw_password:
            # 개발/테스트용: 원본 비밀번호도 포함
            header = ['ID', 'Name', 'Gender', 'Age', 'Birthday', 'Address', 'RawPassword', 'HashedPassword']
            rows = data
        else:
            # 운영용: 해시된 비밀번호만 포함
            header = ['ID', 'Name', 'Gender', 'Age', 'Birthday', 'Address', 'HashedPassword']
            rows = [(id, name, gender, age, birthday, address, hashed_password) 
                   for id, name, gender, age, birthday, address, raw_password, hashed_password in data]
        
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"✅ {count}명의 사용자 데이터가 '{file_name}'에 저장되었습니다.")
        if include_raw_password:
            print("⚠️  보안 주의: 원본 비밀번호가 포함되어 있습니다. 개발/테스트용으로만 사용하세요.")

    def save_password_verification_sample(self, count=5):
        """
        비밀번호 검증 샘플 생성 (테스트용)
        """
        data = self.generator(count)
        
        print("=== 비밀번호 검증 샘플 ===")
        for i, (id, name, gender, age, birthday, address, raw_password, hashed_password) in enumerate(data, 1):
            print(f"\n[사용자 {i}]")
            print(f"ID: {id}")
            print(f"이름: {name}")
            print(f"원본 비밀번호: {raw_password}")
            print(f"해시된 비밀번호: {hashed_password}")
            
            # 비밀번호 검증 테스트
            is_valid = self.generate_password.verify_password(raw_password, hashed_password)
            print(f"비밀번호 검증 결과: {'✅ 성공' if is_valid else '❌ 실패'}")
            
            # 잘못된 비밀번호로 테스트
            wrong_password = "wrong_password_123"
            is_wrong = self.generate_password.verify_password(wrong_password, hashed_password)
            print(f"잘못된 비밀번호 테스트: {'❌ 뚫림(문제있음)' if is_wrong else '✅ 차단됨'}")

def main():
    my_data = DisplayData()
    
    # 1. 운영용 데이터 생성 (해시된 비밀번호만)
    my_data.save_to_csv(1000, './csv/user_data_production.csv', include_raw_password=False)
    
    # 2. 개발/테스트용 데이터 생성 (원본 비밀번호 포함)
    my_data.save_to_csv(100, './csv/user_data_development.csv', include_raw_password=True)
    
    # 3. 비밀번호 검증 샘플 출력
    my_data.save_password_verification_sample(3)
    
    # 4. 소량 데이터 콘솔 출력 (확인용)
    print("\n=== 생성된 사용자 데이터 샘플 ===")
    my_data.print_data(2)

if __name__ == "__main__":
    main()