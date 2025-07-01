class Person:
    _count = 0 

    def __init__(self, name, age): 
        self._name = name
        self._age = age
        Person.count += 1 
        
    def get_name(self):
        return self._name
        
    def set_age(self, age):
         self._age = age
         
    def get_age(self):
        return self._age
        
    def set_name(self, name):
        
         self._name = name
        
        
    def greet(self): 
        print(f'안녕하세요 저는 {self.name}입니다.')


    def ride_car(self):
        print(f'{self.name}는 지금 운전중...')
        
    
        

p =  Person('xuswns', 20) 
p2 = Person('timi' , 10)


