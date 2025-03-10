input_str = input()
target_str = input()

# Please write your code here.

idx = -1
for i in range(len(input_str) - len(target_str) + 1):
    if input_str[i:i+len(target_str)] == target_str:
        idx = i
        break

print(idx)