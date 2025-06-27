myList = [2,3,4,5]
print(myList)
print(len(myList))
print(myList[1])
## print(myList[5]) 
print(myList[-1]) # 거꾸로 갈 수 있음 (대부분의 언어는 허용하지 않음!)


print(myList[1:3]) ## 1번 익데스 부터 3번쨰 인덱스 ㅣ미만
print(myList[:2]) ## 처음부터 2번 인덱스 미만
print(myList[2: ])#2번 인게스에서 끝까지

print('-'*10)
myList.append(6)
print(myList)
myList.insert(2,10)
print(myList)


list2 = [7, 8, 9]
print(myList)
print(list2)
myList.extend(list2)
print(myList)
print(list2)

## something remove()
myList.remove(10) #10이라는 숫자를 삭제할 것이다
print(myList)
myList.pop(3) ##index = 3 remove
print(myList)

myList.pop() ## if no element is given, it will remove the last ele

print(myList)

##search list

## before sorting

print('-'*10)
list3 = [1,2,3,4,5,3,2,1]
index_of_3 = list3.index(3)
count2 = list3.count(2)

print(count2)
sort_list = list3.sort() ##some functions return a copy while another modify the original data
print(list3)
## sorted -> return 값이 존재
# sort -> 복제본을 반환
## after sorting 
sortedList = sorted(list3) 
list3.sort(reverse=True)
print(list3)

list3.reverse()
print(list3)

list3copy = list3.copy()
print(list3copy)


##list comprehension
## 리스트 안에 반복문 또는 조건문을 통해서, 리스트 안에 채워질 요소를 정의할 수 있는 문법
number = [x for x in range(10)] 
print('list comprehesion : ' , number)

## 1-10가지의 숫자를 만들어서 리스트에 채워라
numbers = [ num for num in range(1,11)]
## 1-10까지의 숫자를 만들어서 그 제곱수로 채워라
numbers = [num**2 for num in range(1,11)] 
print('pow() : ', numbers)

## 1-10까지의 숫자중 짝수만
numbers = [ num for num in range(1,11) if num %2 == 0]



