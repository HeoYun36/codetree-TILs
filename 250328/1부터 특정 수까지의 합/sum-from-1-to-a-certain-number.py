n = int(input())

# Please write your code here.
def sum_f(n):
    sum_of_num = 0
    for i in range(1, n + 1):
        sum_of_num += i
    
    result = sum_of_num // 10
    return result

print(sum_f(n))
