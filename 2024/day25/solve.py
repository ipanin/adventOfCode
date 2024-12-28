# Подбор ключей к замкам.
# Ключи и замки схематично описываются как 5 столбиков высотой от 0 до 5.
import util

def parse(blocks: list[list[str]]) -> tuple[list[list[int]], list[list[int]]]:
    keys = []
    locks = []

    # The locks are schematics that have the top row filled (#) and the bottom row empty (.)
    # the keys have the top row empty and the bottom row filled.
    for block in blocks:
        if block[0] == '#####':
            locks.append(parse_block(block[1:]))
        else:
            keys.append(parse_block(block[:-1]))

    return keys, locks

def parse_block(block: list[str]) -> list[int]:
    h = [0, 0, 0, 0, 0]
    for line in block:
        for i, c in enumerate(line):
            if c == '#':
                h[i] += 1

    return h

def solve1(keys: list[list[int]], locks: list[list[int]]) -> int:
    count = 0
    for k in keys:
        for l in locks:
            if match(k, l):
                count += 1
    return count

def match(k: list[int], l: list[int]) -> bool:
    for i in range(5):
        if k[i] + l[i] > 5:
            return False
    return True

blocks = util.load_str_blocks('input.txt')
keys, locks = parse(blocks)
util.assert_equal(solve1(keys, locks), 3495, "Part 1")

