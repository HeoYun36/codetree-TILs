num_list = list(map(int, input().split()))

sum_val = 0
for i in range(len(num_list)):
    if num_list[i] == 0:
        sum_val = num_list[i - 1] + num_list[i - 2] + num_list[i - 3]
        break

print(sum_val)