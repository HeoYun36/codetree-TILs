n = int(input())

arr = input().split()

nums = ""

# 리스트 안에 있는 숫자를 모두 합쳐 한줄로 만들기
for i in range(n):
    nums += arr[i]    

# 1자리씩 출력하다 5자리가 되면 다음 줄로 넘어가서 출력하기
for i in range(len(nums)):
    print(nums[i], end='')
    if i % 5 == 4:
        print()
        