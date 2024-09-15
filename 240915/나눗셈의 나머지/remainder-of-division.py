arr = [0] * 10

a, b = map(int, input().split())


while a > 1:
    arr[a % b] += 1
    a //= b

val_sum = 0
for i in range(10):
    val_sum += arr[i] ** 2

print(val_sum)