a, b = map(int, input().split())

if a < b:
    num1 = a
    num2= b
else:
    num1 = b
    num2 = a

for i in range(b, a - 1, -1):
    print(i, end=' ')