# AoC 2020. Day 20. Jurassic Jigsaw
# Собираем фотографию из фрагментов.

import util
from collections import namedtuple
from collections import Counter

Tile = namedtuple('Tile', ['id', 'bitmap', 'borders', 'x', 'y'])

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
    for i,line in enumerate(block[1:]):
        bin = line.translate(trans)
        left.append(bin[0])
        right.append(bin[9])
        bitmap.append(bin)
    borders = [list2int(right), int(bitmap[9], 2), list2int(left), int(bitmap[0], 2)]
    return Tile(id, bitmap, borders)


def count_match(tile, borders):
    n_match = 0
    for border in tile.borders:
        if borders[border] > 1:
            n_match += 1
    return n_match


# (3371, [550, 312, 626, 797], ['1100011101',
def solve1(tiles):
    borders = [0] * 1024

    for tile in tiles:
        for border in tile.borders:
            borders[border] += 1
            borders[inverted(border)] += 1

    cnt = Counter(borders)
    if len(cnt) != 3:
        raise RuntimeError(f"invalid assumptions", cnt)

    result = 1
    count = 0
    for tile in tiles:
        n_match = count_match(tile, borders)
        if n_match == 2:
            result *= tile.id
            #print(f"Angle tile id={tile.id}")
            count += 1
        elif n_match < 2 or n_match > 4:
            raise RuntimeError(f"Tile id={tile.id} has n_match={n_match}, expected 2..4")

    if count != 4:
        raise RuntimeError(f"Found {count} angle tiles, expected 4")
    return result

def match(tile1, tile2):
    if tile1.borders[RIGHT] == tile2.borders[LEFT]:
        return True, 1, 0
    if tile1.borders[LEFT] == tile2.borders[RIGHT]:
        return True, -1, 0
    if tile1.borders[TOP] == tile2.borders[BOTTOM]:
        return True, 0, -1
    if tile1.borders[BOTTOM] == tile2.borders[TOP]:
        return True, 0, 1
    return False, 0, 0


def extract_angle_tile(unsorted):
    pass


def restore_picture(tiles):
    unsorted = list(tiles)
    arranged = []
    tile1 = extract_angle_tile(unsorted)
    tile1.x = tile1.y = 0
    arranged[0] = tile1
    for pos in range(1, len(tiles)):
        for i, tile in enumerate(unsorted):
            if match(arranged[pos-1], tile):
                rotate(tile)
                arranged.append(tile)
                tile.x = pos % 14
                tile.y = pos // 14
                break
        unsorted.remove(arranged[pos])

    # Fill matrix with pixels
    matrix = {}
    for tile in arranged:
        for i, line in enumerate(tile.bitmap):
            matrix[tile.y+i][tile.x:tile.x +len(line)] = line
    return arranged


"""
01234567890123456789
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
Pattern = [(0, 18), (1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16),
           (1, 17), (1, 18), (1, 19)]


def match_pattern(pict, x, y):
    sizeX = len(pict[0])
    sizeY = len(pict)

    for dy, dx in Pattern:
        if x + dx >= sizeX or y + dx >= sizeY or pict[y + dy][x + dx] == 0:
            return False
    return True

def subtract_pattern(pict, x, y):
    for dy, dx in Pattern:
        pict[y + dy][x + dx] = 0

def remove_monsters(pict):
    pict2 = pict.copy()
    sizeX = len(pict[0])
    sizeY = len(pict)

    for y in range(sizeY):
        for x in range(sizeX):
            if match_pattern(pict, x, y):
                subtract_pattern(pict2, x, y)

    return pict2


def solve2(tiles):
    pict = restore_picture(tiles)
    pict2 = remove_monsters(pict)
    return sum(pict2)


def test(filename, expected1, expected2):
    data = util.load_str_blocks(filename)
    print(filename, "loaded")

    tiles = list(map(parse_block, data))
    result = solve1(tiles)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

test("input_sample.txt", 20899048083289, 273)
test("input.txt", 59187348943703, 0)

