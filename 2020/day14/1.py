# AoC 2020. Day
import collections
import math
import re
import os
import util
from asm import Asm


def test1(fname, expected):
    # asm = Asm(fname)
    data = util.load_str_lines_list(fname)
    result = 0
    util.assert_equal(result, expected)

def get_nums(s:str):
    return [int(x) for x in re.findall("\D*(\d+)\D*", s)]

def bitmask(val, mask):
    result = 0
    pos = 1
    for c in reversed(mask):
        bit = val%2
        val = val // 2
        if c == 'X':
            pass
        elif c == '0':
            bit = 0
        elif c == '1':
            bit = 1
        result += bit * pos
        pos *= 2
    return result

data = util.load_str_lines_list('input.txt')
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
mask = ""
mem = dict()

for line in data:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        continue
    addr, val = get_nums(line)
    mem[addr] = bitmask(val,mask)

print("Part 1.", sum(mem.values()))
# test1('input.txt', 0)

