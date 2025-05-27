n, m = map(int, input().split())

a_arr = []
b_arr = []

def move(arr, k):
    state = 0
    arr.append(state)
    for _ in range(k):
        t, d = input().split()
        t = int(t)

        move = 0
        if d == "R":
            move = 1
        else:
            move = -1

        while t > 0:
            state += move
            arr.append(state)

            t -= 1

move(a_arr, n)
move(b_arr, m)

if len(a_arr) >= len(b_arr):
    length = len(a_arr)
    for _ in range(len(a_arr) - len(b_arr)):
        b_arr.append(b_arr[-1])
else:
    length = len(b_arr)
    for _ in range(len(b_arr) - len(a_arr)):
        a_arr.append(a_arr[-1])

cnt = 0

for i in range(1, length):
    if a_arr[i - 1] != b_arr[i - 1] and a_arr[i] == b_arr[i]:
        cnt += 1

print(cnt)