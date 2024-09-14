num_list = list(map(int, input().split()))

# odd num
odd_sum = 0
for i in range(0, len(num_list), 2):
    odd_sum += num_list[i]

# even num
even_sum = 0
for i in range(1, len(num_list), 2):
    even_sum += num_list[i]

if odd_sum > even_sum:
    print(odd_sum - even_sum)
else:
    print(even_sum - odd_sum)