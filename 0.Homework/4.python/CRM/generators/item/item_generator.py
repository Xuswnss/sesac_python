import random
import sys
import json 
import csv

sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')
from generators.id_generator import IdGenerator
class ItemGenerator:
    def __init__(self):
        self.generate_itemId = IdGenerator()
    
    def random_category(self):
        with open('data/item.json', 'r', encoding='utf-8') as file:
            json_items = json.load(file)
            category = random.choice(list(json_items.keys()))
            product = random.choice(list(json_items[category].items()))
            result = [product[0] +" "+ category, category, product[1]]
        
            return result
            
    
    def generator_item(self, count):
        items = []
        for _ in range(count):
            itemId = self.generate_itemId.generate_id()
            item = self.random_category()
            items.append([itemId] + item)
            
        return items
    
class DisplayData(ItemGenerator):
    def print_data(self, count):
        data = self.generator_item(count)
        for item_id, item_name, item_type, unitprice in data:
            print(f'Id:{item_id}\nName:{item_name}\nType:{item_type}\nUnitPrice:{unitprice}\n')
            
    def save_to_csv(self, count, file_name):
        data = self.generator_item(count)
        
        header = ['Id', 'Name', 'Type', 'UnitPrice']
        with open (file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for id, name, type, unitprice in data:
                writer.writerow([id,name,type,unitprice])
        
        
        

if __name__ == '__main__':
   generator = DisplayData()
#    print(generator.print_data(10))
generator.save_to_csv(100,'./csv/item_data.csv')

