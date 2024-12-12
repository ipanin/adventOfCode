# AoC 2020. Day 4: Passport Processing
import os
import re
import util


def load_list_of_dict(fname):
    folder = os.path.dirname(os.path.realpath(__file__))
    fname = os.path.join(folder, fname)
    result = []

    with open(fname, 'rt') as f:
        block = dict()
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                pairs = x.split(' ')
                for p in pairs:
                    k, v = p.split(':')
                    block[k] = v
            elif len(block) > 0:  # empty line => block ended
                result.append(block)
                block = dict()

        if len(block) > 0:
            result.append(block)
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
def valid(k: str, v: str) -> bool:
    if len(v) == 0:
        return False
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


def passport_fields_valid(d: dict) -> bool:
    for k, v in d.items():
        if not valid(k, v):
            return False

    return True


def test(data, expected):
    result = 0
    for d in data:
        s = set(d.keys())
        if len(REQUIRED_FIELDS - s) == 0:
            result += 1
    util.assert_equal(result, expected)


data = load_list_of_dict('input.txt')
REQUIRED_FIELDS = set('byr iyr eyr hgt hcl ecl pid'.split())

print("Part 1.")
test(data, 233)

data2 = filter(passport_fields_valid, data)
print("Part 2.")
test(data2, 111)
