import util


def solve1(data) -> int:
    count = 0
    for line in data:
        if check_eq(line[0], line[1:]):
            count += line[0]
    return count

def check_eq(answer: int, arguments: list[int]) -> bool:
    N = len(arguments) - 1
    for i in range(2**N):
        bits = to_bits(i, N)
        res = arguments[0]
        for b, bit in enumerate(bits):
            if bit:
                res *= arguments[b+1]
            else:
                res +=  arguments[b+1]
            if res > answer:
                break
        if res == answer:
            return True
    return False

def to_bits(i: int, N: int) -> list[bool]:
    bits = []
    for j in range(N):
        bits.append(((i >> j) & 1) == 1)
    return bits

def solve2(data) -> int:
    count = 0
    for line in data:
        print('.', end='')
        if check_eq2(line[0], line[1:]):
            count += line[0]
    return count

def check_eq2(answer: int, arguments: list[int]) -> bool:
    N = len(arguments) - 1
    for i in range(3**N):
        digits = to_digits(i, N, 3)
        res = arguments[0]
        for b, digit in enumerate(digits):
            if digit == 0:
                res +=  arguments[b+1]
            elif digit == 1:
                res *= arguments[b+1]
            else:
                res = concatenate(res, arguments[b+1])

            if res > answer:
                break
        if res == answer:
            return True
    return False

def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))


def to_digits(i: int, N: int, base: int) -> list[int]:
    digits = []
    for _ in range(N):
        digit = i % base
        i = i // base
        digits.append(digit)
    return digits

data = util.load_int_lists('input_sample.txt')
util.assert_equal(solve1(data), 3749, "Part1 sample")
util.assert_equal(solve2(data), 11387, "Part2 sample")

data = util.load_int_lists('input.txt')
util.assert_equal(solve1(data), 3119088655389, "Part1")
util.assert_equal(solve2(data), 264184041398847, "Part2")
