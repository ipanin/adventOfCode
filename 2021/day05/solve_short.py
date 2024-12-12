# short solution
# Steal an idea to use Counter.

from collections import Counter
import re

# x<0 => -1; x>0 => 1; otherwise 0
sign = lambda x: (x>0) - (x<0)

count = Counter()
for line in open('input.txt'):
    # just extract all numbers from string
    x1,y1,x2,y2 = [int(x) for x in re.findall(r"\d+", line)]

    dx = sign(x2-x1)
    dy = sign(y2-y1)

    count[(x1,y1)] += 1
    while x1 != x2 or y1 != y2:
        x1 += dx
        y1 += dy
        count[(x1,y1)] += 1

print(sum([c>1 for c in count.values()]))