for _ in range(5):
    arr = list(input().split())
    for i in range(3):
        arr[i] = arr[i].upper()
        print(arr[i], end=" ")
    print()