import util

lines = util.load_str_lines("input.txt")
clock = x = 1
p1 = 0
crt = set()

def process(clock, x, crt):
    global p1
    if clock in range(20, 221, 40):
        p1 += clock * x

    if (clock-1)%40 in range(x-1, x+2):
        crt.add(clock)

for line in lines:
    cmd = line.split()
    if cmd[0] == "addx":
        clock += 1
        process(clock, x, crt)
        x += int(cmd[1])
    clock += 1
    process(clock, x, crt)

print("Part1", p1)  # 12880
print("Part2:")  # FCJAPJRE
for i in range(6):
    row = ['#' if i*40+j in crt else '.' for j in range(40)]
    print(''.join(row))
