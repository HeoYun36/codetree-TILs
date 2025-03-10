str_input, o = input().split()

idx = -1
for i in range(len(str_input)):
    if o == str_input[i]:
        idx = i
        break

if idx == -1:
    print("No")
else:
    print(idx)
        

    