n = int(input())

num_list = [int(input()) for _ in range(n)]

sum_val = 0

for num in num_list:
    if (num % 2 != 0) and (num % 3 == 0):
        sum_val += num

print(sum_val)