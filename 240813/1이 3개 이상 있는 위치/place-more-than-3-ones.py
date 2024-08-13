# print(cnt)

dx = [1, 0, -1, 0]
dy = [0, 1, 0 , -1]

# cnt = 0

n = int(input())

arr_2d = [list(map(int, input().split())) for _ in range(n)]

cnt1 = 0

for row in range(n):
    for col in range(n):
        x = row
        y = col
        cnt2 = 0   
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if arr_2d[nx][ny] == 1:
                cnt2 += 1
        if cnt2 >= 3:
            cnt1 += 1

print(cnt1)