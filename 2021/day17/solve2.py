ans = 0
for DX in range(150):
    for DY in range(-150, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for t in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            #if 96<=x<=125 and -144<=y<=-98:
            if 150<=x<=193 and -136<=y<=-86:
                ok = True
        if ok:
            if max_y > ans:
                ans = max_y
                print(DX,DY,ans)
print(ans)
