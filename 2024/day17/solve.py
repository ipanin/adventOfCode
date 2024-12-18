"""
Combo: 0..3 = digit, 4=A, 5=B, 6=C, 7-reserved

adv (opcode 0) A = A >> combo(arg)
bdv (opcode 6) B = A >> combo(arg)
cdv (opcode 7) C = A >> combo(arg)
bxl (opcode 1) B = B XOR arg
bxc (opcode 4) B = B XOR C
bst (opcode 2) B = combo(arg) % 8
jnz (opcode 3) if A != 0: IP = arg
out (opcode 5) print(combo % 8),

Register A: 56256477
Register B: 0
Register C: 0

Program: 2,4, 1,1, 7,5, 1,5, 0,3, 4,3, 5,5, 3,0
    bst A
    bxl 1
    cdv B
    bxl 5
    adv 3
    bxc 3
    out B
    jnz 0

    B = A%8 XOR 1
    C = A >> B
    B = B XOR 5
    A = A >> 3
    B = B XOR C
    print(B%8)
    if A == 0: break
"""

def combo(arg, a,b,c):
    if arg < 4:
        return arg
    return a if arg == 4 else b if arg == 5 else c

def execute(program, a,b,c):
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        arg = program[ip + 1] #
        match opcode:
            case 0:
                a = a >> combo(arg, a,b,c)
            case 1:
                b = b ^ arg
            case 2:
                b = combo(arg, a,b,c) % 8
            case 3:
                if a != 0:
                    ip = arg
                    continue
            case 4:
                b = b ^ c
            case 5:
                print(combo(arg, a,b,c)%8, end=',')
            case 6:
                b = a >> combo(arg, a,b,c)
            case 7:
                c = a >> combo(arg, a,b,c)

        ip += 2

def verify_my_program(expected_output, A):
    out_index = 0
    while A != 0:
        B = (A%8) ^ 1
        out = (B ^ 5 ^ (A >> B)) % 8
        if out != expected_output[out_index]:
            return False
        out_index += 1
        A >>= 3
    return out_index == len(expected_output)

def reverse_recursive(program, a: int) -> int:
    result = 0
    out = program[-1]
    for b_curr in range(8):
        a_curr = a << 3 | b_curr
        b = b_curr ^ 1
        out1 = (b ^ 5 ^ (a_curr >> b)) % 8
        if out1 == out:
            if len(program) == 1:
                return a_curr
            result = reverse_recursive(program[:-1], a_curr)
            if result >= 0:
                return result
    return -1

program = [2,4, 1,1, 7,5, 1,5, 0,3, 4,3, 5,5, 3,0]
print('Part 1.')
execute(program, 56256477, 0, 0)
# 4,1,5,3,1,5,3,5,7

print('\nPart 2.', reverse_recursive(program, 0))
execute(program, 164_542_125_272_765, 0, 0)
