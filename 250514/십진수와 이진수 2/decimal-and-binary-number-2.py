num_list = list(map(int, input()))

num = 0

for i in range(len(num_list)):
    num = num * 2 + num_list[i]

num *= 17

digit = []

while True:
    if num < 2:
        digit.append(num)
        break
    
    digit.append(num % 2)
    num //= 2

for i in digit[::-1]:
    print(i, end='')