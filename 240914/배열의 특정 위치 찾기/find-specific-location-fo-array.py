num_list = list(map(int, input().split()))

even_sum = 0
sum_val = 0

for i in range(1, len(num_list), 2):
    even_sum += num_list[i]

for i in range(2, len(num_list), 3):
    sum_val += num_list[i]

avg = sum_val / 3
print(f"{even_sum} {avg:.1f}")