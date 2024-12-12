# AoC 2020. Day 24: Lobby Layout
# 6-angle tiles layout
# C:\soft\pypy3.7-v7.3.3-win32\pypy3.exe 2.py
# see also https://www.redblobgames.com/grids/hexagons/
import util


def split(line) -> list:
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

def init(fname) -> set:
    data = util.load_str_lines(fname)
    blacks = set() # black coords
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

        pos = (x+z, y+z)  # since 1x + 1y = 1z

        if pos in blacks:
            blacks.remove(pos)
        else:
            blacks.add(pos)
    
    return blacks


NEAR = [(-1, 0), (1, 0), (0, -1), (0, 1),  (1, 1),  (-1, -1)]

def black_near(center, blacks: set) -> int:
    res = 0
    for delta in NEAR:
        x = center[0] + delta[0]
        y = center[1] + delta[1]
        if (x, y) in blacks:
            res += 1
            if res > 2:
                break # optimization
    return res


def transform_tile(pos, black: bool, blacks: set) -> bool:
    b = black_near(pos, blacks)
    if black and (b == 0 or b > 2):  # black
        return False # white
    if not black and b == 2:  # white
        return True # black
    return black


def transform(blacks):
    nxt = set()
    for pos in blacks:
        if transform_tile(pos, True, blacks):
            nxt.add(pos)  # save info only about black

        for delta in NEAR:
            npos = (pos[0] + delta[0], pos[1] + delta[1])
            black = npos in blacks
            if transform_tile(npos, black, blacks):
                nxt.add(npos)  # save info only about black
    return nxt


def solve2(blacks, days: int) -> int:
    for d in range(days):
        blacks = transform(blacks)

    return len(blacks)


DAYS = 100
print('Test part 1.', end=' ')
blacks = init('input1.txt')
util.assert_equal(len(blacks), 10) # num of black

print('Test part 2.', end=' ')
util.assert_equal(solve2(blacks, DAYS), 2208)

print('Part 1.', end=' ')
blacks = init('input.txt')
util.assert_equal(len(blacks), 228)  # num of black

print('Part 2.', end=' ')
util.assert_equal(solve2(blacks, DAYS), 3672)
