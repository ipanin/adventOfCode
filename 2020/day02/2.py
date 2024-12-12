import util


def test1(data, expected):
    result = 0
    #line = "8-12 z: zxzzzzfxzlmzz"
    for line in lines:
        if valid(line):
            result += 1

    if result != expected:
        print(f"Error, expected = {expected}, actual = {result}")
    else:
        print("OK")

def valid(line:str) -> bool:
    parsed = line.split(' ')
    ranged = parsed[0]
    letter = parsed[1][0]
    passw = parsed[2]
    range_min = int(ranged.split("-")[0])-1
    range_max = int(ranged.split("-")[1])-1
    #cnt = passw.count(letter)
    return (passw[range_min] == letter and passw[range_max] != letter) or (passw[range_min] != letter and passw[range_max] == letter)

lines = util.load_str_lines_list('input.txt')

print("Part 2.")
test1(lines, 0)




