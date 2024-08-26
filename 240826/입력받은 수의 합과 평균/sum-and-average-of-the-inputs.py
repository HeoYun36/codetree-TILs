n = int(input())

num_list = [int(input()) for _ in range(n)]

sum_val = 0

for num in num_list:
    sum_val += num

print(f'{sum_val} {sum_val / n:.1f}')