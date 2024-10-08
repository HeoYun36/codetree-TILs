import sys
num_list = list(map(int, input().split()))

max_num = -sys.maxsize

for i in range(len(num_list)):
    if max_num < num_list[i]:
        max_num = num_list[i]

print(max_num)