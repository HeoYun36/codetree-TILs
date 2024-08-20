people_list = [input().split() for _ in range(2)]

age = 0
gender = 1
cnt = 0

for i in range(2):
    if (int(people_list[i][age]) >= 19) and (people_list[i][gender] == 'M'):
       cnt += 1

if cnt >= 1:
    print(1)
else:
    print(0)