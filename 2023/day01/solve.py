def read_lines(fname):
    res = []
    f = open(fname);
    for line in f:
        res.append(line.strip())
    return res

def get_first_digit(line):
    for c in line:
        if c.isdigit():
            return int(c)

def get_last_digit(line):
    for c in line[::-1]:
        if c.isdigit():
            return int(c)

def get_number(line: str):
    d1 = get_first_digit(line)
    d2 = get_last_digit(line)
    return d1*10 + d2

digit_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

"""
returns the first single digit from a alfanumeric string containing digits and letters.
Some of the digits are spelled out with letters: one, two, three, four, five, six, seven, eight, nine also count as valid digits.
"""
def get_first_digit_or_spelled_digit(line:str) -> int:
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        # check that line[i:] starts with one if digit_names
        for index, dn in enumerate(digit_names):
            if line[i:].startswith(dn):
                return index+1
        
    raise Exception("invalid line: " + line)

def get_last_digit_or_spelled_digit(line:str) -> int:
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
        # check that line[i:] starts with one if digit_names
        for index, dn in enumerate(digit_names):
            if line[i:].startswith(dn):
                return index+1

    raise Exception("invalid line: " + line)

def get_number_or_spelled(line: str):
    d1 = get_first_digit_or_spelled_digit(line)
    d2 = get_last_digit_or_spelled_digit(line)
    return d1*10 + d2

line = '8jjpseven'
assert 7 == get_last_digit_or_spelled_digit(line)

lines = read_lines("input.txt")
part1 = part2 = 0
for line in lines:
    num1 = get_number(line)
    num2 = get_number_or_spelled(line)
    part1 += num1
    part2 += num2

print("Part1", part1)
print("Part2", part2)