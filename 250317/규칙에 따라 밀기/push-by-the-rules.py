a = input()
insts = list(input())

for i in range(len(insts)):
    if insts[i] == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:len(a) - 1]

print(a)
