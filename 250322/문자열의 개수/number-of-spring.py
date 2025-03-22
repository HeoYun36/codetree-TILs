arr = []

while True:
    str_input = input()
    arr.append(str_input)

    if str_input == '0':
        break

print(len(arr) - 1)

for i in range(0, len(arr) - 1, 2):
    print(arr[i])

