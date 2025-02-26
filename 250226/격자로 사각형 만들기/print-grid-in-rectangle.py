n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for col in range(n):
    arr_2d[0][col] = 1

for row in range(1, n):
    arr_2d[row][0] = 1

for row in range(1, n):
    for col in range(1, n):
        arr_2d[row][col] = arr_2d[row][col - 1] + arr_2d[row - 1][col - 1] + arr_2d[row - 1][col]

for row in range(n):
    for col in range(n):
        print(arr_2d[row][col], end=' ')
    print()