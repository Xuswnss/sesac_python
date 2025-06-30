file_path = 'test.txt'

#mode 
# r ; read, w = write(new) , a = append(Continue writing)
with open(file_path,'w', encoding='utf-8') as file:
    file.write('hello!\n')
    file.write('hi')

# print('file contents :', contents)