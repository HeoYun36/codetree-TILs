n = int(input())

num_list = []

for num in range(1, n + 1):
    if (num % 2 == 0) or (num % 10 == 5) or (num % 3 == 0 and num % 9 != 0):
        continue
    else:
        num_list.append(num) 

print(*num_list)