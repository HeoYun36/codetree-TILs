N = int(input())

# Please write your code here.

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(N))