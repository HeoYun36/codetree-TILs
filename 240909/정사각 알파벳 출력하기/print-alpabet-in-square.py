n = int(input())

cnt = ord("A")
for _ in range(n):
    for _ in range(n):
        print(chr(cnt), end="")
        cnt += 1
    print()