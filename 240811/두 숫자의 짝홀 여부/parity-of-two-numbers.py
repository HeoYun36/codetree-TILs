def num(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
    

a, b = map(int, input().split())

num(a)
num(b)