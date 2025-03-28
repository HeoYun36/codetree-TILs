n = int(input())

# Please write your code here.
def magic_f(n):
    sum_of_num = n // 10 + n % 10 
    return n % 2 == 0 and sum_of_num % 5 == 0

if magic_f:
    print("Yes")
else:
    print("No")