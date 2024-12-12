vx = 7
vy = 9
x = y= 0

for t in range(1,27):
    x += vx
    y += vy
    if vx > 0: vx -= 1
    vy -= 1
    target = x in range(20, 30+1) and y in range(-10, -5+1)
    print(t, x,y, target)
