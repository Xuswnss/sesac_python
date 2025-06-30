import csv

file_path = 'test.csv'


data = [
            {"name":'john', "age" : 25,"city" :'seoul'},
            {"name":'jiyun',"age" : 22,"city" :'jeju'},
            {"name":'bob', "age" : 30, "city" :'italy'}
]

# print(data)
print('- ' *10)
for person in data:
    # print(person)
    for key, value in person.items():
        print(f'key : {key}, value : {value}')
        print(f'사람의 이름은 {person["name"]}, 나이는 {person["age"]}, 지역은 {person["city"]} 이다ㄴ')
        

with open(file_path, 'w', newline= '')as file:
    # headers = ["name", "age","city"] 
    headers = data[0].key() ##위처럼 하드코딩하지말고 이렇게 해봐
    
    csv_writer = csv.DictWriter(file,fieldnames= headers)
    csv_writer.writeheader
    csv_writer.writerows(data)