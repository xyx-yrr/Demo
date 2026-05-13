def toh(n, s, a, d):

    if n == 1:
        print("Move", n, "from", s, "to", d)
        return

    toh(n-1, s, d, a)

    print("Move", n, "from", s, "to", d)

    toh(n-1, a, s, d)

toh(3, 'A', 'B', 'C')
