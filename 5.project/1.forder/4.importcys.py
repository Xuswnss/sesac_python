import sys
from generators.user_generator import UserGenerator
 
class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generator_user(count)
        for name, birthday, gender ,address in  data:
            print(f'Name : {name}\nBirthday: {birthday}\nGender :{gender}\nAddress: {address}\n')
            
# print(sys.argv)
# sys.argv[0] #실행파일명
# sys.argv[1] #첫번째 인자


if len(sys.argv) > 1:
    num_data = int(sys.argv[1])
else:
    num_data = input('원하는 데이터 개수를 입력하시오 : ')

my_data = DisplayData
my_data.print_data(num_data)