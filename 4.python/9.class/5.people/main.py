from person import Person
from student import Student
from employee import Employee

alice = Person("Alice", 23)
bob = Person('Bob' , 32)
tom = Student('tom', 20,'a2222')
jun = Employee('jun', 20, 'sesac')

alice.greet()
bob.greet()

bob.name ="BOB"
bob.greet()

tom.greet()
tom.study()

jun.greet()
jun.work()