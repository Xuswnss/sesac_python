def square_root(num):
    return num ** 0.5


def square_root2(num):
    if(num < 0 ):
        raise ValueError('음수의 제곱근인 계산할 수 없습니다')
    
    return num ** 0.5

        

print(square_root(35))
print(square_root(1))

try:
    print(square_root2(-25))
except ValueError as a:
    print(a)