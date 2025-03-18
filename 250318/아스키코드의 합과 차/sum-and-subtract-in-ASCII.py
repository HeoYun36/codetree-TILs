str1, str2 = input().split()

result1 = ord(str1) + ord(str2)
result2 = ord(str1) - ord(str2) if ord(str1) >= ord(str2) else ord(str2) - ord(str1)
print(result1, result2)