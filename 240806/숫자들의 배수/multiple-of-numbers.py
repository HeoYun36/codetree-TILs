n = int(input())

nums = []
num = 0

for i in range(1, 100):
    a = n * i
    nums.append(a)
    if a % 5 == 0:
        num += 1
        if num == 2:
            break
    
for num in nums:
    print(num, end=" ")