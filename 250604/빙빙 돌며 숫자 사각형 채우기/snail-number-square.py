n, m = map(int, input().split())

arr_2d = [[0 for _ in range(m)] for _ in range(n)]

def f(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

arr_2d[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not f(nx, ny) or arr_2d[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x = x + dxs[dir_num]
    y = y + dys[dir_num]
    arr_2d[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=' ')
    print()
