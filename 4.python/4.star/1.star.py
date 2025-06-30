#파이썬 별만들기
#1
# print('#1')
# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

#2
# print('#2')
# def draw_triangle(line):
#     for i in range(1, line + 1):
#         print(i * '*')
 
#3
# print('#3')
# def draw_triangle2(line):
#     for i in range(i , line):
#         for j in i:
#             print('*' * i)
            
#4
# print('#4')          
# def draw_triangle3(line):
#     n = line
#     for i in range(1, line + 1):
#         print(' ' * (n - i) + '*' * i)
        
#5
print('#5')  
def iltriangle(line):
    for i in range(5, 0 , -1):
        print(i*'*')
        
# draw_triangle(5)
# draw_triangle2(5)
# draw_triangle3(5)
iltriangle(5)