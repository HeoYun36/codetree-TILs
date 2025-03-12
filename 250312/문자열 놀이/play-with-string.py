S, Q = input().split()

Q = int(Q)

arr = list(S)

for i in range(Q):
    var1, var2, var3 = input().split()

    if var1 == '1':
        var2 = int(var2)
        var3 = int(var3)

        tmp = arr[var2 - 1]
        arr[var2 -1] = arr[var3 -1]
        arr[var3 - 1] = tmp
        print(''.join(arr))
    elif var1 == '2':
        for j in range(len(arr)):
            if arr[j] == var2:
                arr[j] = var3
        print(''.join(arr))
