import util

Direction = {"L":-1, "D":-1j, "R": 1, "U" : 1j}
lines = util.load_str_lines("input.txt")
hpos = tpos = 0
field = set([tpos])
for line in lines:
    dir, n = line.split()
    dir = Direction[dir]
    n = int(n)
    for _ in range(n):
        hpos += dir
        dist = tpos - hpos
        if abs(dist.real) <= 1 and abs(dist.imag) <= 1:
            continue
        tpos += dir
        if dir == 1 or dir == -1:
            tpos = complex(tpos.real, hpos.imag)
        if dir == 1j or dir == -1j:
            tpos = complex(hpos.real, tpos.imag)
        field.add(tpos)
print("Part1", len(field))  # 5619