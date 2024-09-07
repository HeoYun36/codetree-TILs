a, b = map(int, input().split())

even_list = [num for num in range(b, a - 1, -1) if num % 2 == 0]

for i in range(1, 10):
    for j in range(len(even_list)):
        print(f"{even_list[j]} * {i} = {even_list[j] * i}", end="")
        if j < len(even_list) - 1:
            print(" / ", end="")
    print()