n, m = map(int, input().split())

a_list = [0]
b_list = [0]

# 단위 시간마다 A 위치 기록
state = 0
for _ in range(n):
    v, t = map(int, input().split())

    while t > 0:
        state += v
        a_list.append(state)
        t -= 1

# 단위 시간마다 B 위치 기록
state = 0
for _ in range(m):
    v, t = map(int, input().split())

    while t > 0:
        state += v
        b_list.append(state)
        t -= 1

head_list = []

for i in range(1, len(a_list)):
    if a_list[i] > b_list[i]:
        head_list.append('A')
    elif a_list[i] < b_list[i]:
        head_list.append('B')
    else:
        head_list.append("AB")

cnt = 1
for i in range(1, len(head_list)):
    if head_list[i - 1] != head_list[i]:
        cnt += 1

print(cnt)
