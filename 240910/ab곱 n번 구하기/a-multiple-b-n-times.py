n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    sum_val = 1
    for num in range(a, b + 1):
        sum_val *= num
    print(sum_val)