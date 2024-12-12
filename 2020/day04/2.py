# AoC 2020. Day
import os
import re
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
                    if not valid(k, v):
                        continue
                    data[k] = v
            elif len(data.keys()) > 0:
                result.append(data)
                data = dict()

    return result

# byr(Birth Year) - four digits; at least 1920 and at most 2002.
# iyr(Issue Year) - four digits; at least 2010 and at most 2020.
# eyr(Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt(Height) - a number followed by either cm or in:
#    If cm, the number must be at least 150 and at most 193.
#    If in , the number must be at least 59 and at most 76.

# hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
# ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid(Passport ID) - a nine-digit number, including leading zeroes.
def valid(k, v):
    if len(v) == 0:
        return False
    #if (k in ['byr','iyi'] )
    if k == 'byr':
        return 1920 <= int(v) <= 2002
    if k == 'iyr':
        return 2010 <= int(v) <= 2020
    if k == 'eyr':
        return 2020 <= int(v) <= 2030
    if k == 'hgt':
        m = re.fullmatch('([0-9]+)(cm|in)', v)
        if not m:
            return False
        h = int(m.group(1))
        ss = m.group(2)
        return (ss == 'cm' and (150 <= h <= 193)) or (ss == 'in' and (59 <= h <= 76))
    if k == 'hcl':
        return bool(re.fullmatch('#[0-9a-f]{6}', v))
    if k == 'ecl':
        return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if k == 'pid':
        return bool(re.fullmatch('[0-9]{9}', v))

    return True


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


print("Part 2.")
data = load_str_blocks_list('input.txt')
test1(data, 111)
