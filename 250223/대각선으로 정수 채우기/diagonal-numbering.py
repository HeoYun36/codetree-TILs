
n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)] 
    for _ in range(n)
]

num = 1

for start_col in range(m):
    curr_row = 0
    curr_col = start_col

    while 0 <= curr_col and curr_row < n:
        arr_2d[curr_row][curr_col] = num

        curr_row += 1
        curr_col -= 1
        num += 1

for start_row in range(1, n):
    curr_col = m - 1
    curr_row = start_row

    while 0 <= curr_col and curr_row < n:
        arr_2d[curr_row][curr_col] = num

        curr_row += 1
        curr_col -= 1
        num += 1

for row in range(n):
    for col in range(m):
         print(arr_2d[row][col], end=' ')
    print()