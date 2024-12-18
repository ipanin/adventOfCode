import re

a, b, c, *prog = map(int, re.findall(r'\d+', open('input.txt').read()))

def execute(a, b, c):
    result = []
    i = 0
    while i in range(len(prog)):
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        op, arg = prog[i:i+2]
        match op:
            case 0: a >>= combo[arg]
            case 1: b ^= arg
            case 2: b = 7 & combo[arg]
            case 3:
                if a: i = arg; continue
            case 4: b ^= c
            case 5: result.append(combo[arg] & 7)
            case 6: b = a >> combo[arg]
            case 7: c = a >> combo[arg]
        i += 2
    return result

print('Part 1.')
print(*execute(a,b,c), sep=',')


def find(a, i):
    if execute(a, b, c) == prog:
        print(a)
        exit(0)
    if execute(a, b, c) == prog[-i:] or i==0:
        for n in range(8):
            find(8*a+n, i+1)

print('Part 2.')
find(0, 0)
