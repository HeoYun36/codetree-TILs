text = input()
pattern = input()

# Please write your code here.
def magic_f():
    for i in range(len(text) - len(pattern) + 1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i + j] == pattern[j]:
                cnt += 1 
            else:
                break
        if cnt == len(pattern):
            idx = i
            return idx
    
    return -1

idx = magic_f()

print(idx)