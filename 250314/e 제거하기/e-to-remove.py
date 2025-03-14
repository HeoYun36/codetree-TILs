str_input = input()


idx = -1
for i in range(len(str_input)):
    if str_input[i] == 'e':
        idx = i
        break

arr = list(str_input)

arr.pop(idx)

print(''.join(arr))