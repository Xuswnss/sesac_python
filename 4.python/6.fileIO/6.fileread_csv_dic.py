import csv

file_path = 'test.csv'

data = []

with open(file_path, 'w', newline= '')as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

print(data)