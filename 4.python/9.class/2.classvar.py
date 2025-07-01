class Person:
# class(객체) 안에 있는 함수를 method라고 부른다.
# _변수명 -> protected
#__변수명 -> private

    _count = 0 #class variable (공통, 공용 영역에 해당함)

    def __init__(self, name, age): # attribute -> 개별 데이타를 저장하는 공간
        self.name = name
        self.age = age
        # self.count +=1 <- 완전 오답.
        Person.count += 1 #class variable에 접근해서 1을 증가한다.
        
        
    def greet(self): # method
        print(f'안녕하세요 저는 {self.name}입니다.')


    def ride_car(self):
        print(f'{self.name}는 지금 운전중...')
        
    ## getter (값을 읽어오기)
    ## setter (값을 set)
    
    def get_count(cls):
        print(f'자동차를 탑니다')
        
    @classmethod #decorator -> 나의 함수에 기능을 더해주는 것
    def get_count(cls): #class 자체에 접근하기 위해서 cls 라는 클래스 자신을 칭하는 변수를 받아옴
        return cls.count

p =  Person('xuswns', 20) # 객체를 찍어낸 것! = 실체화 = instant =  instantiations
p2 = Person('timi' , 10)
print(f'만들어진 사람수 : {p.get_count()}')

p3 = Person('daljf', 30)


# person1 = {
#     'name' : '김철수',
#     'age' :30,
#     '__class__' : Person,
#     '__dict__': {'name' : '김철수', 'age' : 30}
# } <- 실제로 person은 이런식으로 내부가 작성되어 있다.



