# День 1. Подсчет калорий
# Поиск максимального значения
# В части 2 - поиск 3х наибольших.
import util


def test(filename, expected1, expected2):
    data = load(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)


def solve1(data):
    return max(data)


def solve2(data):
    return sum(sorted(data)[-3:])


def load(fname):
    blocks = util.load_str_blocks(fname)
    return [sum([int(line) for line in b]) for b in blocks]


test("input.txt", 69206, 197400)