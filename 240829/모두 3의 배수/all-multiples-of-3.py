num_list = [int(input()) for _ in range(5)]

satisfied = True
for num in num_list:
    if num % 3 != 0:
        satisfied = False

if satisfied:
    print(1)
else:
    print(0)