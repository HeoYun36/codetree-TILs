n = int(input())

satisfied = True

for num in range(2, n):
    if n % num == 0:
        satisfied = False

if satisfied:
    print('P')
else:
    print('C')