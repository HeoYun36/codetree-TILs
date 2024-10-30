import sys

n = int(input())
nums = list(map(int, input().split()))
min_num = sys.maxsize
x = 0


# 두개 숫자를 고르는데 만약 음수가 되면 부호를 바꿔줘야 함
for i in range(n):
    for j in range(n):
        if j != i:
           x = nums[i] - nums[j]
           if x < 0:
            x = -x
            if x < min_num:
                min_num = x

print(min_num)