n, k = map(int, input().split())

slot = [0] * (n + 1)

for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        slot[j] += 1


print(max(slot))



