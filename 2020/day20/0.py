# AoC 2020. Day 20. Jurassic Jigsaw
# Собираем фотографию из фрагментов.

import util
from collections import namedtuple

Tile = namedtuple('Tile', ['id', 'bitmap', 'borders'])

def inverted(bin: int) -> int:
    return int('{:010b}'.format(bin)[::-1], 2)

def list2int(lst: list) -> int:
    return int("".join(lst), 2)

# Tile 3371:
# ##...###.#
# ........#.
# ..#.#...#.
# ##..#.....
# ##.......#
# ##........
# ...#......
# .........#
# #.#......#
# .#..###...
RIGHT = 0
BOTTOM = 1
LEFT = 2
TOP = 3
def parse_block(block) -> Tile:
    id = int(util.findall_ints(block[0])[0])
    bitmap = []
    left = []
    right = []
    trans = str.maketrans(".#", "01")
    for line in block[1:]:
        bin = line.translate(trans)
        left.append(bin[0])
        right.append(bin[9])
        bitmap.append(bin)
    borders = [list2int(right), int(bitmap[9], 2), list2int(left), int(bitmap[0], 2)]
    return Tile(id, bitmap, borders)


def match(tile1, tile2):
    if tile1.borders[RIGHT] == tile2.borders[LEFT]:
        return True, 1, 0
    if tile1.borders[LEFT] == tile2.borders[RIGHT]:
        return True, -1, 0
    if tile1.borders[TOP] == tile2.borders[BUTTOM]:
        return True, 0, -1
    if tile1.borders[BOTTOM] == tile2.borders[TOP]:
        return True, 0, 1
    return False, 0, 0

def restore_picture(tiles):
    unsorted = list(tiles)
    sorted = {}
    x = y = 0
    sorted[(x, y)] = unsorted.pop()
    while len(unsorted):
        for i, tile in enumerate(unsorted):
            res, dx, dy = match(sorted[(x, y)], tile)
            if res:
                x += dx
                y += dy
                sorted[(x,y)] = unsorted.pop(i)
                break


# (3371, [550, 312, 626, 797], ['1100011101',
def solve(tiles):
    pict = restore_picture(tiles)
    return pict[0][0].id * pict[-1][0].id * pict[-1][0].id * pict[-1][-1].id


data = util.load_str_blocks('input.txt')
tiles = map(parse_block, data)
result = solve(tiles)
print("Part 1.", result)
#util.assert_equal(result, 0)


