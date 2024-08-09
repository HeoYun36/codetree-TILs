digits = list(input())
num = 0

for i in range(len(digits)):
    num *= 2
    num += int(digits[i])

print(num)