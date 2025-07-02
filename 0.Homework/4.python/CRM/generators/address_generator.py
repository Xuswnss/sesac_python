import pandas as pd
import random

class AddressGenerator:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data = pd.read_csv(csv_path, encoding="cp949")
        self.data.columns = ['시도', '시군구']

    def generate_random_road_name(self):
        number = random.randint(1, 150)
        suffix = random.choice(['길', '로'])
        return f"{number}{suffix}"

    def generate_random_building_number(self):
        return str(random.randint(1, 150))

    def clean_text(self, text):
        return str(text).replace('\n', '').replace(' ', '').strip()

    def generate_address(self):
        row = self.data.sample(1).iloc[0]  # 랜덤 행 하나 선택
        sido = self.clean_text(row['시도'])
        sigungu = self.clean_text(row['시군구'])
        road_name = self.generate_random_road_name()
        building_number = self.generate_random_building_number()
        return f"{sido} {sigungu} {road_name} {building_number}"



if __name__ == "__main__":
    generator = AddressGenerator('csv/region_list.csv')
    address_list = [generator.generate_address() for _ in range(50)]
    for address in address_list:
        print(address)
