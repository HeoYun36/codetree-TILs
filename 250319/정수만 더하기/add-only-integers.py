str_input = input()


sum_of_num = 0
for i in range(len(str_input)):
    if '0' <= str_input[i] and str_input[i] <= '9':
        sum_of_num += int(str_input[i])

print(sum_of_num)
