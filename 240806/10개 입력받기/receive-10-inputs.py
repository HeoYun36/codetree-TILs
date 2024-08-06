nums = list(map(int, input().split()))

sum_of_nums = 0
n = 0
for num in nums:
    if num == 0:
        break
    else:
        sum_of_nums +=num
        n += 1

avg = sum_of_nums / n

print(f'{sum_of_nums} {avg:.1f}')