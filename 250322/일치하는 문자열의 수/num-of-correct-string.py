n, str1 = input().split()

cnt = 0
for _ in range(int(n)):
    str2 = input()

    if str1 == str2:
        cnt += 1

print(cnt)
