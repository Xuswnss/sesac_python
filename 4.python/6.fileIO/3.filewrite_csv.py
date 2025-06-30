#csv ; comma seperated value
import csv

file_path  ='test.csv'

data = [
            ['name', 'age', 'city'],
            ['john', 25,'seoul'],
            ['jiyun',22,'jeju'],
            ['bob', 30, 'italy']
]

print(data)
for i in range(len(data)):
    print(data[i])
    
with open(file_path, 'w') as file:
    csv_writer =csv.writer(file)
    csv_writer.writerows(data)
    
print('csv쓰기 완료')
