n = int(input())

arr = [0 for _ in range(201)]

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        arr[i] += 1

max_num = 0
for i in range(201):
    if max_num <= arr[i]:
        max_num = arr[i]

print(max_num)