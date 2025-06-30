file_path = 'test.txt'

#mode 
# r ; read, w = write(new) , a = append(Continue writing)
with open(file_path,'r') as file:
    contents = file.read()

print('file contents :', contents)