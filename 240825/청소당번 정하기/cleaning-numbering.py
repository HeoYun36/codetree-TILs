n = int(input())

classroom_cnt = 0
hall_cnt = 0
restroom_cnt = 0

for n in range(1, n + 1):
    if n % 12 == 0:
        restroom_cnt += 1
    elif n % 3 == 0:
        hall_cnt += 1
    elif n % 2 == 0:
        classroom_cnt += 1

print(classroom_cnt, hall_cnt, restroom_cnt)