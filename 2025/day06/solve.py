# Даны арифметические задачи.
# 1. Вычислить произведение или сумму чисел в столбце.
# 2. Вычислить тоже самое, но числа записаны вертикально -
# старший разряд в первой строке, следущий разряд во 2й строке и т.д.

import util

def solve1(data) -> int:
    ops = data[-1].split()

    results = []
    for op in ops:
        if op == '*':
            results.append(1)
        else:
            results.append(0)

    for line in data[:-1]:
        for i,x in enumerate(line.split()):
            if ops[i] == '*':
                results[i] *= int(x)
            else:
                results[i] += int(x)

    return sum(results)

def solve2(data) -> int:
    ops = data[-1].split()

    data1 = transpose(data[:-1])

    results = []
    for op in ops:
        if op == '*':
            results.append(1)
        else:
            results.append(0)

    i = 0
    for line in data1:
        if line.strip() == '':
            i+=1
            continue
        if ops[i] == '*':
            results[i] *= int(line)
        else:
            results[i] += int(line)

    return sum(results)

def transpose(data):
    result = []
    w = len(data[0])
    h = len(data)
    for i in range(w):
        line = ''
        for j in range(h):
            line += data[j][i]
        result.append(line)
    return result

def load_str_lines(fname: str) -> list[str]:
    data = []
    with open(util.full_name(fname), 'rt', encoding='utf-8') as f:
        for line in f.readlines():
            data.append(line)

    return data

sample_data = load_str_lines('sample.txt')
util.assert_equal(solve1(sample_data), 4277556, "Part 1 Sample")
util.assert_equal(solve2(sample_data), 3263827, "Part 2 Sample")

data = load_str_lines('input.txt')
util.assert_equal(solve1(data),  4583860641327, "Part 1")
util.assert_equal(solve2(data), 11602774058280, "Part 2")
