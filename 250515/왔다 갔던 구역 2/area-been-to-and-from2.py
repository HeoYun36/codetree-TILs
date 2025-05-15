n = int(input())

slot = [0] * 4001
curr_state = 1999

for i in range(n):
    x, d = input().split()
    x = int(x)
    if d == "R":
        while x:
            slot[curr_state] += 1
            curr_state += 1

            x -= 1
    else:
        while x:
            curr_state -= 1
            slot[curr_state] += 1

            x -= 1

length = 0

for i in range(len(slot)):
    if slot[i] >= 2:
        length +=1

print(length)