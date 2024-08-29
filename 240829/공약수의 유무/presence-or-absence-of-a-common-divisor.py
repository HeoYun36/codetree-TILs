a, b = map(int, input().split())

satisfied = False

for num in range(a, b + 1):
    if 1920 % num == 0 and 2880 % num == 0:
        satisfied = True

if satisfied:
    print(1)
else:
    print(0)