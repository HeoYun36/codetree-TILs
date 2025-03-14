str_input = input()

print(str_input)
for _ in range(len(str_input)):
    str_input = str_input[-1] + str_input[:-1]
    print(str_input)
