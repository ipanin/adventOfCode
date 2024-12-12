# AoC 2020. Day 18: Operation Order
# Calculate expressions with operation order
import collections
import util

# 1 + (2 * 3) + (4 * (5 + 6))
# 1 + 2 * 3
# (1 + 2) * 3
def eval_sub(line, i, calc_fun):
    open = 1
    end = i
    while open > 0:
        if line[end] == ')': open -= 1
        if line[end] == '(': open += 1
        end += 1
    return calc_fun(line[i:end-1]), end

def get_arg(line, i, calc_fun):
    while line[i] == ' ': i+=1
    if line[i] == '(':
        arg, i = eval_sub(line, i+1, calc_fun)
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

# multiplication and addition operators have the same precedence
def calc1(line):
    i = 0
    res, i = get_arg(line, i, calc1)
    while i < len(line):
        op, i = get_op(line, i)
        arg, i = get_arg(line, i, calc1)
        if op == '+':
            res += arg
        if op == '*':
            res *= arg
    return res

# addition is evaluated before multiplication
def calc2(line):
    mul = collections.deque()
    i = 0
    arg1, i = get_arg(line, i, calc2)
    while i < len(line):
        op, i = get_op(line, i)
        arg2, i = get_arg(line, i, calc2)
        if op == '+':
            arg1 += arg2
        if op == '*':
            mul.append(arg1)
            arg1 = arg2
    
    while len(mul) > 0:
        arg1 *= mul.pop()

    return arg1

util.assert_equal(calc1("1 + (2 * 3) + (4 * (5 + 6))"), 51)
util.assert_equal(calc1("2 * 3 + (4 * 5)"), 26)
util.assert_equal(calc1("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 437)
util.assert_equal(calc1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 12240)
util.assert_equal(calc1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13632)

util.assert_equal(calc2("1 + (2 * 3) + (4 * (5 + 6))"), 51)
util.assert_equal(calc2("2 * 3 + (4 * 5)"), 46)
util.assert_equal(calc2("5 + (8 * 3 + 9 + 3 * 4 * 3)"), 1445)
util.assert_equal(calc2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 669060)
util.assert_equal(calc2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 23340)

data = util.load_str_lines_list('input.txt')

part1 = sum(map(calc1, data))
print("Part 1.", part1)
util.assert_equal(part1, 1402255785165)

part2 = sum(map(calc2, data))
print("Part 2.", part2)
util.assert_equal(part2, 119224703255966)


