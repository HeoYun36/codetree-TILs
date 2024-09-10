start, end = map(int, input().split())

cnt = 0

for num in range(start, end + 1):
    sum_val = 0
    for i in range(1, num):
        if num % i == 0:
            sum_val += i
    if num == sum_val:
        cnt += 1

print(cnt)