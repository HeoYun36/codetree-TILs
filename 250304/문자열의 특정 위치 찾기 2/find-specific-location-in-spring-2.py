letter = input()

word_list = ["apple", "banana", "grape", "blueberry", "orange"]

num = 0
for word in word_list:
    if word[2] == letter or word[3] == letter:
        print(word)
        num+=1

print(num)

 