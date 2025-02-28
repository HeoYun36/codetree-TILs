str1, str2 = input().split()

if len(str1) > len(str2):
    print(str1, len(str2))
elif len(str2) > len(str1):
    print(str2, len(str2))
else:
    print("same")