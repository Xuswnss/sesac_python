numbers = [1,2,5,3,7,9,22,4,66,77,8]

# 원하는 숫자를 발견하면 해당 인덱스를 반환하고 없으면 -1을 반환한다.
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

target = 22
print(linear_search(numbers, target))
