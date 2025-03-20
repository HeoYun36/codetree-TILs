str1, str2 = input().split()

sum_of_num = 0

def str_f(input_str):
    result = ''
    for i in range(len(input_str)):
        if '0' <= input_str[i] and input_str <= '9':
            result += input_str[i]
        else:
            break

    return result


sum_of_num = int(str_f(str1)) + int(str_f(str2))

print(sum_of_num)

