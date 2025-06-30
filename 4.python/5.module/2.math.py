import math as m


print('#1 math.pi')
print(m.pi)

print('- ' * 10)

radius = 5
area = m.pi * m.pow(radius,2)
print(f'반지름이 {radius}인 원의 넓이는 {area:15.2f} 입니다') #.2f 소수 둘째 자리까지 표시
