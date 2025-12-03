# Дан спискок диапазонов вида a-b,c-d
# В каждом диапазное найти числа
# 1. имеющие одинаковые половины, например 123123
# 2. состоящие только из одинаковых подстрок, например 121212
# Вывести сумму этих чисел
import util

def load(fname: str):
    with open(util.full_name(fname), 'rt', encoding='utf-8') as f:
        line = f.readline().rstrip()
        return [(int(pair[0]),int(pair[1])) for pair in (item.split('-') for item in line.split(','))]

def solve1(data) -> int:
    result = 0
    for rng in data:
        start, end = rng
        for i in range(start, end+1):
            s = str(i)
            if len(s)%2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                result += i
    return result

def solve2(data) -> int:
    result = 0
    for rng in data:
        start, end = rng
        for i in range(start, end+1):
            s = str(i)[::-1] # reversed string
            for sub_len in range(1,len(s)//2+1):
                if len(s) % sub_len != 0:
                    continue
                sub = s[:sub_len]
                ok = True
                for j in range(sub_len, len(s)-sub_len+1, sub_len):
                    if s[j:j+sub_len] != sub:
                        ok = False
                        break
                if ok:
                    result += i
                    break
    return result

sample = load('sample.txt')
data = load('input.txt')

util.assert_equal(solve1(sample), 1227775554, "Part 1 Sample")
util.assert_equal(solve1(data), 23534117921, "Part 1")
util.assert_equal(solve2(sample), 4174379265, "Part 2 Sample")
util.assert_equal(solve2(data), 31755323497, "Part 2")

