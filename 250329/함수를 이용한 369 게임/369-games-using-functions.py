a, b = map(int, input().split())

# Please write your code here.

def f_a(num):
    return (num // 10) % 3 == 0 

def f_b(num):
    return (num % 10) % 3 == 0 and (num % 10) != 0

def f_c(num):
    return num % 3 == 0


cnt = 0
for i in range(a, b + 1):
    if f_a(i) or f_b(i) or f_c(i):
        cnt += 1

print(cnt)


        