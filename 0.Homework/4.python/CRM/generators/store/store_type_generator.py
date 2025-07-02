import random

class StoreTypeGenerator:
    def __init__(self, file_path):
        self.
        
        

class NameGenerator:
    def __init__(self : str , file_path):
        self.names = self.load_data_from_file(file_path)
        
    def load_data_from_file(self, file_path) :
        with open(file_path, 'r', encoding= 'utf-8') as file:
            data =file.read().splitlines()
        return data
    
    def generate_name(self):
        return random.choice(self.names)
        
if __name__ == "__main__":
    generator = NameGenerator('text/name.text')
    name_list = [generator.generate_name() for _ in range(50)]
    for name in name_list:
        print(name)
    