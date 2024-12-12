# AoC 2020. Assembler interpretator
import util


class Asm():
    def __init__(self, fname=''):
        self.prog = []
        self.reset()

        if len(fname):
            self.prog = Asm.load_asm(fname)

    def reset(self):
        self.ip = 0  # instruction pointer
        self.acc = 0  # accumulator register

    @staticmethod
    def load_asm(fname):
        prog = []
        with open(util.full_name(fname), 'rt') as f:
            for line in f.readlines():
                if not len(line) or line.startswith(';'):
                    continue

                op, arg = line.split()
                prog.append([op, int(arg)])
        return prog

    def run_no_loop(self):
        self.reset()
        executed = set()

        while self.ip < len(self.prog) and self.ip not in executed:
            executed.add(self.ip)
            self.step()

        if self.ip != len(self.prog):
            raise Exception(f"Incorrect exit: ip = {self.ip}")

    def run(self):
        self.reset()

        while self.ip < len(self.prog):
            self.step()

        if self.ip != len(self.prog):
            raise Exception(f"Incorrect exit: ip = {self.ip}")

    def step(self):
        op, arg = self.prog[self.ip]

        if op == 'nop':
            pass
        elif op == 'acc':
            self.acc += arg
        elif op == 'jmp':
            self.ip += arg
            return
        else:
            raise Exception(f"Error at {self.ip}: unknown op = {op}")

        self.ip += 1

