Y, M, D = map(int, input().split())

# Please write your code here.

# 윤년 판별
def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 != 0:
                return False
    else:
        return False
    
    return True

# 해당 년에 월, 일이 존재하는 지 여부
def magic_f1(y, m, d):
    feb_day = 28
    if leap_year(y):
        feb_day = 29

    if m == 2:
        if d > feb_day:
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False
    else:
        if d > 31:
            return False
    
    return True

# 어떤 계절인지 출력
def magic_f2(y, m ,d):
    if magic_f1(y, m, d):
        if m >= 3 and m <= 5:
            print("Spring")
        elif m >= 6 and m <= 8:
            print("Summer")
        elif m >= 9 and m <= 11:
            print("Fall")
        else:
            print("Winter")

    else:
        print(-1)

magic_f2(Y, M, D)
         