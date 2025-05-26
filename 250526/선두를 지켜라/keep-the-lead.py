n, m = map(int ,input().split())

a_arr = []
b_arr = []

state = 0
a_arr.append(state)
for _ in range(n):
    v, t = map(int ,input().split())
    while t > 0:
        state += v
        a_arr.append(state)

        t -= 1

state = 0
b_arr.append(state)
for _ in range(m):
    v, t = map(int ,input().split())
    while t > 0:
        state += v
        b_arr.append(state)

        t -= 1

cnt = 0
head_arr = []
for i in range(len(a_arr)):
    if a_arr[i] > b_arr[i]:
        head_arr.append('A')
    elif a_arr[i] < b_arr[i]:
        head_arr.append('B')

for i in range(1, len(head_arr)):
    if head_arr[i] != head_arr[i - 1]:
        cnt += 1

print(cnt)
    

