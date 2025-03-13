str_input = input()

arr = list(str_input)

arr.pop(1)
arr.pop(len(arr) - 2)

result = ''.join(arr)

print(result)