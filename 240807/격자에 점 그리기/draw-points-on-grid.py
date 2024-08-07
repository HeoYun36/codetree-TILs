n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(n)] for _ in range(n)
]

num = 1
for _ in range(m):
    x, y = map(int, input().split())
    arr_2d[x - 1][y - 1] += num
    num += 1

for row in arr_2d:
    for col in row:
        print(col, end=" ")
    print()