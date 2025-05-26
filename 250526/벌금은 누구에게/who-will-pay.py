n, m, k = map(int, input().split())

arr = [0] * n

idx = -1
for _ in range(m):
    num = int(input())
    arr[num - 1] += 1

    if arr[num - 1] >= k:
        idx = num
        break

print(idx)
        