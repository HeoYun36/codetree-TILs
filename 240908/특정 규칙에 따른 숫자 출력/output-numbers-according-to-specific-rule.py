cnt = 1

n = int(input())

for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(n - i):
        print(cnt, end=" ")
        cnt += 1
        if cnt >= 10:
            cnt = 1
    print()