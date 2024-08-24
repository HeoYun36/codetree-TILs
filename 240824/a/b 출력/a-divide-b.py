a, b = map(int, input().split())

num1 = a // b
num2 = a % b * 10

print(f'{num1}.', end='')
for _ in range(20):
    num1 = num2 // b
    print(num1, end='')
    num2 = num2 % b * 10