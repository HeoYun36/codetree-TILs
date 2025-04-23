N = int(input())

# Please write your code here.

def magic_f(n):
    if n % 2 == 0:
        if n == 2:
            return 2
    else:
        if n == 1:
            return 1
    
    return n + magic_f(n - 2)

print(magic_f(N))