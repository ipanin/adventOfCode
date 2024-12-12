# from https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpsjfis/
instr = [*open('day24/input.txt')]

p = 99999999999999
q = 11111111111111
stack = []

for i in range(14):
    a = int(instr[18*i+5].split()[-1])
    b = int(instr[18*i+15].split()[-1])

    if a > 0: stack+=[(i, b)]; continue
    j, b = stack.pop()

    p -= abs((a+b)*10**(13-[i,j][a>-b]))
    q += abs((a+b)*10**(13-[i,j][a<-b]))

print(p, q)
