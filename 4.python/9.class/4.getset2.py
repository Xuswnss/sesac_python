class Person:
    _count = 0 

    def __init__(self, name, age): 
        self._name = name
        self._age = age
        Person._count += 1 
        
        
    @property   #이 함수는 getter 입니다. 
    def name(self):
        return self._name
    
    @property    
    def age(self):
        return self._age
    
    @age.setter 
    def age(self, age):
         self._age = age
         
    @name.setter  
    def name(self, name):
         self._name = name
        
        
    def greet(self): 
        print(f'안녕하세요 저는 {self.name}입니다.')


    def ride_car(self):
        print(f'{self.name}는 지금 운전중...')
        
    
        

p =  Person('xuswns', 20) 
p2 = Person('timi' , 10)

print(p.name)


