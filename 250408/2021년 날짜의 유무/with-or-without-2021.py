M, D = map(int, input().split())

# Please write your code here.

def magic_f(m, d):
    if m > 12:
        return "No"
    elif m == 2:
        if d < 1 or d > 28:
            return "No"
    elif m % 2 == 0:
        if d < 1 or d > 30:
            return "No"
    elif m % 2 != 0:
        if d < 1 or d > 31:
            return "No"
    
    return "Yes"

print(magic_f(M, D))
