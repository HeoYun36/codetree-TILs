a, b = map(int, input().split())

# Please write your code here.

def magic_f(a, b):
    cnt = 0
    for num in range(a, b + 1):
        num1 = num % 10
        if num % 2 == 0:
            continue
        elif num1 == 5:
            continue
        elif num % 3 == 0 and num % 9 != 0:
            continue
        else:
            cnt += 1

    return cnt

print(magic_f(a, b))