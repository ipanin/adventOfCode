# AoC 2020. Day
import os
import util


def load_str_blocks_list(fname):
    folder = os.path.dirname(os.path.realpath(__file__))
    fname = os.path.join(folder, fname)
    result = []

    with open(fname, 'rt') as f:
        # return [int(line.rstrip('\n')) for line in f.readlines()]
        data = dict()
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                pairs = x.split(' ')
                for p in pairs:
                    k, v = p.split(':')
                    if len(v) == 0:
                        continue
                    data[k] = v
            elif len(data.keys()) > 0:
                result.append(data)
                data = dict()

    return result



def test1(data, expected):
    result = 0
    for d in data:
        s = set(d.keys())
        required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        if len(required - s) == 0:
            result += 1
#        else:
#            print('invalid', d)
    util.assert_equal(result, expected)


print("Part 1.")
data = load_str_blocks_list('input.txt')
test1(data, 233)

# print("Part 2.")
