numbers1 = list(map(int, input().split()))

numbers2 = []
for num in numbers1:
    if num >= 250:
        break
    else:
        numbers2.append(num)

sum_of_numbers2 = 0
for num in numbers2:
    sum_of_numbers2 += num

avg = sum_of_numbers2 / len(numbers2)

print(f'{sum_of_numbers2} {avg}')