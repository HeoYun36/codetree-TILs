n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def magic_f(m):
    sum_of_num = 0
    while m != 0:
        sum_of_num += A[m - 1]

        if m % 2 == 0:
            m = m // 2 
        else:
            m -= 1
        
    
    return sum_of_num

print(magic_f(m))

