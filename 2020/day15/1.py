# AoC 2020. Day 15
import util

input = "5,2,8,16,18,0,1"
data = [int(x) for x in input.split(',')]
start_turn = len(data)

last = data.pop()
for turn in range(start_turn, 2020):
    if last not in data:
        data.append(last)
        last = 0
    else:
        curr = turn - util.rindex(data, last)-1
        data.append(last)
        last = curr

print("Part 1.", last)

