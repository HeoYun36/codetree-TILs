str_input = input()

if str_input == 'z':
    print('a')
else:
    result = chr(ord(str_input) + 1)
    print(result)