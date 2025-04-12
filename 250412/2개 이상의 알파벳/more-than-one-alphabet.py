A = input()

# Please write your code here.
def magic_f(string):
    cnt = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            cnt += 1
    
    return cnt >= 2

if magic_f(A):
    print("Yes")
else:
    print("No")
