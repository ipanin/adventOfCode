import re
data = [list(map(int, re.findall('\d+', line))) for line in open('input.txt')]
p1 = sum((a <= c and d <= b) or (c <= a and b <= d) for a,b,c,d in data)
p2 = sum((a <= d and c <= b) for a,b,c,d in data)
print(p1, p2)  # 595 952
