n = int(input())

if n == 1:
    print("*")
else:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            elif j >= i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()