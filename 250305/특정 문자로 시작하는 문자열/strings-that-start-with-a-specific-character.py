n = int(input())

word_arr = [
    input()
    for _ in range(n)
]

letter = input()

idx_arr = []

sum_of_len = 0

for i in range(0, len(word_arr)):
    if word_arr[i][0] == letter:
        idx_arr.append(i)

for i in idx_arr:
    sum_of_len += len(word_arr[i])

avg = sum_of_len / len(idx_arr)

print(len(idx_arr), f"{avg:.2f}")
        


