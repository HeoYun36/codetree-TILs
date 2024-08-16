n = int(input())

houses = list(map(int, input().split()))

dis_list = []
for i in range(n):
    dis = 0
    for j in range(n):
        if j >= i:
            dis += (j - i) * houses[j]
        else:
            dis += (i - j) * houses[j]
    dis_list.append(dis)

print(min(dis_list))