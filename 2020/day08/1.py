# AoC 2020. Day 8
import util


data = util.load_str_lines_list('input.txt')
prog = []
for line in data:
    op, arg = line.split()
    prog.append([op, int(arg)])

executed = set()
ip = acc = 0

while ip not in executed:
    op, arg = prog[ip]
    executed.add(ip)
    if op == 'nop':
        ip += 1
    elif op == 'acc':
        acc += arg
        ip += 1
    elif op == 'jmp':
        ip += arg

print(acc)
