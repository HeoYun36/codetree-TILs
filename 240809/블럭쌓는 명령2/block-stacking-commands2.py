n, k = map(int, input().split())
arr = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a - 1, b):
        arr[i] += 1

max_num = 0
for num in arr:
    if max_num < num:
        max_num = num

print(max_num)