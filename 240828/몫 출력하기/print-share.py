cnt = 0

while True:
    num = int(input())

    if num % 2 == 0:
        print(num // 2)
        cnt += 1
        if cnt >= 3:
            break