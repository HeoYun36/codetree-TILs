n = int(input())

# [현재 색깔, 흰 cnt, 검정 cnt]
slot = [['', 0, 0] for _ in range(199999)]

state = 99999

for _ in range(n):
    x, d = input().split()
    x = int(x)

    # 왼쪽
    if d == 'L':
        for i in range(state - x + 1, state + 1):
            if slot[i][0] != 'g':
                slot[i][1] += 1
                slot[i][0] = "w"
                if slot[i][1] >= 2 and slot[i][2] >= 2:
                    slot[i][0] = 'g'
                    
        state -= (x - 1)
    # 오른쪽
    else:
        for i in range(state, state + x):
            if slot[i][0] != 'g':
                slot[i][2] += 1
                slot[i][0] = "b"
                if slot[i][1] >= 2 and slot[i][2] >= 2:
                    slot[i][0] = 'g'

        state += (x - 1)

white = 0
black = 0
gray = 0

for i in range(len(slot)):
    if slot[i][0] == 'w':
        white += 1
    elif slot[i][0] == 'b':
        black += 1
    elif slot[i][0] == 'g':
        gray += 1

print(white, black, gray)