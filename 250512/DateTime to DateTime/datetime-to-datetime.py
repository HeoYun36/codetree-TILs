a, b, c = map(int ,input().split())


result = (24 * 60 * a + 60 * b + c) - (24 * 60 * 11 + 60 * 11 + 11)

if result < 0:
    print(-1)
else:
    print(result)