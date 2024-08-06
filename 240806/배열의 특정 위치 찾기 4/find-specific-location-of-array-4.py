nums = list(map(int, input().split()))

n = 0
sum_of_even = 0

for num in nums:
    if num == 0:
        break
    elif num % 2 == 0:
        n += 1
        sum_of_even += num

print(f'{n} {sum_of_even}')