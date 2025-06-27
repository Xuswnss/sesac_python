print('4.eg.Py')

numbers = [1, 2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0:
        print(f"number {num} is evenNumber")

    elif num % 2 == 1:
        print(f"number {num} is oddNumber")

def getEvenNumbers(numbers):
    even_number = []

    for num in numbers:
        if num % 2 == 0:
            even_number.append(num)
            print(":" ,even_number)

            return even_number
    
even = getEvenNumbers(numbers)
print("짝수는 : ? ", even)


print("*"*10)

students ={
  '김하은': 92,
  '이민수': 85,
  '박지우': 78,
  '최수빈': 90,
  '정서준': 100,
  '강예은': 74,
  '조도윤': 88,
  '윤유진': 80,
  '장지호': 95,
  '임지윤': 73
}

## 방법 1
def getScore(stu):
    print(stu)
    result = []
    for name, score in stu.items():
       print(name,score)
       if score >= 90:
           print(name)
           result.append(name)
    return result
           
           
            

print(getScore(students))