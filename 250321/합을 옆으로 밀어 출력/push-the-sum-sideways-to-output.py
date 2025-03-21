n = int(input())

result = 0

for i in range(n):
    result += int(input())

result = str(result)

result = result[1:] + result[0]

print(result)