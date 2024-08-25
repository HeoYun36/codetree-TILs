n = int(input())

num_list = [int(input()) for _ in range(n)]

for num in num_list:
    if num % 2 != 0 and num % 3 == 0:
        print(num)