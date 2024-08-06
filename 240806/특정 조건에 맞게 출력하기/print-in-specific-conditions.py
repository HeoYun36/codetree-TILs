nums = list(map(int, input().split()))

for num in nums:
    if num == 0:
        break
    elif num % 2 == 0:
        print(num // 2, end=" ")
    elif num % 2 != 0:
        print(num + 3, end=" ")