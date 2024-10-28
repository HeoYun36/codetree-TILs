import sys

n = int(input())
n_list = list(map(int, input().split()))
max_num = -sys.maxsize
find = False

while(len(n_list)):
    cnt = 0
    # 1. 우선 최댓값을 찾는다.
    for i in range(len(n_list)):
        if max_num < n_list[i]:
            max_num = n_list[i];

    # 2. 그 최댓값이 중복되는지 확인
    for i in range(len(n_list)):
        if max_num == n_list[i]:
            cnt += 1
    
    # 3. 만약 최댓값이 중복되면 중복되는 위치의 값들을 초기화
    if cnt > 1:
        for i in range(len(n_list)):
            if max_num == n_list[i]:
                n_list[i] = -sys.maxsize
        # 최대값 초기화
        max_num = -sys.maxsize
        cnt = 0
    else:
        break

if max_num == -sys.maxsize:
    print(-1)
else:
    print(max_num)