dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0
dir_num = 3

s = input()

for i in range(len(s)):
    if s[i] == "L":
        dir_num = (dir_num + 3) % 4 
    elif s[i] == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)




# dir_num = (dir_num + 1) % 4 # 우회전
# dir_num = (dir_num + 3) % 4 # 좌회전