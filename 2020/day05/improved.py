# AoC 2020. Day 5: Binary Boarding
import util


# BFFFBBFRRR
def decode(s: str) -> int:
    # sbin = s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    sbin = s.translate(str.maketrans('FBLR', '0101'))
    return int(sbin, 2)


def test1(data, expected):
    seats = map(decode, data)
    result = max(seats)
    util.assert_equal(result, expected)


def test2(data, expected):
    seats = map(decode, data)
    hi = max(seats)
    lo = min(seats)
    free_seats = set(range(lo, hi+1)) - set(seats)
    my_seat = free_seats.pop()
    util.assert_equal(my_seat, expected)


util.assert_equal(decode('BFFFBBFRRR'), 567)


print("Part 1.")
data = util.load_str_lines_list('input.txt')
test1(data, 874)

print("Part 2.")
test2(data, 594)
