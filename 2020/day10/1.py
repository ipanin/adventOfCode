# AoC 2020. Day 10. Power adapters
import util


data = util.load_int_lines_list('input.txt')

jolts = sorted(data)
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

j1 = j3 = 0
for i in range(1, len(jolts)):
    if jolts[i] - jolts[i-1] == 1:
        j1 += 1
    elif jolts[i] - jolts[i-1] == 3:
        j3 += 1
print("Part 1. ", j1*j3)
