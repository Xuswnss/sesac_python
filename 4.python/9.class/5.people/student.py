from person import Person
class Student(Person): # 상속(inherit)
    def __init__(self, name, age, student_id):
        super().__init__(name, age) ## 부모 객체를 불러 그곳을통해 초기화
        self._student_id = student_id
        
        
    def study(self):
        print(f'{self.name}은 학교에서 공부하고 있습니다. 학번 : {self._student_id}')