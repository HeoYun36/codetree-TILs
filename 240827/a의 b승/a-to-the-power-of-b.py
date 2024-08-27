a, b = map(int, input().split())

prod = 1
for num in range(b):
    prod *= a

print(prod)