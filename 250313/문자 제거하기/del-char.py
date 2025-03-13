str_input = input()

arr = list(str_input)

for _ in range(len(arr) - 1):
    idx = int(input())
    if idx > len(arr) - 1:
        arr.pop(len(arr) - 1)
    else:
        arr.pop(idx)
    print(''.join(arr))

