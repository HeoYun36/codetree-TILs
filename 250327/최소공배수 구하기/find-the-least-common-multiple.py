n, m = map(int, input().split())

# Please write your code here.

def find_divisior(n, m):
    num = 1
    while True:
        if (n * num) % m == 0:
            print(n * num)
            break
        else:
            num += 1

find_divisior(n, m)

