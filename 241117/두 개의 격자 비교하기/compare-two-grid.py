n, m = map(int, input().split())

new_arr = [[0 for _ in range(m)] for _ in range(n)]

arr1 = [list(map(int ,input().split())) for _ in range(n)]

arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            new_arr[i][j] = 1

for i in range(n):
    for j in range(m):
        print(new_arr[i][j], end=' ')
    print()
