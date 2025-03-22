str_A = input()
str_B = input()

cnt = 0
for i in range(len(str_A)):
    str_A = str_A[-1] + str_A[0: len(str_A) - 1]
    cnt +=1

    if str_A == str_B:
        break

if cnt == 6:
    print(-1)
else:
    print(cnt)
