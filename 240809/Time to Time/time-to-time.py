# a, b, c, d = map(int, input().split())

# hour, mins = a, b

# cnt = 0

# while True:
#     if hour == c and mins == d:
#         break

#     mins += 1 
#     cnt += 1

#     if mins == 60:
#         hour += 1
#         mins = 0

# print(cnt)

a, b, c, d = tuple(map(int, input().split()))

print((c * 60 + d) - (a * 60 + b))