n = int(input())

nums = list(map(int, input().split()))
max_num = 0
# 각 인덱스의 숫자와 그 인덱스 다음의 숫자의 차가 이익이다.
for i in range(n):
    for j in range(i + 1, n):
        # 그 이익의 최댓값을 구하라
        if nums[j] - nums[i] > max_num:
            max_num = nums[j] - nums[i]

print(max_num)