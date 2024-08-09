n = int(input())

arr_2d = [[0 for i in range(201)] for i in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2): 
            arr_2d[row][col] = 1

area = 0
for x in range(201):
    for y in range(201):
        if arr_2d[x][y] == 1:
            area += 1

print(area)