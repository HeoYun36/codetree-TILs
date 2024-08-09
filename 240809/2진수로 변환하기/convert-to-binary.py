n = int(input())

digits = []

while n > 0:
    digits.append(n % 2)
    n //= 2

for i in digits[::-1]:
    print(i, end="")