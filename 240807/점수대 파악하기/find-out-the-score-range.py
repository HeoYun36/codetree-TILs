nums = list(map(int, input().split()))
count_arr = [0] * 10

for num in nums:
    if num == 0:
        break
    elif num > 10:
        count_arr[(num // 10) - 1] += 1

for num in range(10, 0, -1):
    print(f'{num * 10} - {count_arr[num -1]}')