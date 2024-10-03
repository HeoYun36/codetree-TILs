n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx_list = []
result = "Yes"

for i in range(n2):
    if b[i] in a:
        idx_list.append(a.index(b[i]))

if idx_list == []:
    result = "No"
elif len(idx_list) == 1:
    result = "No"
else:
    for i in range(len(idx_list) - 1):
        if idx_list[i] - idx_list[i + 1] >= 2 or idx_list[i + 1] - idx_list[i] >= 2:
            result = "No"

print(result)