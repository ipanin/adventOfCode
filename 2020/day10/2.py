# AoC 2020. Day 10
import util


data = util.load_int_lines_list('input.txt')

jolts = sorted(data)
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

j1 = j3 = 0
mul = [1, 1, 2, 4, 7, 13]  # why 7?
L = 0
part2 = 1
for i in range(1, len(jolts)):
    if jolts[i] - jolts[i-1] == 1:
        j1 += 1
        L += 1
    elif jolts[i] - jolts[i-1] == 2:
        print("+2")
    elif jolts[i] - jolts[i-1] == 3:
        j3 += 1
        print('L=', L)
        part2 *= mul[L]
        L = 0

print("Part 1. ", j1*j3)
print("Part 2. ", part2)  # 9256148959232
