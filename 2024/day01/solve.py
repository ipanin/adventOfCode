# Даны 2 столбца чисел. Самые маленькие в каждом столбце объединяются в пару. Затем следующие 2.
# Часть 1 - посчитать сумму абсолютных разниц по каждой паре.
# Решение 1 - отсортировать каждый столбец. Последовательно посчитать модуль разности i-тых элементов.

# Часть 2 - Посчитать похожесть 1го столбца на 2й. Похожесть столбца это сумма похожести для каждого его элемента.
# Похожесть элемента a = <сколько раз он встречается во 2м столбце> * a. 
# Решение 2 - использовать collections.Counter для подсчета частоты элементов во 2м списке.

import util
from collections import Counter

def load_2_vertical_arrays(fname: str) -> (list[int],list[int]):
    data1 = []
    data2 = []
    with open(util.full_name(fname), 'rt') as f:
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                a, b =line.split()
                data1.append(int(a))
                data2.append(int(b))

    return data1, data2

def distance(a1, a2) -> int:
    sorted_a1 = sorted(a1)
    sorted_a2 = sorted(a2)
    return sum([abs(x[0]-x[1]) for x in zip(sorted_a1, sorted_a2)])

def similarity(a1, a2) -> int:
    result = 0
    c2 = Counter(a2)
    for a in a1:
        if c2[a] > 0:
            result += c2[a]*a
    return result

a1, a2 = load_2_vertical_arrays('input.txt')

part1 = distance(a1, a2)
util.assert_equal(part1, 1879048, "Part1")

part2 = similarity(a1, a2)
util.assert_equal(part2, 21024792, "Part2")
