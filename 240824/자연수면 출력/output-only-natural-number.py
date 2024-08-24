a, b = map(int, input().split())

if a <= 0:
    print(0)
elif int(a) == a:
    for _ in range(b):
        print(a, end='')