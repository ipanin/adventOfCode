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

DIRS = {'e': 1, 'w': -1, 'nw': 1j, 'se': -1j, 'ne': 1+1j, 'sw': -1-1j}
# Map hexagonal grid to square grid:
#
#              (0,1)   (1,1)
#                |     /
#               nw   ne
#                |  /
#     (-1,0)-w-(0,0)-e-(1,0)
#             /  |
#           sw  se
#          /     |
#     (-1,-1)  (0,-1)
#
def init(fname) -> set:
    data = util.load_str_lines(fname)
    blacks = set() # black coords
    for line in data:
        pos = sum(DIRS[d] for d in split(line))
        if pos in blacks:
            blacks.remove(pos)
        else:
            blacks.add(pos)
    
    return blacks


def black_near(center, blacks: set) -> int:
    res = 0
    for delta in DIRS.values():
        if center+delta in blacks:
            res += 1
            if res > 2:
                break  # optimization
    return res


def transform_tile(pos, blacks: set) -> bool:
    is_black = pos in blacks
    #black_neighbors = sum(pos+delta in blacks for delta in DIRS.values()) # two times slower
    black_neighbors = black_near(pos, blacks)
    if is_black and (black_neighbors == 0 or black_neighbors > 2):
        return False # white
    if not is_black and black_neighbors == 2:
        return True # black
    return is_black


def transform(blacks):
    possible = set(blacks)
    possible |= set(p+d for d in DIRS.values() for p in blacks)

    nxt = set()
    for pos in possible:
        if transform_tile(pos, blacks):
            nxt.add(pos)  # save info only about black

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
