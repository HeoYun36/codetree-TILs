n = int(input())

arr = [
    input()
    for _ in range(n)
]

sum_of_len = 0
cnt = 0

for word in arr:
    sum_of_len += len(word)
    if word[0] == 'a':
        cnt += 1

print(sum_of_len, cnt)
    
