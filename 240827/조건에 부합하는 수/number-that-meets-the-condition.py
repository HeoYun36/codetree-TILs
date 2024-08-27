a = int(input())

num_list = []

for num in range(1, a + 1):
    if (num % 2 == 0 and num % 4 != 0) or ((num // 8) % 2 == 0) or ((num % 7) < 4):
        continue
    num_list.append(num)

print(*num_list)