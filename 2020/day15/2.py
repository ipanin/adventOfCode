# AoC 2020. Day 15

input = "5,2,8,16,18,0,1"
data = [int(x) for x in input.split(',')]
start_turn = len(data)
last = data.pop()
lasts = {5:1, 2:2, 8:3, 16:4, 18:5, 0:6}

for turn in range(start_turn, 30000000):
    if turn % 1000000 == 0: print(turn)
    if last not in lasts.keys():
        lasts[last] = turn
        last = 0
    else:
        curr = turn - lasts[last]
        lasts[last] = turn
        last = curr

print("Part 2.", last)

