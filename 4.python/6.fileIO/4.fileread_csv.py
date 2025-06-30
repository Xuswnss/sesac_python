import csv

file_path = 'test.csv'


data = [
            ['name', 'age', 'city'],
            ['john', 25,'seoul'],
            ['jiyun',22,'jeju'],
            ['bob', 30, 'italy']
]
print('읽기 시작')
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # print(row)
        # data.append(row)
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        csv_writer.writerow(['Aliice' , 20 ,'korea'])

print(data)        
        
print('읽기 완료')