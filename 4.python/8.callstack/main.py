import module_a as ma

def start_program():
    print('main으로 부터 시작된 start_program함수')
    local_function_a()
    
def local_function_a():
    print('main으로 부터 호출된 local_function_a 함수')
    ma.function_a1()
    
if __name__ == '__main__':
    start_program()