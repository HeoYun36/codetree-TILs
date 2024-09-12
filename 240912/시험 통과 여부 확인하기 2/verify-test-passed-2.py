n = int(input())

cnt = 0
for _ in range(n):
    score_list = list(map(int, input().split()))
    sum_score = 0
    for i in range(4):
        sum_score += score_list[i]
    avg_score = sum_score / len(score_list)
    if avg_score >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)