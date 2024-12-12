# solution from https://www.reddit.com/r/adventofcode/comments/zesk40/comment/iz8fww6/
from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
for line in open('input.txt'):
    match line.split():
        case '$', 'cd', '/': cwd = ['/']
        case '$', 'cd', '..': cwd.pop()
        case '$', 'cd', dir_name: cwd.append(dir_name + '/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for parent in accumulate(cwd):
                dirs[parent] += int(size)

print("Part1", sum(size for size in dirs.values() if size <= 100_000))
print("Part2", min(size for size in dirs.values() if size >= dirs['/'] - 40_000_000))
