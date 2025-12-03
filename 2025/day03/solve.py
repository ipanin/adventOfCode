# Каждая строка содержит цифрры. Из этих цифр нужно составить число,
# не меняя порядок цифр, но можно пропускать цифры.
# 1. Выбрать две цифры, дающие максимальное число.
# 2. Выбрать 12 цифр, дающие максимальное число.
# Вывести сумму этих чисел

import util

def solve1(data) -> int:
    result = 0
    for line in data:
        result += joltage1(line)
    return result

def joltage1(line):
    first = 0
    first_pos = -1
    for i, v in enumerate(line[:-1]):
        vv = int(v)
        if vv > first:
            first = vv
            first_pos = i
        if vv == 9:
            break

    second = 0
    for i, v in enumerate(line[first_pos+1:]):
        vv = int(v)
        if vv > second:
            second = vv
        if vv == 9:
            break

    return first*10+second

def solve2(data) -> int:
    result = 0
    for line in data:
        result += joltage2(line, 12)
    return result

def joltage2(line, ndigits: int):
    result = ''
    found_index = -1
    end_index = len(line) - ndigits
    for _ in range(ndigits):
        start_index = found_index+1
        found = 0
        for i in range(start_index, end_index+1):
            d = int(line[i])
            if d > found:
                found = d
                found_index = i
            if d == 9:
                break
        end_index += 1
        result += str(found)

    return int(result)

sample = util.load_str_lines('sample.txt')
data = util.load_str_lines('input.txt')

util.assert_equal(solve1(sample), 357, "Part 1 Sample")
util.assert_equal(solve1(data), 17158, "Part 1")
util.assert_equal(joltage2('987654321111111', 12), 987654321111, "Part 2 Sample line")
util.assert_equal(solve2(sample), 3121910778619, "Part 2 Sample")
util.assert_equal(solve2(data), 170449335646486, "Part 2")
