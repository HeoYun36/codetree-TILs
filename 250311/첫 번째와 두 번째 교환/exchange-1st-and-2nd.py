str_input = input()

first_letter = str_input[0]
second_letter = str_input[1]

arr = list(str_input)

for i in range(len(arr)):
    if arr[i] == first_letter:
        arr[i] = second_letter
    elif arr[i] == second_letter:
        arr[i] = first_letter

print(''.join(arr))

