# AoC 2020. Day 1. Report Repair
import util
from typing import List

def find_sum2(data : List[int], target : int) -> (int, int):
    datas = sorted(data)
    L = len(datas)
    for i in range(L):
        a = datas[i]
        for j in range(i+1, L):
            b = datas[j]
            if a + b == target:
                return (a,b)
            if a + b > target:
                break
    return (0, 0)

def find_sum3(data : List[int], target : int) -> (int, int, int):
    datas = sorted(data)
    L = len(datas)
    for i in range(L):
        a = datas[i]
        for j in range(i+1, L):
            b = datas[j]
            if a + b > 2020:
                break
            for k in range(j+1, L):
                c = datas[k]
                if a + b + c == 2020:
                    return (a,b,c)
                if a + b + c > 2020:
                    break
    return (0, 0, 0)

data = util.load_int_lines_list('input.txt')

print("Part 1.")
a, b = find_sum2(data, 2020)
print (a, b)
util.assert_equal(a*b, 918339)

print("Part 2.")
a, b, c = find_sum3(data, 2020)
print (a, b, c)
util.assert_equal(a*b*c, 23869440)




