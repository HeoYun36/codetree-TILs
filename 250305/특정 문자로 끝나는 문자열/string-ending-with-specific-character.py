word_arr =[
    input()
    for _ in range(10)
]

letter = input()

idx_arr = []

for i in range(10):
    if word_arr[i][len(word_arr[i]) - 1] == letter:
        idx_arr.append(i)

if idx_arr != []:
    for i in idx_arr:
        print(word_arr[i])
else:
    print("None")
