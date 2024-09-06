cnt = 9

n = int(input())

for _ in range(n):
    for _ in range(n):
        print(cnt, end="")
        cnt -= 1
        if cnt <= 0:
            cnt = 9
    print()