try:
    with open('hello.txt', 'r')as file:
        contents = file.read()
        
        print('file contents: ', contents)
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('file does not read')
except:
    print('it is unknown error')