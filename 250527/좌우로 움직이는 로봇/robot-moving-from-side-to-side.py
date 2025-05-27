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

length = max(len(a_arr), len(b_arr))

cnt = 0
t = 1

while t < length: 
    a_idx = t
    b_idx = t

    if t >= len(a_arr):
        a_idx = len(a_arr) - 1
    
    if t >= len(b_arr):
        b_idx = len(b_arr) - 1

    if (a_arr[a_idx - 1] != b_arr[b_idx - 1]) and (a_arr[a_idx] == b_arr[b_idx]):
        cnt += 1
    
    t += 1

print(cnt)

