# AoC 2020. Day
import re
import util


def test1(fname, expected):
    data = util.load_str_lines_list(fname)
    result = 0
    util.assert_equal(result, expected)

def get_nums(s:str):
    return [int(x) for x in re.findall("\D*(\d+)\D*", s)]

def bitmask(val, mask):
    result = []
    for c in reversed(mask):
        bit = str(val % 2)
        val = val // 2
        if c == '0':
            pass
        elif c == '1':
            bit = '1'
        elif c == 'X':
            bit = 'X'
        result.append(bit)
    return "".join(reversed(result))

def fill_x(mask: str, val: int) -> int:
    result = 0
    pos = 1
    for c in reversed(mask):
        if c == 'X':
            bit = val%2
            val = val // 2
        elif c == '0':
            bit = 0
        elif c == '1':
            bit = 1
        result += bit * pos
        pos *= 2
    return result

def write(mem, addr_mask, val):
    cnt = addr_mask.count('X')
    for i in range(2**cnt):
        addr = fill_x(addr_mask, i)
        mem[addr] = val

data = util.load_str_lines_list('input.txt')
mask = ""
mem = dict()

for line in data:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        continue
    addr, val = get_nums(line)
    addr_mask = bitmask(addr,mask)
    write(mem, addr_mask, val)

print("Part 2.", sum(mem.values()))
# test1('input.txt', 0)

