offset = 100
n = int(input())

arr_2d = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(n):
    x, y = map(int, input().split())
    x += offset
    y += offset
    for row in range(x, x + 8):
        for col in range(y, y + 8):
            arr_2d[row][col] += 1

area = 0

for row in range(201):
    for col in range(201):
        if arr_2d[row][col] >= 1:
            area += 1

print(area)