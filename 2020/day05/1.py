# AoC 2020. Day 5: Binary Boarding
import util


# BFFFBBFRRR
def decode(s: str) -> int:
    result = 0
    bit = 1
    for c in reversed(s):
        if c in ['B', 'R']:
            result += bit
        bit *= 2
    return result


def test1(data, expected):
    seats = [decode(s) for s in data]
    result = max(seats)
    util.assert_equal(result, expected)


def test2(data, expected):
    seats = [decode(s) for s in data]
    hi = max(seats)
    lo = min(seats)
    free_seats = set(range(lo, hi+1)) - set(seats)
    my_seat = free_seats.pop()
    util.assert_equal(my_seat, expected)


util.assert_equal(decode('BFFFBBFRRR'), 567)

data = util.load_str_lines_list('input.txt')

print("Part 1.")
test1(data, 874)

print("Part 2.")
test2(data, 594)
