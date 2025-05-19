n = int(input())

slot = [0] * 200001
state = 100000

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(state - x + 1, state + 1):
            slot[i] = 1
        
        state -= (x + 1)
    else:
        for i in range(state, state + x):
            slot[i] = -1
        
        state += (x - 1)

white = 0
black = 0

for i in range(len(slot)):
    if slot[i] == 1:
        white += 1
    elif slot[i] == -1:
        black += 1

print(white, black)

