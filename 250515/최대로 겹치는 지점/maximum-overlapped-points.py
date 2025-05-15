n = int(input())

slot = [0] * 101

for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2 + 1):
        slot[j] += 1

print(max(slot))

