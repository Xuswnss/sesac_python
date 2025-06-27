def getGrade(score):
            if score >= 90:
                    grade ='gradeA'

            elif score >= 80:
                    grade = 'gradeB'
            elif score >= 70:
                    grade = 'gradeC'
            else:      
                        grade ='gradeF'
            return grade

name = input('Write your name  :')
score = input('write your score')
grade = getGrade(score)
print(f'student {name} : score{score}')
