n, t = map(int, input().split())

num_list = list(map(int, input().split()))

cnt1 = 0
cnt2 = 1

for i in range(1, n):
    if num_list[i] > t and num_list[i - 1] > t:
        cnt2 += 1
    else:
        cnt2 = 1

    if cnt2 > cnt1:
        cnt1 = cnt2

print(cnt1)

