file_path ='file.txt'
file = open(file_path, "r") #file is called file Descriptor

contents = file.read()
file.close()