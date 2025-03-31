y = int(input())

# Please write your code here.

def leap_year(year):
    if year % 4 != 0:
        return False
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    
    return True
    
if leap_year(y):
    print("true")
else:
    print("false")    