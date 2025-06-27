## json 과 유사하나 같지 않다.

dict = {
            "name" : "xuswns",
            "age" : 20,
            "location" : "seoul"
}

print(dict['name']) ## name이라는 키가 가지고 있는 값은?
print(dict["age"])
user1 = {
            "name" : "jjj",
            'age' : 30,
            'location' : "jeju"
}

user1['age'] = 20
print(user1['age']) #original value changed

user1['car'] = 'hyunDai K5'
print(user1)

user1['car'] = "" #지워진 것이아니라 빈값을 할당한 것임
print(user1)

## 특정 키 값을 지우는 키워드는 del이다
# json의 공식 문법은 쌍따옴표 dic은 싱글 따옴표
# del은 keyword이므로 변수명으로 만들 수 없음
del user1['car']
print(user1)

print(user1.keys()) #key
print(user1.values())
print(user1.items())

user_item = user1.items()
user_item_list = list(user_item)
print(user_item_list)
print(user_item_list[1])

## 리스트와, 튜플과, 딕셔너리를 구분할 줄 알고 자유롭게 다룰 줄 알아야 한다
# [], (), {key, value}