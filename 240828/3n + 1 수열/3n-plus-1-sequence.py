n = int(input())

cnt = 0

while True:
    if n == 1:
        break
        
    cnt += 1

    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

print(cnt)