class Person:
# class(객체) 안에 있는 함수를 method라고 부른다.

    def __init__(self, name, age): # attribute -> 개별 데이타를 저장하는 공간
        self.name = name
        self.age = age
        
    def __str__(self): # 이 객체를 사람들이 보기 좋게 표현하는 함수
        return f'Person'
    
    def __eq__(self, other): ##나와 다른 객체를 비교할 떄 조건
        return self.name == other.name and self.age == other.age
        
        
    def greet(self): # method
        print(f'안녕하세요 저는 {self.name}입니다.')


    def ride_car(self):
        print(f'{self.name}는 지금 운전중...')

p =  Person('xuswns', 20)
p2 = Person('timi' , 10)
p3 = Person('xuswns', 20)
p.ride_car()
p.greet()
print(Person)
p2.ride_car()
p2.greet()
print('p와 p3를 같나요?? : ',p == p3)