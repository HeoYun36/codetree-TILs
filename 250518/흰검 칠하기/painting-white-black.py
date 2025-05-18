n = int(input())

slot = [[0, 0, 0] for _ in range(199999)]

state = 99999

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        for i in range(state, state + x):
            if slot[i][0] != 'g':
                slot[i][1] += 1
                if slot[i][1] == 2 and slot[i][2] == 2:
                    slot[i][0] = 'g'
                else:
                    slot[i][0] = "b"
        state += (x - 1)
    else:
        for i in range(state - x + 1, state + 1):
            if slot[i][0] != 'g':
                slot[i][2] += 1
                if slot[i][1] == 2 and slot[i][2] == 2:
                    slot[i][0] = 'g'
                else:
                    slot[i][0] = "w"

        state -= (x - 1)

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