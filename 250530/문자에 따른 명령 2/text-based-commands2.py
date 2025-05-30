inst_list = input()

x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = 3

for letter in inst_list:
    if letter == 'L':
        dir_num = (dir_num - 1) % 4
    elif letter == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)