a, b = map(int, input().split())
n = list(map(int, input()))

num = 0

for i in range(len(n)):
    num = num * a + n[i]

digit = []

while True:
    if num < b:
        digit.append(num)
        break

    digit.append(num % b)
    num //= b

for i in digit[::-1]:
    print(i, end='')