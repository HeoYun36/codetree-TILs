people_list = [input().split() for _ in range(2)]

age = 0
gender = 1

for i in range(2):
    if (int(people_list[i][age]) >= 19) and (people_list[i][gender] == 'M'):
        print(1)
        break
    else:
        print(0)