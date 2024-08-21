symtom = 0
temp = 1
cnt = 0

patients = [input().split() for _ in range(3)]

for patient in patients:
    if patient[symtom] == 'Y' and int(patient[temp]) >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')