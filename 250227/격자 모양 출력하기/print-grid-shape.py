n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y = map(int, input().split())
    arr_2d[x - 1][y - 1] = x * y

for row in range(n):
    for col in range(n):
        print(arr_2d[row][col], end=' ')
    print()