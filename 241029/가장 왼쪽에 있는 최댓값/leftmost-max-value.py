import sys

n = int(input())
nums = list(map(int, input().split()))
idx = 1

# 만약 idx가 0이면 종료
while(idx != 0):
    max_num = -sys.maxsize
    
    #1. 우선 최댓값 찾기
    for i in range(len(nums)):
        if max_num < nums[i]:
            max_num = nums[i] 

    #2. 그 최댓값의 idx 찾아서 저장하고 출력
    for i in range(len(nums)):
        if max_num == nums[i]:
            idx = i
            break

    print(idx + 1, end=" ")

    #3. 그 0부터 idx전까지를 리스트로 만들기
    nums = nums[:idx]