num_list = list(map(int, input()))

num = 0

for i in range(len(num_list)):
    num = num * 2 + num_list[i]

print(num)