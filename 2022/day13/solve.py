import util

p1 = 0

lines = util.load_str_lines("input.txt")
idx = 1
res = []


def compare_lists(left, right):
    left_elements = split(left)
    right_elements = split(right)


for i in range(0,3,len(lines)):
    left = lines[i]
    right = lines[i+1]
    if compare_lists(left, right):
        res.append(idx)
    idx += 1
    break

print("Part1", sum(res))