## store.csv
import sys
import csv
sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')
#Id,Name,Type,Address
from generators.id_generator import IdGenerator
from store_name_generator import StoreNameGenerator # address, type
from store_type_generator import StoreTypeGenerator

class StoreGenerator:
    def __init__(self):
        self.generate_storeId = IdGenerator()
        self.generate_store_name_and_address = StoreNameGenerator()
        self.generate_store_type = StoreTypeGenerator('text/store_type.text')
        
    
    def generator_store(self, count):
        stores = []
        for _ in range(count):
            store_id = self.generate_storeId.generate_id()
            store_name, address = self.generate_store_name_and_address.generate_store()
            store_type = self.generate_store_type.generate_name()
            store_name = f'{store_type} {store_name}'
            stores.append((store_id, store_name, store_type, address))
        return stores
        

class DisplayData(StoreGenerator):
    def print_data(self, count):
        data = self.generator_store(count)
        for store_id, store_name, store_type , store_address in  data:
            print(f'Store_id:{store_id}\nStore_name:{store_name}\nStore_type:{store_type}\nStore_address:{store_address}\n')
            
    def save_to_csv(self, count , file_name):
        data = self.generator_store(count)
        
        header = ['Id', 'Name', 'Type', 'Address']
        with open(file_name, mode = 'w', newline='',encoding = 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for store_id, store_name, store_type, store_Address in data:
                writer.writerow([store_id, store_name, store_type , store_Address])
 
 
def main():
    generator = DisplayData()           
    generator.save_to_csv(100, './csv/store_data.csv')

if __name__ == "__main__":
    generator = DisplayData()
    generator.print_data(100)
    # main()