n = int(input())

if n == 0:
    print(0)

digits = [0 for i in range(100)]
idx = 0

while n > 0:
    digits[idx] = n % 2
    idx += 1

    n //= 2

for i in range(idx - 1, -1, -1):
    print(digits[i], end="")