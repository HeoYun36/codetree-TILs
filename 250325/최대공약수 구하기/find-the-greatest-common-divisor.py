n, m = map(int, input().split())

# Please write your code here.

def find_divisor(n , m):
    min_num = n if n <= m else m
    for i in range(n + 1, 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break

find_divisor(n, m)
            