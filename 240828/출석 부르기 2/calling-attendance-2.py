name_list = ["John", "Tom", "Paul", "Sam"]

while True:
    num = int(input())
    if num <= 4:
        print(name_list[num - 1])
    else:
        print("Vacancy")
        break