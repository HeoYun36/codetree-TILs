n = int(input())

num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

cnt = 0

for i in range(n):
    if i == 0 or num_list[i] != num_list[i - 1]:
        cnt += 1

print(cnt)