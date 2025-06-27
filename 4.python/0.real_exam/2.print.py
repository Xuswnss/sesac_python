name = 'alice'
name1 = 'xuswns'
name2 = 'Riku'
print(name)
print('Hello, ' + name) #덧셈 연산
print('Hello, ' , name) # argument(인자)
print('hello, {}!!'.format(name))
print('hello, {1}!! {0}??'.format(name,name))

print("Hello, %s!!" % name) # %s는 문자열을 출력하는 곳이다
print("Hello, %s!! %s" % (name1, name2) )# %s는 문자열을 출력하는 곳이다

##결론적으로 위에 다양한 것들을 거쳐서 지금 가장 많이 스는건 f스트림의 표기법이다

print(f'hello, {name}!!')