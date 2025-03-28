n = int(input())

# Please write your code here.
def magic_f(n):
    sum_of_num = n // 10 + n % 10 
    if n % 2 == 0 and sum_of_num % 5 == 0:
        return "Yes"
    else:
        return "No"

print(magic_f(n))