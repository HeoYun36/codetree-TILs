num_list = [int(input()) for _ in range(10)]

sum_val = 0
n = 0

for num in num_list:
    if num >= 0 and num <= 200:
        sum_val += num
        n += 1

print(f'{sum_val} {sum_val / n:.1f}')