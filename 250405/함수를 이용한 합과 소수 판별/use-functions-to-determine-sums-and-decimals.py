a, b = map(int, input().split())

# Please write your code here.

def prime(num):
    cnt = 0
    for i in range(1, num):
        if num % i == 0:
            cnt += 1

    if cnt >= 2:
        return False
    else:
        return True

def even(num):
    sum_of_num = 0
    while True:
        sum_of_num += num % 10
        num = num // 10
        if num == 0:
            break

    if sum_of_num % 2 == 0:
        return True
    else:
        return False

def magic_f(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if prime(i) and even(i):
            cnt +=1
    
    return cnt

print(magic_f(a, b))
