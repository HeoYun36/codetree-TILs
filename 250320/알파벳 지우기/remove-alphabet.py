str1 = input()
str2 = input()

def str_f(input_str):
    result = ''
    for i in range(len(input_str)):
        if '0' <= input_str[i] and input_str[i] <= '9':
            result += input_str[i]

    return result

sum_of_num = int(str_f(str1)) + int(str_f(str2))
print(sum_of_num)