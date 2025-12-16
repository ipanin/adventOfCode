# 1. Кнопка переключает определенные биты. Найти наименьшее количество кнопок,
# чтобы включить указанные биты.
import itertools as it
import util

def solve1(lines) -> int:
    res = 0
    for  line in lines:
        target, masks, _ = parse(line)
        res += min_mask_count(masks, target)

    return res

def min_mask_count(masks, target):
    for i in range(len(masks)):
        tuples = it.combinations(masks, i+1)
        for tup in tuples:
            mask = 0
            for m in tup:
                mask ^= m
            if mask == target:
                return i+1
    raise Exception("Not Found")

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
util.assert_equal(solve1(sample_data), 7, "Part 1 Sample")

data = util.load_str_lines('input.txt')
util.assert_equal(solve1(data), 375, "Part 1")
