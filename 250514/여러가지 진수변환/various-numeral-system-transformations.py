n, b = map(int, input().split())

digit = []

while True:
    if n < b:
        digit.append(n)
        break

    digit.append(n % b)
    n //= b

for i in digit[::-1]:
    print(i, end='')