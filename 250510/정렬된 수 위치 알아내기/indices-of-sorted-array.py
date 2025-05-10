n = int(input())
arr1 = list(map(int, input().split()))

arr1 = [(arr1[i], i) for i in range(n)]

arr1.sort(key=lambda x: x[0])

arr2 = [0] * n

for idx, x in enumerate(arr1, start=1):
    arr2[x[1]] = idx

print(*arr2)
