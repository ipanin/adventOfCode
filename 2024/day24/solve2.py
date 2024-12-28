import util

BITS = 46

def parse_ops(op_list: list[str]) -> dict[str, list[str]]:
    ops = {}
    for line in op_list:
        inputs, output = line.split(' -> ')
        i1, op, i2 = inputs.split()
        ops[output] = [op, i1, i2]
    return ops

def solve2(op_list: dict[str, list[str]]):
    for bit in range(BITS-1):
        for x in range(3):
            ok = True
            for y in range(3):
                x1 = x << bit
                y1 = y << bit
                if not test(x1,y1, op_list):
                    ok = False
                    break
            if not ok:
                break

def test(x:int, y:int, op_list: dict[str, list[str]]):
    z = calculate(x,y,op_list)
    expected = (x + y) % 2**BITS
    if expected != z:
        zstr = format(z, f'0{BITS}b')
        expstr = format(expected, f'0{BITS}b')
        wrong_bits = []
        for i in range(BITS):
            if zstr[-i-1] != expstr[-i-1]:
                wrong_bits.append(i)
        print(f'x={x}, y={y}, z={z}, expected={expected}, wrong bits={wrong_bits}')
        return False
    return True

def calculate(x: int, y: int, op_list: dict[str, list[str]]) -> int:
    in_list = {}
    for bit in range(BITS):
        xbit = x & 1
        ybit = y & 1
        in_list[f'x{bit:02}'] = xbit
        in_list[f'y{bit:02}'] = ybit
        x >>= 1
        y >>= 1

    changed = True
    while changed:
        changed = False
        for out, v in op_list.items():
            if out not in in_list:
                op, i1, i2 = v
                if i1 in in_list and i2 in in_list:
                    match op:
                        case 'AND': r = in_list[i1] & in_list[i2]
                        case 'OR' : r = in_list[i1] | in_list[i2]
                        case 'XOR': r = in_list[i1] ^ in_list[i2]
                        case _: raise Exception(f"Unknown op {op}")

                    in_list[out] = r
                    changed = True

    res = 0
    for i, val in in_list.items():
        if i.startswith('z'):
            res += val * 2**int(i[1:])

    return res


block2 = util.load_str_lines('input2.txt')
op_list = parse_ops(block2)
solve2(op_list)
# bks,hnd,nrn,tdv,tjp,z09,z16,z23