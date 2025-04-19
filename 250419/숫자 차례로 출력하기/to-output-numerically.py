n = int(input())

# Please write your code here.

def magic_f1(n):
    if n == 0:
        return

    magic_f1(n - 1)
    print(n, end=' ')

def magic_f2(n):
    if n == 0:
        return

    print(n, end=' ')
    magic_f2(n - 1)

magic_f1(n)
print()
magic_f2(n)