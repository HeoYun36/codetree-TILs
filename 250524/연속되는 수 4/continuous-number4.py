n = int(input())

num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

cnt1 = 1
cnt2 = 1

for i in range(1, n):
    if num_list[i] > num_list[i - 1]:
        cnt2 += 1
    else:
        cnt2 = 1

    if cnt2 > cnt1:
        cnt1 = cnt2

print(cnt1)