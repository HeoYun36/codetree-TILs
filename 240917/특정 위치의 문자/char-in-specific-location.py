string_list = ["L", "E", "B", "R", "O", "S"]

s = input()

idx = -1

for i, char in enumerate(string_list):
    if char == s:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)