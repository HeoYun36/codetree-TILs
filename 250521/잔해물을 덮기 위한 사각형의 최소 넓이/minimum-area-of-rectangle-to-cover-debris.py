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


max_x2 = 0
max_y2 = 0

min_x1 = 2000
min_y1 = 2000

for i in range(2001):
    for j in range(2001):
        if arr_2d[i][j] == 1:
            if max_x2 <= i:
                max_x2 = i

            if max_y2 <= j:
                max_y2 = j

            if min_x1 >= i:
                min_x1 = i
            
            if min_y1 >= j:
                min_y1 = j

area = 0
for i in range(min_x1, max_x2 + 1):
    for j in range(min_y1, max_y2 + 1):
        area +=1

print(area)




