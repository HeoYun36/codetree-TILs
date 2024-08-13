offset = 1000
area = 1

arr_2d = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += offset
    x2 += offset
    y1 += offset
    y2 += offset
    if i == 2:
        area = 2

    for row in range(x1, x2):
        for col in range(y1, y2):
            arr_2d[row][col] = area

sum_of_area = 0

for row in range(2001):
    for col in range(2001):
        if arr_2d[row][col] == 1:
            sum_of_area += 1

print(sum_of_area)