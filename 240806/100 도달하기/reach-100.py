n = int(input())

nums = [1]
nums.append(n)

for num in nums:
    if nums[-1] > 100:
        break
    nums.append(nums[-1] + nums[-2])
for num in nums:
    print(num, end=" ")