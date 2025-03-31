a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

sum_of_num = 0
for i in range(a, b + 1):
    if is_prime(i):
        sum_of_num += i

print(sum_of_num)
