n = int(input())
if n >= 80:
    print("pass")
else:
    need_score = 80 - n
    print(f"{need_score} more score")