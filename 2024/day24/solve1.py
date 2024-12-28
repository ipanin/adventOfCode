import util

def parse_inputs(in_list: list[str]) -> dict[str, int]:
    inputs = {}
    for line in in_list:
        inp, value = line.split(': ')
        inputs[inp] = int(value)
    return inputs

def parse_ops(op_list: list[str]) -> dict[str, list[str]]:
    ops = {}
    for line in op_list:
        inputs, output = line.split(' -> ')
        i1, op, i2 = inputs.split()
        ops[output] = [op, i1, i2]
    return ops

def solve1(in_list: dict[str, int], op_list: dict[str, list[str]]) -> int:
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


block1, block2 = util.load_str_blocks('sample.txt')
in_list = parse_inputs(block1)
op_list = parse_ops(block2)
util.assert_equal(solve1(in_list, op_list), 2024, "Part 1 sample")

block1, block2 = util.load_str_blocks('input.txt')
in_list = parse_inputs(block1)
op_list = parse_ops(block2)
util.assert_equal(solve1(in_list, op_list), 53190357879014, "Part 1")

