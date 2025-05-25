n, m = map(int, input().split())

a = [0 for _ in range(1000001)]
b = [0 for _ in range(1000001)]

# A
idx = 0
state = 0

for _ in range(n):
    d, t = input().split()
    t = int(t)

    # 방향 설정
    move = 0

    if d == 'R':
        move = 1
    else:
        move = -1

    # 주어진 시간만큼 이동하면서 리스트에 위치 기록
    while t != 0:
        idx += 1
        state += move
        a[idx] = state

        t -= 1

# B
idx = 0
state = 0

for _ in range(m):
    d, t = input().split()
    t = int(t)

    # 방향 설정
    move = 0

    if d == 'R':
        move = 1
    else:
        move = -1

    # 주어진 시간만큼 이동하면서 리스트에 위치 기록
    while t != 0:
        idx += 1
        state += move
        b[idx] = state

        t -= 1

sec = -1
# 몇 초 뒤에 만나는지 확인
for i in range(1, 1000001):
    if a[i] == b[i]:
        sec = i
        break

print(sec)



