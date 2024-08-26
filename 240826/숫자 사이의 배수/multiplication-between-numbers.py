a, b = map(int, input().split())

sum_val = 0
n = 0

for num in range(a, b + 1):
    if num % 5 == 0 or num % 7 == 0:
        sum_val += num
        n += 1

print(f'{sum_val} {sum_val / n:.1f}')