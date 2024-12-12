# AoC 2020. Day 1.
import util

def find_mul(data0):
    data = sorted(data0)
    L = len(data)
    for i in range(L):
        a = data[i]
        for j in range(i+1, L):
            b = data[j]
            if a + b == 2020:
                return a*b
            if a + b > 2020:
                break
    return 0

def find_mul3(data0):
    data = sorted(data0)
    L = len(data)
    for i in range(L):
        a = data[i]
        for j in range(i+1, L):
            b = data[j]
            for k in range(j+1, L):
                c = data[k]
                if a + b + c == 2020:
                    return a*b*c
                if a + b + c > 2020:
                    break
    return 0


data = util.load_int_lines_list('input.txt')

print("Part 1.")
result = find_mul(data)
util.assert_equal(result, 918339)

print("Part 2.")
result = find_mul3(data)
util.assert_equal(result, 23869440)




