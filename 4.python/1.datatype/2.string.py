str = 'hello, world!'
str2 = 'for the first time in forever'


print("-----------Start Python-------------")
print(str)


print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title()) # 문장의 단어마다 대문자 변경
print(str.strip()) #앞 뒤로 불필요한 공백을 제거
print(str.lstrip()) # 왼쪽 공백 제거
print(str.rstrip) # 오른쪽 공백 제거
print(str.split()) # 문자를 단위로 자른다.

print(str2)

words = str2.split()
print(words[2].upper())
print(','.join(words))







print("-----------End Python-------------")

