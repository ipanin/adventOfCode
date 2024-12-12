# AoC 2020. Day 24: Lobby Layout
# 6-angle tiles layout
import util


def split(line):
    res = []
    i = 0
    while i < len(line):
        if line[i] in ['e','w']:
            res.append(line[i])
            i += 1
        else:
            res.append(line[i:i+2])
            i += 2
    
    return res

def solve(fname) -> set:
    data = util.load_str_lines(fname)
    field = dict()
    for line in data:
        # e, se, sw, w, nw, and ne
        # e-w,se-nw,sw-ne
        x = y = z = 0
        dirs = split(line)
        for d in dirs:
            if d == 'e':
                x += 1
            elif d == 'w':
                x -= 1
            elif d == 'nw':
                y += 1
            elif d == 'se':
                y -= 1
            elif d == 'ne':
                z += 1
            elif d == 'sw':
                z -= 1
            else:
                print('unexpected direction', d)

        x += z; y += z; z = 0 # since 1x + 1y = 1z

        tile = field.get((x,y,z), False) # False = white
        field[(x,y,z)] = not tile
    
    return sum(field.values())


print("Test.")
util.assert_equal(solve('input1.txt'), 10)

print("Part 1.")
util.assert_equal(solve('input.txt'), 228)


