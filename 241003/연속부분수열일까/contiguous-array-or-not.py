import sys

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n1):
    success = True
    
    for j in range(n2):
        if i + j >= n1:
            success = False
            break

        if a[i + j] != b[j]:
            success = False
            break

    if success:
        print("Yes")
        sys.exit()

print("No")