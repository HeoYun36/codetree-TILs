a, b = map(int, input().split())

# Please write your code here.
def f_a(num):
    arr = list(str(num))
    for i in range(len(arr)):
        if arr[i] == 3 or arr[i] == 6 or arr[i] == 9:
            return True

f_a(23)
    

# def f_b(num):
#     return num % 3 == 0

# def is_magic_number(n):
#     return f_a(n) or f_b(n)
        
# cnt = 0
# for i in range(a, b + 1):
#     if is_magic_number(i):
#         print(i)
#         cnt += 1

# print(cnt)


