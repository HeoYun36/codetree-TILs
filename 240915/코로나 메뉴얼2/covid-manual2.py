cnt_arr = [0] * 4

for i in range(3):
    symtom, temp = input().split()
    temp = int(temp)
    if symtom == "Y":
        if temp >= 37:
            cnt_arr[0] += 1
        else:
            cnt_arr[2] += 1
    else:
        if temp >= 37:
            cnt_arr[1] += 1
        else:
            cnt_arr[3] += 1

for i in range(4):
    print(cnt_arr[i], end=" ")

if cnt_arr[0] >= 2:
    print("E")