str_input = input()

result = ""
letter = str_input[0]
result += letter
cnt = 1

if len(str_input) == 1:
    result = str_input + '1'
else:
    for i in range(1, len(str_input)):
        if str_input[i] != letter:
            result += str(cnt)
            letter = str_input[i]
            result += letter
            cnt = 1
        else:
            cnt += 1
            if i == len(str_input) - 1:
                result += str(cnt)

print(len(result))
print(result)

