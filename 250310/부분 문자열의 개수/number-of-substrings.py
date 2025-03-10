input_str = input()
target_str = input()

# Please write your code here.
cnt = 0
for i in range(len(input_str) - len(target_str) + 1):
    if input_str[i:i+len(target_str)] == target_str:
        cnt +=1

print(cnt)
