start, end = map(int, input().split())

cnt1 = 0
for num in range(start, end + 1):
    cnt2 = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt2 += 1
    if cnt2 == 3:
        cnt1 += 1

print(cnt1)