import re
p1 = p2 = 0
for line in open('input.txt'):
    a, b, c, d = map(int, re.findall('\d+', line))
    if a <= c and b >= d or c <= a and d >= b: p1 += 1
    if a <= d and c <= b: p2 += 1
print(p1, p2)  # 595 952
