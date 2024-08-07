nums = list(map(int, input().split()))

arr = [0] * 9

for num in nums:
    if num == 0:
        break
    elif num // 10 > 0:
        arr[(num // 10) - 1] += 1

for i in range(1, 10):
    print(f'{i} - {arr[i - 1]}')