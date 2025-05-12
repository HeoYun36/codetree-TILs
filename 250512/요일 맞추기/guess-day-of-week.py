m1, d1, m2, d2 = map(int, input().split())

# 두 날짜 사이에 일수 구하기
def count_days(m1, d1, m2, d2):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0

    if m1 == m2:
        if d1 == d2:
            result = 0
        else:
            if d1 > d2:
                result = d1 - d2
            else:
                result = d2 - d1
    else:
        if m1 > m2:
            start_m, end_m = m2, m1
            start_d, end_d = d2, d1
        else:
            start_m, end_m = m1, m2
            start_d, end_d = d1, d2
        result += (months[start_m] - start_d)
        for month in range(start_m + 1, end_m):
            result += months[month]
        result += end_d
    
    return result

days_1 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_2 = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]

if m1 < m2:
    print(days_1[count_days(m1, d1, m2, d2) % 7])
elif m1 > m2:
    print(days_2[count_days(m1, d1, m2, d2) % 7])
elif d1 > d2:
    print(days_2[count_days(m1, d1, m2, d2) % 7])
else:
    print(days_1[count_days(m1, d1, m2, d2) % 7])
