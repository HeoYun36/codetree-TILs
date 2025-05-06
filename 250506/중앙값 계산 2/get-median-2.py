n = int(input())
arr1 = list(map(int, input().split()))


for i in range(n):
    arr2 = []
    # 홀수 번째 원소일 때
    if i % 2 == 0:
        for j in range(i + 1):
            arr2.append(arr1[j])
        arr2.sort()
        print(arr2[len(arr2) // 2], end=' ')
        
