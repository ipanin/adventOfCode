# AoC 2020. Day 6
import util
import os


def load_list_of_set(fname):
    folder = os.path.dirname(os.path.realpath(__file__))
    fname = os.path.join(folder, fname)
    result = []

    with open(fname, 'rt') as f:
        block_begin = True
        block = set()
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                if block_begin:
                    block = set(list(x))
                    block_begin = False
                else:
                    # block = block.union(list(x)) # part 1
                    block = block.intersection(list(x))
            else:  # empty line => block ended
                result.append(block)
                block_begin = True

        if not block_begin:
            result.append(block)
    return result


def test(data, expected):
    result = 0
    result = sum(map(len, data))
    util.assert_equal(result, expected)


print("Part 2.")
data = load_list_of_set('input.txt')
test(data, 0)
