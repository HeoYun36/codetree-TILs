n = int(input())

for _ in range(n):
    a, b = map(int ,input().split())
    sum_even_val = 0
    for num in range(a, b + 1):
        if num % 2 == 0:
            sum_even_val += num
    print(sum_even_val)