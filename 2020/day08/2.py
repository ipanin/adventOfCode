# AoC 2020. Day 8: Handheld Halting
import util


def run(prog):
    executed = set()
    ip = acc = 0
    done = False

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
        if ip >= len(prog):
            done = True
            break

    return done, acc


def test2(fname, expected):
    data = util.load_str_lines_list(fname)
    prog = []
    for line in data:
        op, arg = line.split()
        prog.append([op, int(arg)])

    done = False
    acc = 0
    ip = 0
    for instr, arg in prog:
        fixed_prog = prog.copy()
        if instr == 'nop':
            fixed_prog[ip] = ['jmp', arg]
        elif instr == 'jmp':
            fixed_prog[ip] = ['nop', arg]
        else:
            ip += 1
            continue

        ip += 1
        done, acc = run(fixed_prog)
        if done:
            break

    util.assert_equal(acc, expected)


print("Part 2.")
test2('input0.txt', 8)
test2('input.txt', 944)
