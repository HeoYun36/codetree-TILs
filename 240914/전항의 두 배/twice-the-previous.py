a1, a2 = map(int, input().split())

num_list = [a1, a2]

for _ in range(8):
    num_list.append(num_list[-1] + 2 * num_list[-2])

print(*num_list)