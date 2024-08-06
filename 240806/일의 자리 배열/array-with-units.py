nums = list(map(int, input().split()))

for i in range(3, 11):
    num = nums[-1] + nums[-2]
    nums.append(num % 10)

for num in nums:
    print(num, end=" ")