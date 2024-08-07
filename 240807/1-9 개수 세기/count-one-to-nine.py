count_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    count_arr[num - 1] += 1

for num in count_arr:
    print(num)