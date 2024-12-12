# Van Eck Sequence on Numberphile
# https://oeis.org/A181391
for part in [2020,30000000]:
    nums, one = { e:i+1 for i,e in enumerate([5,2,8,16,18,0]) }, 1
    for turn in range(7, part):
        nums[one], one = turn, 0 if one not in nums else turn-nums[one]
    print(one)

###

import sys
for line in sys.stdin:
    inp = list(map(int, line.strip().split(',')))
    last = dict()
    lnum = None
    for i in range(30000000):
        if i < len(inp):
            num = inp[i]
        else:
            if lnum not in last:
                num = 0
            else:
                num = (i-1)-last[lnum]
        last[lnum] = i-1
        lnum = num
    print(num)