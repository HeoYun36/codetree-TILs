# n, q 입력
n, q = map(int, input().split())

# 원소들 입력
n_list = list(map(int, input().split()))

# q번 걸쳐서 질의 입력
for _ in range(q):
    q_num = list(map(int, input().split()))
    # 1 a
    if q_num[0] == 1:
        print(n_list[q_num[1] - 1])
    # 2 b
    elif q_num[0] == 2:
        idx = 0
        for i in range(n):
            if n_list[i] == q_num[1]:
                idx = i
                break
        if idx == 0:
            print(0)
        else:
            print(idx + 1)
    # 3 s e
    elif q_num[0] == 3:
        for i in range(q_num[1] - 1, q_num[2]):
            print(n_list[i], end=" ")
        print()