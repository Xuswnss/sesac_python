try:
    result = 10 / 0 #division by zero
    print(result)
except ZeroDivisionError:
    print('error : division by zero')

def convert_to_int(num_str):
    """
    글자를 숫자로 바꾸는 함수임 
    Args:
        num_str(String): 사용자 입력의 문자열 형태의 숫자로 받음
        
    Returns:
        result: 변환된 숫작밧, 변환에 실해한 경우 None을 반환함
    """
    try: 
        result = int(num_str)
        
    except ValueError:
        print('입력한 값이 숫자가 아닙니다. 입력값:', num_str)
        result = 'error error'
        
    return result
        
    
def double_number(num):
    return num * 2

user_input = 'A'
result = double_number(convert_to_int(user_input))
print(f'입력한 숫자 : {user_input}의 두배 값은 {result}입니다')