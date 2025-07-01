from person import Person

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self._company = company
        
    def greet(self):
        print(f'저는 {self._company}에서 일하는 {self._name} 입니다.')
    
    def work(self):
        print(f'직원 {self.name}은 {self._company}에서 일하는 중이다.')