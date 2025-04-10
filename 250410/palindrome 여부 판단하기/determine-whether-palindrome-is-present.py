A = input()

# Please write your code here.

def palindrome(string):
    if string == string[-1::-1]:
        return "Yes"
    else:
        return "No"

print(palindrome(A))