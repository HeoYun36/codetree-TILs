n = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        print(num_list[i], end=" ")