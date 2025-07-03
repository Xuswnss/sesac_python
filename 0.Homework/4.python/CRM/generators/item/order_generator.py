import sys
import pandas as pd
import random
import csv
sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')

from generators.id_generator import IdGenerator
from generators.date_generator import DateGenerator


class OrderGenerator:
    def __init__(self):
        self.id_generator = IdGenerator()
        self.date_generator = DateGenerator()
        self.store_ids = pd.read_csv('csv/store_data.csv', header=None)[0].tolist()
        self.user_ids = pd.read_csv('csv/user_data.csv', header=None)[0].tolist()

    def generate_orderAt(self):
        return self.date_generator.generate_date_time()

    def generator_order(self, count):
        orders = []
        for _ in range(count):
            order_id = self.id_generator.generate_id()
            order_at = self.generate_orderAt()
            store_id = random.choice(self.store_ids)
            user_id = random.choice(self.user_ids)
            orders.append((order_id, order_at, store_id, user_id))
        return orders
    
class DisplayData(OrderGenerator):
    def print_data(self, count):
        data = self.generator_order(count)
        for id ,orderAt, storeId, userId in data:
            print(f'Id:{id}\norderAt:{orderAt}\nstoreId:{storeId}\nuserId:{userId}\n')
            
    def save_to_csv(self,count,file_name):
        data = self.generator_order(count)
        header = [ 'Id', 'OrderAt', 'StoreId', 'UserId']
        with open(file_name, mode='w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for id, orderAt, storeId, userId in data:
                writer.writerow([id, orderAt, storeId, userId])
        
            

if __name__ == '__main__':
    generator = DisplayData()
    # print(generator.print_data(10))
    print(generator.save_to_csv(100,'./csv/order_data.csv'))
