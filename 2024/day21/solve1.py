# Day 21: Keypad Conundrum (головоломка)
import util

def solve1(codes, num_robots) -> int:
    res = 0
    for code in codes:
        seq = convert(code, num_robots)
        res += complexity(code, seq)
    return res

def convert(code, num_robots):
    seq = numpad2dir(code)
    for _ in range(num_robots-1):
        seq = dirpad2dir(seq)

    return seq

NUMPAD = {
    '7': 0,  '8': 1,    '9': 2,
    '4': 1j, '5': 1+1j, '6': 2+1j,
    '1': 2j, '2': 1+2j, '3': 2+2j,
    '0': 1+3j, 'A': 2+3j
}

DIRPAD = {
             '^': 1,    'A': 2,
    '<': 1j, 'v': 1+1j, '>': 2+1j
}

def numpad2dir(code: str):
    pos = 'A'
    res = ''
    for c in code:
        res += move(NUMPAD, pos, c) + 'A'
        pos = c

    return res

def dirpad2dir(code):
    pos = 'A'
    res = ''
    for c in code:
        res += move2(pos, c) + 'A'
        pos = c

    return res

NAV_REV = {
    'A': { '<' : '^', ''   : 'A', 'v'  : '>', '<v': 'v','v<<': '<', '<v<': '<'},
    '^': { ''  : '^', '>'  : 'A', 'v>' : '>', 'v' : 'v', 'v<': '<'},
    '>': { '<^': '^', '^'  : 'A', ''   : '>',  '<': 'v', '<<': '<'},
    'v': { '^' : '^', '>^' : 'A', '>'  : '>',   '': 'v', '<' : '<'},
    '<': { '>^': '^', '>>^': 'A', '>>' : '>',  '>': 'v', ''  : '<'}
}

def decode(seq: str)-> str:
    res = []
    pos = 'A'
    moves = seq.split('A')
    for m in moves:
        pos = NAV_REV[pos][m]
        res.append(pos)

    return ''.join(res[:-1])

def move(pad: dict[str, complex], pos, c) -> str:
    start = pad[pos]
    end = pad[c]
    res = []
    dx = int(end.real - start.real)
    dy = int(end.imag - start.imag)
    stepx = 1 if dx > 0 else -1
    stepy = 1j if dy > 0 else -1j

    if dx > 0:
        for _ in range(dx):
            res.append(util.DIRECTION_MAP_REV[stepx])

    if dx < 0 and start.imag < 3:
        for _ in range(-dx):
            res.append(util.DIRECTION_MAP_REV[stepx])

    for _ in range(abs(dy)):
        res.append(util.DIRECTION_MAP_REV[stepy])

    if dx < 0 and start.imag == 3:
        for _ in range(-dx):
            res.append(util.DIRECTION_MAP_REV[stepx])

    return ''.join(res)

NAV = {
    'AA': '',   'A^':'<',   'A>':'v',   'Av': '<v', 'A<':'v<<',
    '^^': '',   '^A':'>',   '^>':'v>',  '^v': 'v',  '^<':'v<',
    '>^': '<^', '>A':'^',   '>>':'',    '>v': '<',  '><':'<<',
    'v^': '^',  'vA':'>^',  'v>':'>',   'vv': '',   'v<':'<',
    '<^': '>^', '<A':'>>^', '<>':'>>',  '<v': '>',  '<<':''
}

NAV0 = {
    'AA': '',   'A^':'<',   'A>':'v',   'Av': 'v<', 'A<':'v<<',
    '^^': '',   '^A':'>',   '^>':'v',   '^v': 'v',  '^<':'v<',
    '>^': '^<', '>A':'^',   '>>':'',    '>v': '<',  '><':'<<',
    'v^': '^',  'vA':'>^',  'v>':'>',   'vv': '',   'v<':'<',
    '<^': '>^', '<A':'>>^', '<>':'>>',  '<v': '>',  '<<':''
}

NAVA = {
    'AA': 'A',   'A^':'<A',   'A>':'vA',   'Av': '<vA', 'A<':'v<<A',
    '^^': 'A',   '^A':'>A',   '^>':'vA',   '^v': 'vA',  '^<':'v<A',
    '>^': '<^A', '>A':'^A',   '>>':'A',    '>v': '<A',  '><':'<<A',
    'v^': '^A',  'vA':'>^A',  'v>':'>A',   'vv': 'A',   'v<':'<A',
    '<^': '>^A', '<A':'>>^A', '<>':'>>A',  '<v': '>A',  '<<':'A'
}
NAV1 = {
    'AA': '', 'A^':'<', 'A>':'v', 'Av': '<v', 'A<':'<v<',
    '^^': '', '^A':'>', '^>':'v', '^v': 'v',  '^<':'v<',
    '>^': '<^', '>A':'^', '>>':'', '>v': '<',  '><':'<<',
    'v^': '^', 'vA':'>^', 'v>':'>', 'vv': '',  'v<':'<',
    '<^': '>^', '<A':'>>^', '<>':'>>', '<v': '>',  '<<':''
}

def move2(pos:str, c:str) -> str:
    return NAV[pos+c]

def complexity(code, seq):
    i = 1
    s = 0
    for c in reversed(code):
        if c.isdigit():
            s += int(c)*i
            i *= 10

    return len(seq) * s

def test(data):
    for k,v in data.items():
        res = convert(k, 3)
        #util.assert_equal(res, v, f"Sample {k}")
        util.assert_equal(len(res), len(v), f"Sample {k}")

codes = util.load_str_lines('sample.txt')
util.assert_equal(solve1(codes, 3), 126384, "Part 1 sample")

data = {
'029A': '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A',
'980A': '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A',
'179A': '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A',
'456A': '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A',
'379A': '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
}

test(data)
#seq = '<A^A>^^AvvvA'
code = '379A'
seq = numpad2dir(code)
#seq1 = dirpad2dir(seq)
#seq2 = dirpad2dir(seq1)

seq3 = data[code]
print(seq3)
seq2 = decode(seq3)
print(seq2)
seq1 = decode(seq2)
print(seq1)
print(seq)
codes = util.load_str_lines('input.txt')
util.assert_equal(solve1(codes, 3), 0, "Part 1")
