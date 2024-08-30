# 변수 선언 및 입력
n = int(input())

# 길이가 n인 직각삼각형을 출력합니다.
for i in range(n):
	for _ in range(n-i):
		print("*", end=" ")
	print()