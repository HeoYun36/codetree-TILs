nums = list(map(int, input().split()))

min_num = nums[0]

for i in range(1, 3):
    if min_num > nums[i]:
        min_num = nums[i]

print(min_num)