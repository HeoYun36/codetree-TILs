N = int(input())

# Please write your code here.

def recur_f(n):
    if n == 1:
        return 1
    
    return recur_f(n - 1) + n

print(recur_f(N))