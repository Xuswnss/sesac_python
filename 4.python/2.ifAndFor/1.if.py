

def getGrade(score):
 if score >= 90:
         grade = 'grade a'
 elif score >= 80:
         grade = 'grade b'
 elif score >= 70:
         grade = 'grade c'
 else:
         grade = ' grade f'

         return grade

xuswns = getGrade(95)
print('xuswns of grade : ' , xuswns)


user = input("점수를 입력하세요  : " )

#내장함수(built in function)

userScore = getGrade(int(user))
print('사용자의 학점은는 ? : ')