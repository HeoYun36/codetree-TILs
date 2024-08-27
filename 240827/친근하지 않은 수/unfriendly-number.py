n = int(input())

cnt = 0
for num in range(1, n + 1):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        continue
    cnt += 1

print(cnt)