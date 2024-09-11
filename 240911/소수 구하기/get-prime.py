n = int(input())

for num in range(2, n + 1):
    cnt = 0
    for i in range(1, n + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        print(num, end=" ")