a, b = map(int, input().split())

prod = 1

for num in range(a, b + 1):
    prod *= num
    
print(prod)