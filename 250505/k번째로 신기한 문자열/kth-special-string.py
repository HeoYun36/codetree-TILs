n, k, t = input().split()
n, k = int(n), int(k)
str_list = [input() for _ in range(n)]

arr = []

for i in range(n):
    cnt = 0
    for j in range(len(t)):
        if str_list[i][j] == t[j]:
            cnt += 1
        else:
            break
        
    if cnt == len(t):
        arr.append(str_list[i])

arr.sort()

print(arr[k - 1])

