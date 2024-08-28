sum_of_age = 0
n = 0

while True:
    age = int(input())

    if age >= 20 and age < 30:
        sum_of_age += age
        n += 1
    else:
        break

print(f'{sum_of_age / n:.2f}')