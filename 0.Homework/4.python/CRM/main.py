import pandas as pd
from generators.member.user_generator import UserGenerator
from generators.store.store_generator import StoreGenerator
from generators.item.item_generator import ItemGenerator
from generators.item.order_generator import OrderGenerator
from generators.item.order_item_generator import OrderItemGenerator

def main():
    data_type = input("데이터 유형을 입력해주세요\n1.User\n2.Store\n3.Item\n4.Order\n5.OrderItem\n")
    count = int(input('생성할 데이터 개수를 입력하세요 : '))
    output_type = input('csv or print? : ')
    
    generator_map = {
        "1" : UserGenerator,
        "2" : StoreGenerator,
        "3" : ItemGenerator,
        "4" : OrderGenerator,
        "5" : OrderItemGenerator
    }
    
    if data_type not in generator_map:
        print('유효하지 않습니다')
        return
    
    
    generator_class = generator_map[data_type]
    generator = generator_class()  
    print('generator : ', generator)
    data = generator.generator(count)
    
    if output_type == "csv":
        df = pd.DataFrame(data)
        class_name = generator.__class__.__name__
        df.to_csv(f'csv/{class_name.lower()}_data.csv', index=False, encoding='utf-8')
        print(f'{data_type} csv 저장 완')
    elif output_type == 'print':
        for row in data:
            print(row)
    else:
        print('error')
        

if __name__ == "__main__":
    main()




