count_arr = [0] * 10
nums = list(map(int, input().split()))

for num in nums:
    count_arr[num - 1] += 1


for i in range(1, 7):
    print(f'{i} - {count_arr[i - 1]}')