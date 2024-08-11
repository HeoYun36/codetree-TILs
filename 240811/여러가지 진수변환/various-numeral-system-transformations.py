n, b = map(int, input().split())

digits = [0 for _ in range(100)]
idx = 0

while n > 0:
    digits[idx] = n % b
    idx += 1

    n //= b


for i in range(idx - 1, -1, -1):
    print(digits[i], end="")