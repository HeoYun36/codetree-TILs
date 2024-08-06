numbers = list(map(int, input().split()))
if numbers[-1] == 0:
    numbers.pop()

for num in numbers[-1::-1]:
    print(num, end=" ")