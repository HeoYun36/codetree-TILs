str_input = input()

for i in range(len(str_input)):
    # 대문자일 때
    if 'A' <= str_input[i] and str_input[i] <= 'Z':
        print(str_input[i].lower(), end='')
    else:
        print(str_input[i].upper(), end='')