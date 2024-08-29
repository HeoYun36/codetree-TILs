a, b, c = map(int, input().split())

satisfied = False
for num in range(a, b + 1):
    if num % c == 0:
        satisfied = True

if satisfied:
    print("YES")
else:
    print("NO")