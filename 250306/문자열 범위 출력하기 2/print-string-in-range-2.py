str_input = input()
num = int(input())

if len(str_input) < num:
    for i in range(-1, 0, -1):
        print(str_input[i], end='')
else:
    for i in range(-1, -1 - num, -1):
        print(str_input[i], end='')