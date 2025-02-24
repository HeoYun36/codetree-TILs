n = int(input())

arr_2d = [[0 for _ in range(n)] for _ in range(n)]

num = 1

state = True

for col in range(n - 1, -1, -1):
    if state == False:
        for row in range(n):
            arr_2d[row][col] = num
            num += 1
        state = True
    else:
        for row in range(n - 1, -1, -1):
            arr_2d[row][col] = num
            num += 1
        state = False

for row in range(n):
    for col in range(n):
        print(arr_2d[row][col], end=' ')
    print()
            