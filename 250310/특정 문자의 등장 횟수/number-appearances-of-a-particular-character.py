str_input = input()

cnt_ee = 0
cnt_eb = 0

for i in range(len(str_input) - 1):
    if str_input[i:i+2] == "ee":
        cnt_ee += 1
    elif str_input[i:i+2] == "eb":
        cnt_eb += 1

print(cnt_ee, cnt_eb)

