N = int(input())

# Please write your code here.
cnt = 0

def f(n):
    global cnt

    if n == 1:
        return

    if n % 2 == 0:
        cnt += 1
        return f(n // 2)
    else:
        cnt += 1
        return f(n // 3)

f(N)

print(cnt)