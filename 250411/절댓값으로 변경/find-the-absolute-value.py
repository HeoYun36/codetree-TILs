n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def magic_f(arr):
    for i in range(len(arr)):
        if arr[i] < 0 :
            arr[i] = -arr[i]

magic_f(arr)

for i in range(len(arr)):
    print(arr[i], end=' ')