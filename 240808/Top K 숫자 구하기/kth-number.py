n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = sorted(arr1)
print(arr2[k - 1])