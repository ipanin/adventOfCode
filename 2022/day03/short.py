from string import ascii_letters

lines = open("input.txt").read().strip().split("\n")

p1 = 0
for line in lines:
    middle = len(line) // 2
    common, = set(line[:middle]) & set(line[middle:])
    p1 += ascii_letters.index(common) + 1

p2 = 0
for i in range(0, len(lines), 3):
    line1, line2, line3 = lines[i:i+3]
    common, = set(line1) & set(line2) & set(line3)
    p2 += ascii_letters.index(common) + 1

print("Part1", p1)
print("Part2", p2)