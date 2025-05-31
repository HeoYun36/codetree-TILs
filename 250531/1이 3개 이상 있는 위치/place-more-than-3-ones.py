n = int(input())

arr_2d = [list(map(int, input().split())) for _ in range(n)]

def f(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dx_list = [0, 1, 0, -1]
dy_list = [1, 0, -1, 0]

cnt1 = 0

for i in range(n):
    for j in range(n):
        cnt2 = 0
        for dx, dy in zip(dx_list, dy_list):
            x = j + dx
            y = i + dy
            if f(x, y) and arr_2d[x][y] == 1:
                cnt2 += 1
        
        if cnt2 >= 3:
            cnt1 += 1

print(cnt1)