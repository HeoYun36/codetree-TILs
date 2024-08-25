cnt = 0

num_list = [int(input()) for _ in range(10)]

for num in num_list:
    if num % 2 != 0:
        cnt += 1

print(cnt)