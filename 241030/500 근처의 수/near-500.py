nums = list(map(int, input().split()))
max_num = 0
min_num = 1001

for i in range(len(nums)):
    # 500미만 최대값 찾기 
    if nums[i] > max_num and nums[i] < 500:
        max_num = nums[i]
    # 500 초과 최소값 찾기
    if nums[i] < min_num and nums[i] > 500:
        min_num = nums[i]
    
print(max_num, min_num)