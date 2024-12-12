# AoC 2020. Day 9: Encoding Error
import util


data = util.load_int_lines_list('input.txt')
L = len(data)

preamble_len = 25
for i in range(preamble_len, L):
    ok = False
    part1 = data[i]
    preamble = set(data[i-preamble_len:i])
    for a in preamble:
        b = part1 - a
        if b in preamble and a != b:
            ok = True
            break
    if not ok:
        break

print('Part 1: ', part1)  # 177777905

for i in range(L-1):
    total = data[i]
    for j in range(i+1, L):
        total += data[j]
        if total > part1:
            break
        if total == part1:
            lo = min(data[i:j])
            hi = max(data[i:j])
            print('Part 2: ', lo + hi)  # 23463012
            exit(0)

