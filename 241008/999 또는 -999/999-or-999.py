import sys

n_list = list(map(int, input().split()))

n_list = n_list[0:-1]

max_num = -sys.maxsize
min_num = sys.maxsize

for i in range(len(n_list)):
    if max_num < n_list[i]:
        max_num = n_list[i]

for i in range(len(n_list)):
    if min_num > n_list[i]:
        min_num = n_list[i]

print(max_num, min_num)