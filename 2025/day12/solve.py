#from functools import cache
import util

def solve1(net) -> int:
    return 1

def load(fname):
    # aaa: you hhh
    lines = util.load_str_lines(fname)
    net = {}
    for  line in lines:
        source, dest = line.split(':')
        net[source] = dest.split()

    return net

sample_data = load('sample1.txt')
util.assert_equal(solve1(sample_data), 0, "Part 1 Sample")

data = load('input.txt')
#util.assert_equal(solve1(data), 0, "Part 1")
