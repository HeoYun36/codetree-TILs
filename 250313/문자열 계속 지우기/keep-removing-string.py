A = input()
B = input()

# Please write your code here.
state = False 

while len(A) >= len(B):
    for i in range(len(A) - len(B) + 1):
        for j in range(len(B)):
            if A[i+j] == B[j]:
                state = True
            else:
                state = False
                break
        
        if state == True:
            A = A[:i] + A[i + len(B):]
            break
    if state == False:
        break

print(A)

