n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max_num(n, num):
    if n == -1:
        return num
    
    if arr[n - 1] > num:
        num = arr[n - 1]
    
    return max_num(n - 1, num)


num = max_num(n, 0)
print(num)
