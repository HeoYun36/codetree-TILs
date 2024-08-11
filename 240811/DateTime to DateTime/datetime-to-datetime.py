a, b, c = map(int, input().split())

days = 11
hours = 11
mins = 11

cnt = 0

while True:
    if days == a and hours == b and mins == c:
        print(cnt)   
        break
    elif a == 11 and b == 11 and c < 11:
        print(-1)
        break
    elif a == 11 and b < 11:
        print(-1)
        break
    elif a < 11:
        print(-1)
        break
    else:
        mins += 1
        cnt += 1
        if mins == 60:
            hours += 1
            mins = 0
            if hours == 24:
                days += 1
                hours = 0