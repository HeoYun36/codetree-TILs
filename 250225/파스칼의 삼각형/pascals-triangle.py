n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            arr_2d[i - 1][j - 1] = 1
        else:
            arr_2d[i - 1][j - 1] = arr_2d[i - 2][j - 1] + arr_2d[i - 2][j - 2]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(arr_2d[i - 1][j - 1], end=' ')
    print()