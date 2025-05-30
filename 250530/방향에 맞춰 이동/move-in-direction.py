n = int(input())

x, y = 0, 0

dir_dic = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    a, b = input().split()
    for _ in range(int(b)):
        x += dx[dir_dic[a]]
        y += dy[dir_dic[a]]


print(x, y)

