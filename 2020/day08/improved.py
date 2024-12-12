# AoC 2020. Day 8: Handheld Halting
import util
from asm import Asm


def test1(fname, expected):
    asm = Asm(fname)

    try:
        asm.run_no_loop()
    except Exception:
        pass

    util.assert_equal(asm.acc, expected)


def test2(fname, expected):
    asm = Asm(fname)
    bug_program = asm.prog.copy()

    ip = 0
    for instr, arg in asm.prog:
        if instr == 'nop':
            asm.prog[ip] = ['jmp', arg]
        elif instr == 'jmp':
            asm.prog[ip] = ['nop', arg]
        else:
            ip += 1
            continue

        ip += 1
        try:
            asm.run_no_loop()
            break  # finished, bug fixed
        except Exception:  # bug not fixed
            asm.prog = bug_program.copy()

    util.assert_equal(asm.acc, expected)


print("Part 1.")
test1('input0.txt', 5)
test1('input.txt', 1915)

print("Part 2.")
test2('input0.txt', 8)
test2('input.txt', 944)
