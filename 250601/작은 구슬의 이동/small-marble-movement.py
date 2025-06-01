n, t = map(int, input().split())

r, c, d = input().split()
r, c = int(r), int(c)

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

def f(x, y):
    return 0 < x and x <= n and 0 < y and y <= n

dir_dic = {
    "R" : 0,
    "D" : 1,
    "U" : 2,
    "L" : 3
}

dir_num = dir_dic[d]
for _ in range(t):
    nr = r + dr[dir_num]
    nc = c + dc[dir_num]

    if not f(nr, nc):
        dir_num = 3 - dir_num
    else:
        r = r + dr[dir_num]
        c = c + dc[dir_num]        

print(r, c)
