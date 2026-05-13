x = 0
y = 0

while y != 2:
    
    if x == 0:
        x = 4
        print(x, y)

    elif y == 3:
        y = 0
        print(x, y)

    else:
        t = min(x, 3 - y)
        x = x - t
        y = y + t
        print(x, y)
