n = int(input())
nums = list(map(int, input().split()))

# 최댓값 찾기
max_num = -1

for i in range(n):
    #최대가 될 수 있는 후보
    if max_num < nums[i]:
        # 각각의 숫자를 조사함
        cnt = 0
        for j in range(n):
            if nums[j] == nums[i]:
                cnt += 1

        # 이 숫자가 배열에서 유일할때만 갱신
        if cnt == 1:
            max_num = nums[i]

print(max_num)