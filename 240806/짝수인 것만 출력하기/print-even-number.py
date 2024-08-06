n = int(input())
nums = list(map(int, input().split()))

even_list = []
for num in nums:
    if num % 2 == 0:
        even_list.append(num)

for num in even_list:
    print(num, end=" ")