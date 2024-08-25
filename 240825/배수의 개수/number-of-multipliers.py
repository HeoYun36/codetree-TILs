cnt1 = 0
cnt2 = 0

num_list = [int(input()) for _ in range(10)]

for num in num_list:
    if (num % 3 == 0) and (num % 5 == 0):
        cnt1 += 1
        cnt2 += 1
    elif num % 3 == 0:
        cnt1 += 1
    elif num % 5 == 0:
        cnt2 += 1

print(cnt1, cnt2)