# from https://www.reddit.com/r/adventofcode/comments/rf7onx/comment/hod6ieo/
from os import pardir
from parse import findall

instr = open('input.txt').read()
dots  = list(findall('{:d},{:d}', instr))
folds = list(findall('{:l}={:d}', instr))

def fold(dots, axis, line):
    return {(min(x, 2*line-x) if axis=='x' else x, min(y, 2*line-y) if axis=='y' else y) for x,y in dots}

print("Part 1:", len(fold(dots, *folds[0])))
print("Part 2:")

for axis, line in folds:
    dots = fold(dots, axis, line)

X, Y = map(max, zip(*dots))
for y in range(Y+1):
    print(*[" #"[(x,y) in dots] for x in range(X+1)])
