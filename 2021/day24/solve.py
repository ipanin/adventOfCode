# Day 24: Arithmetic Logic Unit

from functools import cache
import util

N = 14
div= [ 1,  1,  1, 26,  1, 26, 26,  1,  1,  1, 26, 26, 26, 26]
a =  [13, 11, 15, -6, 15, -8, -4, 15, 10, 11,-11,  0, -8, -7]
b =  [ 3, 12,  9, 12,  2,  1,  1, 13,  1,  6,  2, 11, 10,  3]

@cache
def check_max(i: int, res: int) -> str:
    mod = res // div[i]
    rem = res % 26

    if i == N-1:
        digit = rem + a[i]
        if (0 < digit < 10) and (mod == 0): 
            return str(digit)
        else: 
            return ""

    for digit in range(9, 0, -1):
        if digit == rem + a[i]:
            res1 = mod
        else:
            res1 = mod * 26 + digit + b[i]

        digits1 = check_max(i+1, res1)
        if len(digits1):
            return str(digit) + digits1

    return ""

'''
def check_digit(digit, i, rem, mod):
    if digit != rem + a[i]:
        res1 = mod * 26 + digit + b[i]
    else:
        res1 = mod

    if i == N-1:
        if res1 == 0: return str(digit)
        else: return ""

    return check_max(i+1, res1)
    if len(digits1):
        return str(digit) + digits1
'''

@cache
def check_min(i: int, res: int) -> str:
    mod = res // div[i]
    rem = res % 26
    for digit in range(1,10):
        if digit != rem + a[i]:
            res1 = mod * 26 + digit + b[i]
        else:
            res1 = mod

        if i == N-1:
            if res1 == 0: return str(digit)
            else: continue

        digits1 = check_min(i+1, res1)
        if len(digits1):
            return str(digit) + digits1

    return ""

def test(title, func, expected):
    result = func(0, 0)
    print(title, result)
    util.assert_equal(result, expected)

test("Part 1.", check_max, "91699394894995")
test("Part 2.", check_min, "51147191161261")