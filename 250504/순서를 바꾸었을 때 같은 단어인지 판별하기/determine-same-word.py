word1 = input()
word2 = input()

# Please write your code here.
word1_sort = sorted(word1)
word2_sort = sorted(word2)

word1_str = ''.join(word1_sort)
word2_str = ''.join(word2_sort)

if word1_str != word2_str:
    print("No")
else:
    print("Yes")

