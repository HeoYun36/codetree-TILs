import sys
n = int(input())

num_list = list(map(int ,input().split()))

min_num = sys.maxsize

cnt = 0

for i in range(len(num_list)):
    if min_num > num_list[i]:
        min_num = num_list[i]

for i in range(len(num_list)):
    if min_num == num_list[i]:
        cnt += 1

print(min_num, cnt)