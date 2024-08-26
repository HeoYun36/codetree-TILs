a, b = map(int, input().split())

if a > b:
    a, b = b, a

sum_val = 0

for num in range(a, b + 1):
    if num % 5 == 0:
        sum_val += num

print(sum_val)