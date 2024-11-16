arr_2d = [list(map(int, input().split())) for _ in range(4)]
sum_of_arr = 0

for i in range(4):
    for j in range(i + 1):
        sum_of_arr += arr_2d[i][j]
        
print(sum_of_arr)