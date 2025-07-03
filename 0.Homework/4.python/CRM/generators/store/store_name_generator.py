import random
import sys
import os
import csv
sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')
from generators.address_generator import AddressGenerator
# 1. 주소 생성
# 2. 주소에서 '시군구' 추출
# 3. '구'를 뽑고 '시, 군, 구'제거 (2글자 이하 -> 예) 중구 -> 구 붙이기)
# 4. type + 구 + 랜덤Num + 호점 붙이기

class StoreNameGenerator:
    
    def __init__(self):
        self.address_generator = AddressGenerator('csv/region_list.csv')
    
    def generate_random_number(self):
        return str(random.randint(1, 20))
    
    def generate_store_address(self): ## 가게 찐 주소
        address = self.address_generator.generate_address()
        parts = address.split()
        sigungu = ''
        sigungu = parts[1]
        if len(parts[1]) <= 2:
            sigungu = parts[1]
        elif sigungu.endswith('구') or sigungu.endswith('군') or sigungu.endswith('시'):
                sigungu = sigungu[:-1]
        return address, sigungu
    
    def generate_store(self):
        address, sigungu = self.generate_store_address()
        store_name =f'{sigungu} {self.generate_random_number()}호점'
        return store_name, address
        
        
        
        
if __name__ == "__main__":
    generator = StoreNameGenerator()
    for _ in range(10):
        store_name , address = generator.generate_store()
        print(f'storeName : {store_name} storeAddress : {address}')
