def remove_duplicate(number):
    # 구현
    # 목록을 순회하고 중복된 숫자이면 제거하고 나머지를 반환리스트에넣는다.
    unique_numbers =[]
    for num in numbers:
        seen_num = False
        for prev_num in unique_numbers:
            if num == prev_num:
                seen_num = True
        if seen_num == False:
            unique_numbers.append(num)

    return unique_numbers


def remove_duplicate2(number):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def remove_duplication3(number):
    return list(set(number))

numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]
print(remove_duplicate(numbers))