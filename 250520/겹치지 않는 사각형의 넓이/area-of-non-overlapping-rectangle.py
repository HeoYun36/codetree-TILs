arr_2d = [[0 for _ in range(2001)] for _ in range(2001)]


a_x1, a_y1, a_x2, a_y2 = map(int, input().split())

b_x1, b_y1, b_x2, b_y2 = map(int, input().split())

m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        arr_2d[i][j] = 1

for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        arr_2d[i][j] = 1

for i in range(m_x1, m_x2):
    for j in range(m_y1, m_y2):
        arr_2d[i][j] = 2


area = 0

for i in range(2001):
    for j in range(2001):
        if arr_2d[i][j] == 1:
            area +=1

print(area)

