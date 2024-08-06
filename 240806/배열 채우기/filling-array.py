numbers = list(map(int, input().split()))

a = []

for num in numbers:
    if num == 0:
        break
    else:
        a.append(num)


for num in a[-1::-1]:
    print(num, end=" ")