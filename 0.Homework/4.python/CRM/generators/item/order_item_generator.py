# orderitem.csv
import sys
import pandas as pd
import random
import csv
sys.path.append('/Users/hyeonjiyun/Desktop/src/sesac/SESAC_PY3/sesac_python/0.Homework/4.python/CRM')
from generators.id_generator import IdGenerator


class OrderItemGenerator:
    def __init__(self):
        self.id_generator = IdGenerator()
        self.orderId = pd.read_csv('csv/order_data.csv', header=None)[0].tolist()
        self.itemId= pd.read_csv('csv/item_data.csv', header=None)[0].tolist()
    
    
    def generator(self, count):
        orderItems = []
        for _ in range(count):
            orderItemId = self.id_generator.generate_id()
            orderId = random.choice(self.orderId)
            itemId = random.choice(self.itemId)
            orderItems.append((orderItemId, orderId, itemId))
        return orderItems
    
class DisplayData(OrderItemGenerator):
    def print_data(self, count):
        data = self.generator(count)
        for id, orderId, itemId in data:
            print(f'Id:{id}\nOrderId:{orderId}\nItemId:{itemId}\n')
            
    def save_to_csv(self,count,file_name):
        data = self.generator(count)
        header = [ 'Id', 'OrderId', 'ItemId']
        with open(file_name, mode='w', newline='', encoding='utf-8') as file :
            writer = csv.writer(file)
            writer.writerow(header)
            for id, orderId, itemId in data:
                writer.writerow([id, orderId, itemId])
            

if __name__ == "__main__":
    generator = DisplayData()
    # print(generator.print_data(10))
    print(generator.save_to_csv(30000, './csv/orderItem_data.csv'))