nums = list(map(int, input().split()))
min_num = nums[0]
for i in range(1, 3):
    if min_num > nums[i]:
        min_num = nums[i]

if nums[0] == min_num:
    print(1, end= " ")
else:
    print(0, end= " ")

if nums[0] == nums[1] and nums[1] == nums[2]:
    print(1)
else:
    print(0)