# 반복문으로 2번 반복해서 4열을 입력받아 2행 4열을 입력받음
arr = [list(map(int, input().split()) )for _ in range(2)]

# 행 평균(2번)
for i in range(2):
    sum_of_row = 0
    for j in range(4):
        sum_of_row += arr[i][j]
    print(f"{sum_of_row / 4:.1f}", end=' ')

print()

# 열 평균(4번)
for j in range(4):
    sum_of_col = 0
    for i in range(2):
        sum_of_col += arr[i][j]
    print(f"{sum_of_col / 2:.1f}", end=' ')

print()

# 전체 평균
sum_of_all = 0
for i in range(2):
    for j in range(4):
        sum_of_all += arr[i][j]
print(f"{sum_of_all / 8:.1f}")
