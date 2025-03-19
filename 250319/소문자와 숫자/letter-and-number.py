str_input = input()

for i in range(len(str_input)):
    if 'A' <= str_input[i] and str_input[i] <= 'Z':
        # 한 글자씩 소문자로 변환하는 과정 
        print(chr(ord(str_input[i]) - ord('A') + ord('a')), end='')
    elif str_input[i].isdigit() or str_input[i].isalpha():
        print(str_input[i], end='')