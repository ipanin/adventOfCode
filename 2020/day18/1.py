# AoC 2020. Day
import collections
import math
import re
import os
import util

# 1 + (2 * 3) + (4 * (5 + 6))
# 1 + 2 * 3
# (1 + 2) * 3
def eval_sub(line, i):
    open = 1
    end = i
    while open > 0:
        if line[end] == ')': open -= 1
        if line[end] == '(': open += 1
        end += 1
    return calc1(line[i:end-1]), end

def get_arg(line, i):
    while line[i] == ' ': i+=1
    if line[i] == '(':
        arg, i = eval_sub(line, i+1)
        return (arg, i)

    arg = ''
    while i < len(line) and line[i].isdigit():
        arg += line[i]
        i += 1
    return (int(arg), i)

def get_op(line, i):
    while line[i] == ' ': i+=1
    
    if line[i] in ['+', '*']:
        return line[i], i+1

    print('unexpected op', line[i])

def calc1(line):
    #stack = deque()
    i = 0
    res, i = get_arg(line, i)
    while i < len(line):
        op, i = get_op(line, i)
        arg, i = get_arg(line, i)
        if op == '+':
            res += arg
        if op == '*':
            res *= arg
    return res


def solve1(data):
    res = 0
    for line in data:
        res += calc1(line)
    return res


util.assert_equal(calc1("1 + (2 * 3) + (4 * (5 + 6))"), 51)
util.assert_equal(calc1("2 * 3 + (4 * 5)"), 26)
util.assert_equal(calc1("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 437)
util.assert_equal(calc1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 12240)
util.assert_equal(calc1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13632)

data = util.load_str_lines_list('input.txt')
part1 = sum(map(calc1, data))
print("Part 1.", part1)
#util.assert_equal(result, 0)


