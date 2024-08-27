n = int(input())

num = 1

while n > 1:
    n //= num
    num += 1

print(num - 1)