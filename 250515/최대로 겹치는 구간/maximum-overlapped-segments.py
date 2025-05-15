n = int(input())

offset = 100

slot = [0] * 201




for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100

    for i in range(x1, x2):
        slot[i] += 1

print(max(slot))

