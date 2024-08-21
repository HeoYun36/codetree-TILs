a, b, c = map(int, input().split())

if a < b and b < c:
    print(b)
elif a > b and b > c:
    print(b)
elif a > b and a < c:
    print(a)
elif a > c and a < b:
    print(a)
else:
    print(c)