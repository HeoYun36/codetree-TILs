n = int(input())
x = 0
y = 0

dir_list = ["E", "S", "W", "N"]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    d, s = input().split()
    index = 0 
    for i in range(4):
        if dir_list[i] == d:
            index = i
    x += int(s) * dx[index]
    y += int(s) * dy[index]

print(x, y)