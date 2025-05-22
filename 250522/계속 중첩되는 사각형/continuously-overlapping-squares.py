n = int(input())

arr_2d = [[0 for _ in range(201)] for _ in range(201)]


# 1이 빨간색 -1이 파란색
color = 1
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_2d[i][j] = color
    
    color *= -1

area = 0
for i in range(201):
    for j in range(201):
        if arr_2d[i][j] == -1:
            area += 1

print(area)