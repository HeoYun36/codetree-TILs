n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

result_list = [0, 0, 0, 0]

# 인수분해 함수
def factorization(n):
    factor_list = [0, 0, 0, 0]  # 2, 3, 5 ,7
    if n == 1:
        return factor_list

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            factor_list[0] += 1
        elif n % 3 == 0:
            n = n // 3
            factor_list[1] += 1
        elif n % 5 == 0:
            n = n // 5
            factor_list[2] += 1
        elif n % 7 == 0:
            n = n // 7
            factor_list[3] += 1
    
    return factor_list

for i in range(n):
    factor_list = factorization(arr[i])
    for i in range(4):
        if factor_list[i] > result_list[i]:
            result_list[i] = factor_list[i]

result = (2 ** result_list[0]) * (3 ** result_list[1]) * (5 ** result_list[2]) * (7 ** result_list[3])
print(result)


        
