#
from functools import cache
import util

def solve1(data) -> int:
    curr_x = data[0].find('S')
    beams = set([curr_x])
    result = 0

    for line in data[1:]:
        beams_new = set()
        for x in beams:
            if line[x] == '^':
                result += 1
                beams_new.add(x-1)
                beams_new.add(x+1)
            else:
                beams_new.add(x)
        beams = beams_new
    return result

def solve2(data) -> int:
    t = tree(data)
    x = data[0].find('S')
    return t.count_ways(x, 1)

class tree():
    def __init__(self, data):
        self.data = data

    @cache
    def count_ways(self, x, y):
        if y == len(self.data):
            return 1
        if self.data[y][x] == '^':
            return self.count_ways(x-1, y+1) + self.count_ways(x+1, y+1)
        else:
            return self.count_ways(x, y+1)

sample_data = util.load_str_lines('sample.txt')
util.assert_equal(solve1(sample_data), 21, "Part 1 Sample")
util.assert_equal(solve2(sample_data), 40, "Part 2 Sample")

data = util.load_str_lines('input.txt')
util.assert_equal(solve1(data), 1573, "Part 1")
util.assert_equal(solve2(data), 15093663987272, "Part 2")
