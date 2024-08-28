while True:
    width, height, s = input().split()
    area = int(width) * int(height)
    print(area)

    if s == 'C':
        break