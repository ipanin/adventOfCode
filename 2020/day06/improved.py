# AoC 2020. Day 6: Custom Customs
import util


def union_len(block: list) -> int:
    # convert list of strings to list of sets, then find union of all sets
    # finally get len of union
    return len(set.union(*map(set, block)))


def intersect_len(block: list) -> int:
    return len(set.intersection(*map(set, block)))


def test1(fname, expected):
    blocks = util.load_str_blocks(fname)
    result = sum(map(union_len, blocks))
    util.assert_equal(result, expected)


def test2(fname, expected):
    blocks = util.load_str_blocks(fname)
    result = sum(map(intersect_len, blocks))
    util.assert_equal(result, expected)


print("Part 1.")
test1('input0.txt', 11)
test1('input.txt', 6726)

print("Part 2.")
test2('input0.txt', 6)
test2('input.txt', 3316)
