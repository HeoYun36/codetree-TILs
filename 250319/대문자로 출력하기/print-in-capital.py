str_input = input()

for i in range(len(str_input)):
    if 'a' <= str_input[i] and str_input[i] <= 'z':
        print(chr(ord(str_input[i]) - ord('a') + ord('A')), end='')
    elif 'A' <= str_input[i] and str_input[i] <= 'Z':
        print(str_input[i], end='')