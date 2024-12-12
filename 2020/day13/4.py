def common(p1, p2, distance):
    #count = 4
    n = 1
    while True:
        a = p1*n+distance
        if a % p2 ==0:
            c = p1*n
            m = a//p2
            print(c, n, m)
            #count -= 1
            #if count == 0:
            break
        n += 1

common(17, 13, 2)
common(17, 19, 3)
common(13, 19, 1)