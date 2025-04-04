a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    return int(x / y)

def cal(a, o, c):
    if o == '+':
        return add(a, c)
    elif o == '-':
        return minus(a, c)
    elif o == '*':
        return multiple(a, c)
    elif o == '/':
        return divide(a, c)


if cal(a, o, c):
    print(f"{a} {o} {c} = {cal(a, o, c)}")
else:
    print("False")