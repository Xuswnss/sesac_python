import random as r

print("random number")
print('random number ', r.randint(1, 100)) # 1-100까지를 포함하는 랜덤 숫자 생성

def roll_dice():
           return  r.randint(1,6)

print(f'주사위 던진 결과 {roll_dice()}')

counts = [0,0,0,0,0,0]
def roll_dices(numbers):

    for i in range(numbers):
        result = roll_dice()
        counts[result - 1] += 1
## eg. 6이 나오면 index = 6-1 = 5번쨰 가 1이 증가한다.    
roll_dices(100)
for i in range(6):
    print(f'{i+1}이 나온 횟수  :{counts[i]} 확률 : {counts[i]/ sum(counts)}')

# counts2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} <- 하드 코딩 아래가 Modern ver
counts2 = {i:0 for i in range(1,7)}
print(counts2)

def roll_dices2(numbers):

    for i in range(numbers):
        result = roll_dice()
        counts2[result] += 1
        
roll_dices2(100_000)
print(counts2)

for dice_num, dice_count in counts2.items():
    print(f'주사위 수 {dice_num}이 나온 횟수는 {dice_count} 입니다. ')
    

       