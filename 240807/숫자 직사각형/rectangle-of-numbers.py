n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)] 

num = 1

for row in range(n):
    for col in range(m):
        arr[row][col] = num
        num +=1


for row in range(n):
    for col in range(m):
        print(arr[row][col], end=" ")
    print()