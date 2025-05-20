n = int(input())

arr_2d = [[0 for _ in range(201)] for _ in range(201)]

offset = 100

for i in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr_2d[i][j] += 1

area = 0

for i in range(201):
    for j in range(201):
        if arr_2d[i][j] >= 1:
            area += 1

print(area)

