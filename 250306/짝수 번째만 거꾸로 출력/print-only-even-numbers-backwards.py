str_input = input()

result = ""

for i in range(1, len(str_input), +2):
    result += str_input[i]

for letter in result[-1::-1]:
    print(letter, end='')

