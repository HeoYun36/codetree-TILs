str_input = input()
letter_input = input()

num = 0

for i in range(len(str_input)):
    if letter_input == str_input[i]:
        num += 1

print(num)
