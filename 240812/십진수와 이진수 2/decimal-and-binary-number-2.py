n = input()

num = 0

for i in range(len(n)):
    num *= 2
    num += int(n[i])

num *= 17

digits = [0 for _ in range(100)]
idx = 0

while num > 0:
    digits[idx] = num % 2
    idx += 1

    num //= 2


for i in range(idx - 1, -1, -1):
    print(digits[i], end="")