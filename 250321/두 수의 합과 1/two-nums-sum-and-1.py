num1, num2 = map(int, input().split())

num = num1 + num2
cnt = 0

str1 = str(num)
for i in range(len(str1)):
    if str1[i] == '1':
        cnt += 1

print(cnt)

