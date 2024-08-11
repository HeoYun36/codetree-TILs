a = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if a > num:
        print(1)
    else:
        print(0)