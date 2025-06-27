x = 5
y = 'hello'
z = [1 , 2, 3]

print(type(x))
print(type(y))
print(type(z))
print(isinstance(x, int))
print(isinstance(x,str))
print(isinstance(y.str))


print('*'*10)
#class A
class A:
            pass
class B(A): # B extends A (A를 상속 받음)
            pass

class C:
        pass
b = B() # b = nev B()s b라는 변수를 B라는 클래스로 직어냄
print(isinstance(b,A)) # true
print(isinstance(b,B)) # true
print(isinstance(b,C)) # False
