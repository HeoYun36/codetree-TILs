import sys

# n개의 정수를 입력 받음
n = int(input())
n_list = list(map(int, input().split()))

max_num = -sys.maxsize
result_list = []

# 큰 수를 찾고 그 큰 수를 리스트에서 빼서 다른 리스트에 추가
for i in range(len(n_list)):
    for i in range(len(n_list)):
        if max_num < n_list[i]:
            max_num = n_list[i]
    n_list.remove(max_num)
    result_list.append(max_num)
    max_num = -sys.maxsize
# 그 리스트의 첫번째, 두번째 원소 출력
print(result_list[0], result_list[1])