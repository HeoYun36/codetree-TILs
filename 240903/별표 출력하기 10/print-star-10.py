n = int(input())

for i in range(n * 2):
    if i % 2 == 0:
        for j in range(i // 2 + 1):
            print("*", end=" ")
    else:
        for j in range((n * 2 - i) // 2 + 1):
            print("*", end=" ")
    print()