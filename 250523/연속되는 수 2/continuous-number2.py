n = int(input())

num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

if n == 1:
    print(1)
else:
    cnt = 1

    arr = []



    for i in range(1, n):
        if num_list[i] != num_list[i - 1]:
            arr.append(cnt)
            cnt = 1
        else:
            cnt += 1

        if i == n - 1:
            arr.append(cnt)

    print(max(arr))