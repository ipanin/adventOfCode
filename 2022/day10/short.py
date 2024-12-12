# from https://www.reddit.com/r/adventofcode/comments/zhjfo4/comment/izmspl7/
from itertools import accumulate

f = lambda x: int(x) if x[-1].isdigit() else 0
xs = [*map(f, open('input.txt').read().split())]
part1, part2 = 0, '\n'
for i, x in enumerate(accumulate(xs, initial=1), start=1):
    if i % 40 == 20: part1 += i*x
    part2 += '# ' if (i-1)%40-x in [-1,0,1] else ('\n' if i % 40 == 0 else '  ')

print(part1, part2)