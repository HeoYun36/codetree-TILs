n, b = map(int, input().split())

digit = []

while True:
    if n < b:
        digit.apppend(n)
        break

    digit.append(n % b)
    n //= b

for i in digit:
    print(i, end='')