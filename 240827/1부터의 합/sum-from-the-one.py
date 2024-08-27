n = int(input())

sum_val = 0

for num in range(1, 101):
    sum_val += num

    if sum_val >= n:
        print(num)
        break