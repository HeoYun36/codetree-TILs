str1, str2 = input().split()

arr1 = list(str1[:2])

arr2 = list(str2)

for i in range(2):
    arr2[i] = arr1[i]

print(''.join(arr2))
