a, b, c = map(int, input().split())

satisfied = True

for num in range(a, b + 1):
    if num % c == 0:
        satisfied = False

if satisfied:
    print("YES")
else:
    print("NO")