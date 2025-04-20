N = int(input())

# Please write your code here.

def magic_f(n):
    if n == 0:
        return
    
    print(n, end=' ')
    magic_f(n - 1)
    print(n, end=' ')

magic_f(N)