# 2. Кнопка увеличивает указанные счетчики. Найти наименьше количество нажатий
# кнопок, чтобы получить указанные значения всех счетчиков.
import itertools as it
import numpy as np;
import util

def solve2(lines) -> int:
    res = 0
    for  line in lines:
        _, masks, joltage = parse(line)
        res += min_sum_count(masks, joltage)

    return res

def min_sum_count(masks, targets):
    N = len(targets)
    tuples = it.combinations(masks, N)
    res = 10**20
    for tup in tuples:
        s = sum_count(tup, targets)
        if s > 0 and s < res:
            res = s
    return res

def sum_count(masks, targets):
    N = len(targets)
    arr = []
    for m in masks:
        line = []
        for i in range(N):
            bit = m%2
            m >>= 1
            line.append(bit)
        arr.append(line)

    a = np.array(arr)

    if np.linalg.det(a) == 0:
        return -1
    b = np.array(targets)
    x = np.linalg.solve(a.T, b)
    if sum((xx < 0 for xx in x)) > 0:
        return -1
    return sum(x)

def parse(line: str):
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    target = 0
    masks = []
    joltage = []
    translation_table = str.maketrans('.#', '01')
    items = line.split()
    for item in items:
        if item[0] == '[':
            s = item[-2:0:-1].translate(translation_table)
            target = int(s, 2)
        elif item[0] == '(':
            mask = 0
            for i in item[1:-1].split(','):
                mask |= 1 << int(i)
            masks.append(mask)
        elif item[0] == '{':
            joltage= [int(i) for i in item[1:-1].split(',')]
    return target, masks, joltage


sample_data = util.load_str_lines('sample.txt')
util.assert_equal(solve2(sample_data), 33, "Part 2 Sample")

#data = util.load_str_lines('input.txt')
#util.assert_equal(solve2(data), 0, "Part 2")
