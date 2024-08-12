n = int(input())

arr = [0 for _ in range(101)]

for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        arr[i] += 1

max_num = 0

for i in range(101):
    if max_num < arr[i]:
        max_num = arr[i]

print(max_num)