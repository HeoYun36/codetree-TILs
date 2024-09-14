num_list = list(map(int, input().split()))

index = 0

for i in range(len(num_list)):
    if num_list[i] % 3 == 0:
        index = i - 1
        break

print(num_list[index])