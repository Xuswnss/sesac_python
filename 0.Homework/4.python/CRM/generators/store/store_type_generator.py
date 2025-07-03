import random

class StoreTypeGenerator:
    def __init__(self, file_path):
        self.store_name = self.load_data_from_file(file_path)
        
    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding= 'utf-8' ) as file:
            data =file.read().splitlines()
        return data
            
    def generate_name(self):
        return random.choice(self.store_name)
        
if __name__ == "__main__":
    generator = StoreTypeGenerator('text/store_type.text')
    name_list = [generator.generate_name() for _ in range(10)]
    for name in name_list:
        print(name)
    