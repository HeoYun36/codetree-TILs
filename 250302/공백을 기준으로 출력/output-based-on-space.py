str_input1 = input()
str_input2 = input()

answer = ""
for word in str_input1.split():
    answer += word

for word in str_input2.split():
    answer += word

print(answer)