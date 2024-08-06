numbers = list(map(int, input().split()))
numbers.pop()

for num in numbers[-1::-1]:
    print(num, end=" ")