points1 = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
part1 = 0

points2 = { "(": 1, "[": 2, "{": 3, "<": 4 }
scores2 = []

for line in open("input.txt").readlines():
    stack = []
    score2 = 0
    for c in line.strip():
        if c in "(<[{":
            stack.append(c)
        else:
            b = stack.pop()
            if abs(ord(b) - ord(c)) > 2: # не парные скобки
                part1 += points1[c]
                break
    else:
        while len(stack):
            score2 = score2 * 5 + points2[stack.pop()]
        scores2.append(score2)

part2 = sorted(scores2)[len(scores2) // 2]
print(part1, part2)
