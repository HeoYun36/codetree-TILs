n, m = map(int, input().split())

a = [0]
b = [0]

def move(arr, d, t, state):
     # 방향 설정
    move_dir = 0

    if d == 'R':
        move_dir = 1
    else:
        move_dir = -1

    # 주어진 시간만큼 이동하면서 리스트에 위치 기록
    while t != 0:
        state += move_dir
        arr.append(state)

        t -= 1
    
    return state

# A
state = 0

for _ in range(n):
    d, t = input().split()
    t = int(t)

    state = move(a, d, t, state)

# B
state = 0

for _ in range(m):
    d, t = input().split()
    t = int(t)

    state = move(b, d, t, state)

sec = -1
length = max(len(a), len(b))

for i in range(1, length):
    if a[i] == b[i]:
        sec = i
        break

print(sec)