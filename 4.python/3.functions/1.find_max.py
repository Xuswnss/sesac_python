numbers = [-1,2,3,4,5,6,7,8,-9]

def find_max(num):
    result = num[0]
    ## 현재값이 다음값보다 크면 현재 값을 result에 넣는다.
    for i in num:
        print(i)
        if i > result:
            result = i
    return result
      

print('가장큰수 : ',find_max(numbers))

print(max(numbers))
print(min(numbers))

numbers.sort(reverse=True)
print(numbers[0])