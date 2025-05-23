n = int(input())

num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

if n == 1:
    print(1)
else:
    cnt = 1

    cnt_list = []

    for i in range(1, n):
        if num_list[i - 1] * num_list[i] < 0:
            cnt_list.append(cnt)
            cnt = 0

        cnt += 1

        if i == n - 1:
            cnt_list.append(cnt)

    print(max(cnt_list))
