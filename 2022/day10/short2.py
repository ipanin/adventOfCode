#https://github.com/juanplopes/advent-of-code-2022/blob/main/day10.py
def execute(program):
    x = 1
    for line in program:
        yield x
        if line[0] == 'addx':
            yield x
            x += int(line[1])

S = list(execute(line.split() for line in open("input.txt").readlines()))
print(sum(S[i-1]*i for i in range(20,221,40)))

for i in range(6):
    print(''.join('.#'[abs(S[i*40+j] - j) <= 1] for j in range(40)))
