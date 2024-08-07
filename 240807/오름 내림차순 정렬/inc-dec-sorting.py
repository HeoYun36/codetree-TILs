n = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(arr)
arr2 = arr1[::-1]

for num in arr1:
    print(num, end=" ")

print()

for num in arr2:
    print(num, end=" ")