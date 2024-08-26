n = int(input())

sum_val = 0

for num in range(1, n):
    if n % num == 0:
        sum_val += num

if sum_val == n:
    print('P')
else:
    print('N')