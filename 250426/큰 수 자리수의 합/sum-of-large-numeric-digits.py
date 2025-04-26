a, b, c = map(int, input().split())

def magic_f(num):
    if num // 10 == 0:
        return num

    return magic_f(num // 10) + num % 10

num = a * b * c

print(magic_f(num))