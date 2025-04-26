n = int(input())

# Please write your code here.

cnt = 0

def magic_f(n):
    global cnt

    if n == 1:
        return
    
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    
    cnt += 1
    return magic_f(n)

magic_f(n)
print(cnt)