a_x1, a_y1, a_x2, a_y2 = map(int ,input().split())

b_x1, b_y1, b_x2, b_y2 = map(int ,input().split())

offset = 1000

a_x1 += offset
a_y1 += offset
a_x2 += offset
a_y2 += offset

b_x1 += offset
b_y1 += offset
b_x2 += offset
b_y2 += offset

arr_2d = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        arr_2d[i][j] += 1

for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        arr_2d[i][j] -= 1

x_arr = []
y_arr = []

for i in range(2001):
    for j in range(2001):
        if arr_2d[i][j] == 1:
            x_arr.append(i)
            y_arr.append(j)

max_x2 = max(x_arr) + 1
max_y2 = max(y_arr) + 1

min_x1 = min(x_arr)
min_y1 = min(y_arr)

area = 0

for i in range(min_x1, max_x2):
    for j in range(min_y1, max_y2):
        area += 1

print(area)

