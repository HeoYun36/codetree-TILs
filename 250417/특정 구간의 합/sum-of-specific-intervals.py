n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def magic_f():
    for (a1, a2) in queries:
        sum_of_num = 0
        for i in range(a1 - 1, a2):
            sum_of_num += arr[i]
        print(sum_of_num)

magic_f()

