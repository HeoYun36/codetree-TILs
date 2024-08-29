n = int(input())

satisfied = False

for num in range(2, n):
    if n % num == 0:
        satisfied = True

if satisfied:
    print("C")
else:
    print("N")