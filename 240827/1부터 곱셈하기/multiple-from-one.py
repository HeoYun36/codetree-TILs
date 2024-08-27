n = int(input())

prod = 1

for num in range(1, 11):
    prod *= num

    if prod >= n:
        print(num)
        break