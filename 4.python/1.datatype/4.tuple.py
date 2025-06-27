## 튜플은 리스트와 동일하나 데이터를 변경 할 수 없다.
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[1])
## print(tuple1[2] = 5 ) 오류 발생


tupleToList = list(tuple1) ## it is  a copy
tupleToList[2] = 5
print(tupleToList)
print(ListToTuple)

ListToTuple = tuple(tupleToList)


### 튜플안에 데이터를 여러개의 변수로 나누어 담을 ㅜㅅ있다
# 튜플 안 패킹

a, b,c = (1, 2, 3)
# a, b, _ = (1, 2, 3) 변수에 담지 않을 때에는 underbar을 사용한다.
print('a' ,a)
print('b',b)
print('c',c)

